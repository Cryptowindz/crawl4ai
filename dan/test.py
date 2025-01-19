import asyncio
import json
from typing import Dict, List, Set
from urllib.parse import urljoin, urlparse
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

class DocumentationCrawler:
    def __init__(self, max_pages: int = 50):
        # Configure browser settings
        self.browser_conf = BrowserConfig(
            headless=True,  # Run in headless mode
            java_script_enabled=True  # Enable JavaScript for dynamic content
        )
        
        # Configure markdown generator with content filter
        self.md_generator = DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(
                threshold=0.4,
                threshold_type="fixed"
            )
        )
        
        # Define schema for structured data extraction
        self.docs_schema = {
            "name": "Documentation Content",
            "baseSelector": "article, main, .documentation, .content, .docs-content, #__next, #root", # Added common React/Next.js root elements
            "fields": [
                {"name": "title", "selector": "h1, .docs-header h1, [class*='title']", "type": "text"},
                {"name": "sections", "selector": "h2, h3, .docs-section h2, .docs-section h3, [class*='heading']", "type": "text"},
                {"name": "code_blocks", "selector": "pre code, .docs-code, [class*='code']", "type": "text"},
                {"name": "paragraphs", "selector": "p, .docs-paragraph, [class*='paragraph']", "type": "text"},
                {"name": "links", "selector": "a", "type": "attribute", "attribute": "href"}
            ]
        }

        # Configure crawler settings with markdown generator
        self.run_conf = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,  # Always get fresh content
            markdown_generator=self.md_generator,
            extraction_strategy=JsonCssExtractionStrategy(self.docs_schema),
            page_timeout=30000  # 30 second timeout
        )

        self.max_pages = max_pages
        self.visited_urls: Set[str] = set()
        
        # Add selectors for finding documentation links
        self.docs_link_schema = {
            "name": "Documentation Links",
            "baseSelector": "body",
            "fields": [
                {
                    "name": "links",
                    "selector": (
                        "nav a, "           # Navigation links
                        ".sidebar a, "       # Sidebar links
                        "main a, "          # Main content links
                        "[role='navigation'] a, " # Navigation elements
                        ".docs-content a, "  # Documentation content links
                        "[class*='nav'] a, " # Any nav-related class
                        "[class*='menu'] a, " # Menu items
                        "[class*='sidebar'] a, " # Sidebar items
                        "header a, "         # Header links
                        "aside a"           # Sidebar/auxiliary content
                    ),
                    "type": "attribute",
                    "attribute": "href"
                }
            ]
        }

    def is_valid_doc_url(self, base_url: str, url: str) -> bool:
        """Check if URL is valid for crawling"""
        if not url:
            return False
            
        # Convert relative URLs to absolute
        full_url = urljoin(base_url, url)
        
        # Parse URLs
        base_parsed = urlparse(base_url)
        url_parsed = urlparse(full_url)
        
        print(f"Validating URL: {full_url}")
        
        # Skip obviously invalid URLs
        if any(url_parsed.path.endswith(ext) for ext in [
            '.png', '.jpg', '.jpeg', '.gif', '.pdf', '.zip', '.js', '.css'
        ]):
            print(f"Skipping file: {full_url}")
            return False
            
        # Accept if same domain and not visited
        is_valid = (
            url_parsed.netloc == base_parsed.netloc and
            full_url not in self.visited_urls and
            url != '/' and  # Skip root path
            not url.startswith('#') and  # Skip anchor links
            not any(skip in url_parsed.path.lower() for skip in ['assets/', 'images/', 'static/'])  # Skip asset directories
        )
        
        if is_valid:
            print(f"Valid URL found: {full_url}")
        
        return is_valid

    async def extract_doc_links(self, crawler: AsyncWebCrawler, url: str) -> List[str]:
        """Extract documentation links from a page"""
        # First try with navigation elements
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            page_timeout=15000,  # 15 seconds timeout
            wait_for="nav, .sidebar, .menu, .navigation",  # Wait for navigation elements
            extraction_strategy=JsonCssExtractionStrategy({
                "name": "Navigation Links",
                "baseSelector": "body",
                "fields": [
                    {
                        "name": "links",
                        "selector": (
                            "nav a[href], "    # Navigation links
                            ".sidebar a[href], " # Sidebar links
                            ".menu a[href], "   # Menu links
                            ".navigation a[href]" # Navigation links
                        ),
                        "type": "attribute",
                        "attribute": "href"
                    }
                ]
            })
        )

        try:
            print(f"\nExtracting links from {url}")
            result = await crawler.arun(url=url, config=config)
            
            if not result.extracted_content or result.extracted_content == '[{"links":["/"]}]':
                print("Initial extraction failed, trying content-based approach...")
                # Try with content elements and longer timeout
                config.page_timeout = 20000  # 20 second timeout
                config.wait_for = ".docs-content, .markdown-body, article, main"  # Wait for content
                config.extraction_strategy = JsonCssExtractionStrategy({
                    "name": "All Links",
                    "baseSelector": "body",
                    "fields": [
                        {
                            "name": "links",
                            "selector": "a[href]",  # Get all links
                            "type": "attribute",
                            "attribute": "href"
                        }
                    ]
                })
                result = await crawler.arun(url=url, config=config)
            
            links_data = json.loads(result.extracted_content) if result.extracted_content else []
            print(f"Raw extracted links data: {links_data}")
            
            all_found_links = set()
            if isinstance(links_data, list):
                for item in links_data:
                    if isinstance(item, dict) and 'links' in item:
                        links = {link.strip() for link in item['links'] if link and link.strip()}
                        all_found_links.update(links)
            
            print(f"All found links before filtering: {all_found_links}")
            
            # Convert relative to absolute URLs and filter
            valid_links = []
            for link in all_found_links:
                full_url = urljoin(url, link)
                if self.is_valid_doc_url(url, link):
                    valid_links.append(full_url)
                    print(f"Added valid link: {full_url}")
            
            return valid_links
            
        except Exception as e:
            print(f"Error extracting links from {url}: {str(e)}")
            return []

    async def crawl_documentation(self, start_urls: List[str]) -> List[Dict]:
        results = []
        urls_to_crawl = start_urls.copy()
        
        async with AsyncWebCrawler(config=self.browser_conf) as crawler:
            while urls_to_crawl and len(self.visited_urls) < self.max_pages:
                current_url = urls_to_crawl.pop(0)
                
                if current_url in self.visited_urls:
                    continue
                    
                self.visited_urls.add(current_url)
                
                try:
                    print(f"\nCrawling {current_url}...")
                    result = await crawler.arun(url=current_url, config=self.run_conf)
                    
                    # Handle markdown result correctly
                    markdown_content = result.markdown
                    if hasattr(markdown_content, 'fit_markdown'):
                        filtered_markdown = markdown_content.fit_markdown
                        raw_markdown = markdown_content.raw_markdown
                    else:
                        filtered_markdown = str(markdown_content)
                        raw_markdown = str(markdown_content)
                    
                    # Combine markdown and structured data
                    page_data = {
                        'url': current_url,
                        'markdown': filtered_markdown,
                        'raw_markdown': raw_markdown,
                        'structured_data': json.loads(result.extracted_content) if result.extracted_content else None,
                        'error': None
                    }
                    
                    results.append(page_data)
                    print(f"Successfully crawled {current_url}")
                    
                    # Extract and add new links to crawl
                    new_links = await self.extract_doc_links(crawler, current_url)
                    urls_to_crawl.extend([link for link in new_links if link not in self.visited_urls])
                    print(f"Found {len(new_links)} new links to crawl")
                    
                except Exception as e:
                    print(f"Error crawling {current_url}: {str(e)}")
                    results.append({
                        'url': current_url,
                        'markdown': None,
                        'structured_data': None,
                        'error': str(e)
                    })

        return results

    def save_results(self, results: List[Dict], output_dir: str = "crawled_docs"):
        """Save crawled results to files"""
        import os
        from urllib.parse import urlparse
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Save individual pages
        for result in results:
            if result['error']:
                continue
                
            # Create filename from URL path
            parsed_url = urlparse(result['url'])
            filename = (parsed_url.netloc + parsed_url.path).replace('/', '_').replace('.', '_')
            if not filename.strip('_'):  # Handle root URLs
                filename = parsed_url.netloc
            
            # Save markdown
            if result['markdown']:
                with open(f"{output_dir}/{filename}.md", 'w', encoding='utf-8') as f:
                    f.write(result['markdown'])
            
            # Save structured data
            if result['structured_data']:
                with open(f"{output_dir}/{filename}.json", 'w', encoding='utf-8') as f:
                    json.dump(result['structured_data'], f, indent=2)
        
        # Save crawl summary
        with open(f"{output_dir}/crawl_summary.json", 'w', encoding='utf-8') as f:
            summary = {
                'total_pages': len(results),
                'successful_pages': len([r for r in results if not r['error']]),
                'failed_pages': len([r for r in results if r['error']]),
                'crawled_urls': [r['url'] for r in results]
            }
            json.dump(summary, f, indent=2)

async def main():
    # Example documentation URLs to crawl
    start_urls = [
        "https://docs.meteora.ag/",
        "https://docs.meteora.ag/docs/",
        "https://docs.meteora.ag/docs/introduction",
        "https://docs.meteora.ag/docs/getting-started",
    ]
    
    crawler = DocumentationCrawler(max_pages=50)  # Limit to 50 pages per site
    results = await crawler.crawl_documentation(start_urls)
    
    # Save results to files
    crawler.save_results(results)
    
    # Print summary
    print("\nCrawling Summary:")
    print(f"Total pages crawled: {len(results)}")
    successful = len([r for r in results if not r['error']])
    print(f"Successful: {successful}")
    print(f"Failed: {len(results) - successful}")

if __name__ == "__main__":
    asyncio.run(main())

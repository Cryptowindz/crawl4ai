This website uses cookies to offer you a better browsing experience. Find out more on how we use cookies.
Opt-out[Details](https://solana.com/docs/intro/</privacy-policy#collection-of-information>)
Accept
[](https://solana.com/docs/intro/</>)
  * Learn
  * Developers
  * Solutions
  * Network
  * Community


Search`⌘``K`
[Documentation](https://solana.com/docs/intro/</docs>)[Courses](https://solana.com/docs/intro/</developers/courses>)[Guides](https://solana.com/docs/intro/</developers/guides>)[Cookbook](https://solana.com/docs/intro/</developers/cookbook>)[Terminology](https://solana.com/docs/intro/</docs/terminology>)[RPC API](https://solana.com/docs/intro/</docs/rpc>)[Stack Exchange](https://solana.com/docs/intro/<https:/solana.stackexchange.com/>)
##### Table of Contents
  * [What You'll Learn](https://solana.com/docs/intro/</docs/intro/quick-start#what-you-ll-learn>)
  * [Solana Playground](https://solana.com/docs/intro/</docs/intro/quick-start#solana-playground>)
  * [Create Playground Wallet](https://solana.com/docs/intro/</docs/intro/quick-start#create-playground-wallet>)
  * [Get Devnet SOL](https://solana.com/docs/intro/</docs/intro/quick-start#get-devnet-sol>)


* [Edit Page](https://solana.com/docs/intro/<https:/github.com/solana-foundation/developer-content/blob/main/docs/intro/quick-start/index.md?plain=1>)
* Scroll to Top
[Home](https://solana.com/docs/intro/</>)>[Solana Documentation](https://solana.com/docs/intro/</docs>)>Getting Started
# [Solana Quick Start Guide](https://solana.com/docs/intro/</docs/intro/quick-start>)
Welcome to the Solana Quick Start Guide! This hands-on guide will introduce you to the core concepts for building on Solana, regardless of your prior experience. By the end of this tutorial, you'll have a basic foundation in Solana development and be ready to explore more advanced topics.
## What You'll Learn [#](https://solana.com/docs/intro/<#what-you-ll-learn>)
In this tutorial, you'll learn about:
  * Understanding Accounts: Explore how data is stored on the Solana network.
  * Sending Transactions: Learn to interact with the Solana network by sending transactions.
  * Building and Deploying Programs: Create your first Solana program and deploy it to the network.
  * Program Derived Addresses (PDAs): Learn how to use PDAs to create deterministic addresses for accounts.
  * Cross-Program Invocations (CPIs): Learn how to make your programs interact with other programs on Solana.


The best part? You don't need to install anything! We'll be using Solana Playground, a browser-based development environment, for all our examples. This means you can follow along, copy and paste code, and see results immediately, all from your web browser. Basic programming knowledge is helpful but not required.
Let's dive in and start building on Solana!
## Solana Playground [#](https://solana.com/docs/intro/<#solana-playground>)
Solana Playground (Solpg) is a browser-based development environment that allows you to quickly develop, deploy, and test Solana programs!
Open a new tab in your web browser and navigate to <https://beta.solpg.io/>.
### Create Playground Wallet [#](https://solana.com/docs/intro/<#create-playground-wallet>)
If you're new to Solana Playground, the first step is to create your Playground Wallet. This wallet will allow you to interact with the Solana network right from your browser.
#### Step 1. Connect to Playground [#](https://solana.com/docs/intro/<#step-1-connect-to-playground>)
Click the "Not connected" button at the bottom left of the screen.
![Not Connected](https://solana-developer-content.vercel.app/assets/docs/intro/quickstart/pg-not-connected.png)Not Connected
#### Step 2. Create Your Wallet [#](https://solana.com/docs/intro/<#step-2-create-your-wallet>)
You'll see an option to save your wallet's keypair. Optionally, save your wallet's keypair for backup and then click "Continue".
![Create Playground Wallet](https://solana-developer-content.vercel.app/assets/docs/intro/quickstart/pg-create-wallet.png)Create Playground Wallet
You should now see your wallet's address, SOL balance, and connected cluster (devnet by default) at the bottom of the window.
![Connected](https://solana-developer-content.vercel.app/assets/docs/intro/quickstart/pg-connected.png)Connected
Info
Your Playground Wallet will be saved in your browser's local storage. Clearing your browser cache will remove your saved wallet.
Some definitions you may find helpful:
  * _wallet address_ : a unique identifier for a digital wallet, used to send or receive crypto assets on a blockchain. Each wallet address is a string of alphanumeric characters that represents a specific destination on the network. Think of it like an email address or bank account number—if someone wants to send you cryptocurrency, they need your wallet address to direct the funds.
  * _connected cluster_ : a set of network nodes that work together to maintain a synchronized copy of the blockchain. These clusters are essential for providing a decentralized, distributed ledger and powering the Solana network by validating transactions, securing the chain, and executing programs (smart contracts).


### Get Devnet SOL [#](https://solana.com/docs/intro/<#get-devnet-sol>)
Before we start building, we first need some devnet SOL.
From a developer's perspective, SOL is required for two main use cases:
  * To create accounts where we can store data or deploy programs
  * To pay for transaction fees when we interact with the network


Below are two methods to fund your wallet with devnet SOL:
#### Option 1: Using the Playground Terminal [#](https://solana.com/docs/intro/<#option-1-using-the-playground-terminal>)
To fund your Playground wallet with devnet SOL. In the Playground terminal, run:
Terminal
```
solana airdrop 5
```

#### Option 2: Using the Devnet Faucet [#](https://solana.com/docs/intro/<#option-2-using-the-devnet-faucet>)
If the airdrop command doesn't work (due to rate limits or errors), you can use the [Web Faucet](https://solana.com/docs/intro/<https:/faucet.solana.com/>).
  * Enter your wallet address (found at the bottom of the Playground screen) and select an amount
  * Click "Confirm Airdrop" to receive your devnet SOL


![Faucet Airdrop](https://solana-developer-content.vercel.app/assets/docs/intro/quickstart/faucet-airdrop.gif)Faucet Airdrop
[Previous« Solana Documentation](https://solana.com/docs/intro/</docs>)[NextReading from Network »](https://solana.com/docs/intro/</docs/intro/quick-start/reading-from-network>)
  * [Getting Started](https://solana.com/docs/intro/</docs>)
    * [Quick Start](https://solana.com/docs/intro/</docs/intro/quick-start>)
      * [Reading from Network](https://solana.com/docs/intro/</docs/intro/quick-start/reading-from-network>)
      * [Writing to Network](https://solana.com/docs/intro/</docs/intro/quick-start/writing-to-network>)
      * [Deploying Programs](https://solana.com/docs/intro/</docs/intro/quick-start/deploying-programs>)
      * [Program Derived Address](https://solana.com/docs/intro/</docs/intro/quick-start/program-derived-address>)
      * [Cross Program Invocation](https://solana.com/docs/intro/</docs/intro/quick-start/cross-program-invocation>)
    * [Installation](https://solana.com/docs/intro/</docs/intro/installation>)
    * [Intro to Development](https://solana.com/docs/intro/</docs/intro/dev>)
    * [Wallets](https://solana.com/docs/intro/</docs/intro/wallets>)
  * [Core Concepts](https://solana.com/docs/intro/</docs/core>)
    * [Solana Account Model](https://solana.com/docs/intro/</docs/core/accounts>)
    * [Transactions and Instructions](https://solana.com/docs/intro/</docs/core/transactions>)
    * [Fees on Solana](https://solana.com/docs/intro/</docs/core/fees>)
    * [Programs on Solana](https://solana.com/docs/intro/</docs/core/programs>)
    * [Program Derived Address](https://solana.com/docs/intro/</docs/core/pda>)
    * [Cross Program Invocation](https://solana.com/docs/intro/</docs/core/cpi>)
    * [Tokens on Solana](https://solana.com/docs/intro/</docs/core/tokens>)
    * [Clusters & Endpoints](https://solana.com/docs/intro/</docs/core/clusters>)
  * [The Solana Toolkit](https://solana.com/docs/intro/</docs/toolkit>)
    * [Getting Started](https://solana.com/docs/intro/</docs/toolkit/getting-started>)
    * Creating a Project
      * [Overview](https://solana.com/docs/intro/</docs/toolkit/projects/overview>)
      * [Basic Anchor](https://solana.com/docs/intro/</docs/toolkit/projects/anchor-init>)
      * [Solana Programs](https://solana.com/docs/intro/</docs/toolkit/projects/solana-program>)
      * [Web App](https://solana.com/docs/intro/</docs/toolkit/projects/web-app>)
      * [Mobile App](https://solana.com/docs/intro/</docs/toolkit/projects/mobile-app>)
      * [Existing Projects](https://solana.com/docs/intro/</docs/toolkit/projects/existing-project>)
      * [Project layout](https://solana.com/docs/intro/</docs/toolkit/projects/project-layout>)
    * [Best Practices](https://solana.com/docs/intro/</docs/toolkit/best-practices>)
    * [Local Validator](https://solana.com/docs/intro/</docs/toolkit/local-validator>)
    * Test Suite
      * [Overview](https://solana.com/docs/intro/</docs/toolkit/test-suite/overview>)
      * [Testing Basics](https://solana.com/docs/intro/</docs/toolkit/test-suite/basics>)
      * [Code Coverage](https://solana.com/docs/intro/</docs/toolkit/test-suite/code-coverage>)
      * [Fuzz Tester](https://solana.com/docs/intro/</docs/toolkit/test-suite/fuzz-tester>)
      * [Security Scanner](https://solana.com/docs/intro/</docs/toolkit/test-suite/security-scanner>)
      * [JavaScript Tests](https://solana.com/docs/intro/</docs/toolkit/test-suite/js-test>)
      * [Rust Tests](https://solana.com/docs/intro/</docs/toolkit/test-suite/rust-tests>)
    * [Troubleshooting](https://solana.com/docs/intro/</docs/toolkit/troubleshooting>)
  * Solana Clients
    * [Rust](https://solana.com/docs/intro/</docs/clients/rust>)
    * [JavaScript / TypeScript](https://solana.com/docs/intro/</docs/clients/javascript>)
    * [Web3.js API Examples](https://solana.com/docs/intro/</docs/clients/javascript-reference>)
  * Developing Programs
    * [Anchor Framework](https://solana.com/docs/intro/</docs/programs/anchor>)
      * [Program Structure](https://solana.com/docs/intro/</docs/programs/anchor/program-structure>)
      * [IDL File](https://solana.com/docs/intro/</docs/programs/anchor/idl>)
      * [JS/TS Client](https://solana.com/docs/intro/</docs/programs/anchor/client-typescript>)
      * [PDAs with Anchor](https://solana.com/docs/intro/</docs/programs/anchor/pda>)
      * [CPIs with Anchor](https://solana.com/docs/intro/</docs/programs/anchor/cpi>)
    * [Rust Programs](https://solana.com/docs/intro/</docs/programs/rust>)
      * [Program Structure](https://solana.com/docs/intro/</docs/programs/rust/program-structure>)
    * [Deploying Programs](https://solana.com/docs/intro/</docs/programs/deploying>)
    * [Program Examples](https://solana.com/docs/intro/</docs/programs/examples>)
    * [Testing with NodeJS](https://solana.com/docs/intro/</docs/programs/testing>)
    * [Limitations](https://solana.com/docs/intro/</docs/programs/limitations>)
    * [FAQ](https://solana.com/docs/intro/</docs/programs/faq>)
  * Advanced Topics
    * [Confirmation & Expiration](https://solana.com/docs/intro/</docs/advanced/confirmation>)
    * [Retrying Transactions](https://solana.com/docs/intro/</docs/advanced/retry>)
    * [Versioned Transactions](https://solana.com/docs/intro/</docs/advanced/versions>)
    * [Address Lookup Tables](https://solana.com/docs/intro/</docs/advanced/lookup-tables>)
    * [State Compression](https://solana.com/docs/intro/</docs/advanced/state-compression>)
    * [Actions and Blinks](https://solana.com/docs/intro/</docs/advanced/actions>)
  * [Economics](https://solana.com/docs/intro/</docs/economics>)
    * Inflation
      * [Proposed Inflation Schedule](https://solana.com/docs/intro/</docs/economics/inflation/inflation-schedule>)
      * [Inflation Terminology](https://solana.com/docs/intro/</docs/economics/inflation/terminology>)
    * [Staking](https://solana.com/docs/intro/</docs/economics/staking>)
      * [Stake Accounts](https://solana.com/docs/intro/</docs/economics/staking/stake-accounts>)
      * [Stake Programming](https://solana.com/docs/intro/</docs/economics/staking/stake-programming>)
  * More Information
    * [Add Solana to Your Exchange](https://solana.com/docs/intro/</docs/more/exchange>)


Managed by
[](https://solana.com/docs/intro/</>)
[](https://solana.com/docs/intro/</youtube>)[](https://solana.com/docs/intro/</twitter>)[](https://solana.com/docs/intro/</discord>)[](https://solana.com/docs/intro/</reddit>)[](https://solana.com/docs/intro/</github>)[](https://solana.com/docs/intro/</telegram>)
© 2025 Solana Foundation. All rights reserved.
Solana
  * [Grants](https://solana.com/docs/intro/<https:/solana.org/grants>)
  * [Break Solana](https://solana.com/docs/intro/<https:/break.solana.com/>)
  * [Media Kit](https://solana.com/docs/intro/</branding>)
  * [Careers](https://solana.com/docs/intro/<https:/jobs.solana.com/>)
  * [Disclaimer](https://solana.com/docs/intro/</tos>)
  * [Privacy Policy](https://solana.com/docs/intro/</privacy-policy>)


Get Connected
  * [Blog](https://solana.com/docs/intro/</news>)
  * [Newsletter](https://solana.com/docs/intro/</newsletter>)


en
© 2025 Solana Foundation. All rights reserved.

This website uses cookies to offer you a better browsing experience. Find out more on how we use cookies.
Opt-out[Details](https://solana.com/docs/</privacy-policy#collection-of-information>)
Accept
[](https://solana.com/docs/</>)
  * Learn
  * Developers
  * Solutions
  * Network
  * Community


Search`⌘``K`
[Documentation](https://solana.com/docs/</docs>)[Courses](https://solana.com/docs/</developers/courses>)[Guides](https://solana.com/docs/</developers/guides>)[Cookbook](https://solana.com/docs/</developers/cookbook>)[Terminology](https://solana.com/docs/</docs/terminology>)[RPC API](https://solana.com/docs/</docs/rpc>)[Stack Exchange](https://solana.com/docs/<https:/solana.stackexchange.com/>)
##### Table of Contents
  * [Solana Account Model](https://solana.com/docs/</docs/core#solana-account-model>)
  * [Transactions and Instructions](https://solana.com/docs/</docs/core#transactions-and-instructions>)
  * [Fees on Solana](https://solana.com/docs/</docs/core#fees-on-solana>)
  * [Programs on Solana](https://solana.com/docs/</docs/core#programs-on-solana>)
  * [Program Derived Address](https://solana.com/docs/</docs/core#program-derived-address>)
  * [Cross Program Invocation](https://solana.com/docs/</docs/core#cross-program-invocation>)
  * [Tokens on Solana](https://solana.com/docs/</docs/core#tokens-on-solana>)
  * [Clusters and Endpoints](https://solana.com/docs/</docs/core#clusters-and-endpoints>)


* [Edit Page](https://solana.com/docs/<https:/github.com/solana-foundation/developer-content/blob/main/docs/core/index.md?plain=1>)
* Scroll to Top
[Home](https://solana.com/docs/</>)>[Solana Documentation](https://solana.com/docs/</docs>)
# [Core Concepts](https://solana.com/docs/</docs/core>)
Build a strong understanding of the core concepts that make Solana different from other blockchains. Understanding the "Solana programming model" through these core concepts is very important to maximize your success as a Solana blockchain developer.
## Solana Account Model [#](https://solana.com/docs/<#solana-account-model>)
On Solana, all data is stored in what are referred to as "accounts”. The way data is organized on the Solana blockchain resembles a [key-value store](https://solana.com/docs/<https:/en.wikipedia.org/wiki/Key%E2%80%93value_database>), where each entry in the database is called an "account".
Learn more about [Accounts](https://solana.com/docs/</docs/core/accounts>) here.
## Transactions and Instructions [#](https://solana.com/docs/<#transactions-and-instructions>)
On Solana, we send [transactions](https://solana.com/docs/</docs/core/transactions#transaction>) to interact with the network. Transactions include one or more [instructions](https://solana.com/docs/</docs/core/transactions#instruction>), each representing a specific operation to be processed. The execution logic for instructions is stored on [programs](https://solana.com/docs/</docs/core/programs>) deployed to the Solana network, where each program stores its own set of instructions.
Learn more about [Transactions](https://solana.com/docs/</docs/core/transactions>) and [Instructions](https://solana.com/docs/</docs/core/transactions#instruction>) here.
## Fees on Solana [#](https://solana.com/docs/<#fees-on-solana>)
The Solana blockchain has a few different types of fees and costs that are incurred to use the permissionless network. These can be segmented into a few specific types:
  * [Transaction Fees](https://solana.com/docs/</docs/core/fees#transaction-fees>) - A fee to have validators process transactions/instructions
  * [Prioritization Fees](https://solana.com/docs/</docs/core/fees#prioritization-fees>) - An optional fee to boost transactions processing order
  * [Rent](https://solana.com/docs/</docs/core/fees#rent>) - A withheld balance to keep data stored on-chain


Learn more about [Fees on Solana](https://solana.com/docs/</docs/core/fees>) here.
## Programs on Solana [#](https://solana.com/docs/<#programs-on-solana>)
In the Solana ecosystem, "smart contracts" are called programs. Each program is an on-chain account that stores executable logic, organized into specific functions referred to as _instructions_ and called via _instruction handler_ functions within the respective deployed program.
Learn more about [Programs on Solana](https://solana.com/docs/</docs/core/programs>) here.
## Program Derived Address [#](https://solana.com/docs/<#program-derived-address>)
Program Derived Addresses (PDAs) provide developers on Solana with two main use cases:
  * **Deterministic Account Addresses** : PDAs provide a mechanism to deterministically derive an address using a combination of optional "seeds" (predefined inputs) and a specific program ID.
  * **Enable Program Signing** : The Solana runtime enables programs to "sign" for PDAs which are derived from its program ID.


You can think of PDAs as a way to create hashmap-like structures on-chain from a predefined set of inputs (e.g. strings, numbers, and other account addresses).
Learn more about [Program Derived Address](https://solana.com/docs/</docs/core/pda>) here.
## Cross Program Invocation [#](https://solana.com/docs/<#cross-program-invocation>)
A Cross Program Invocation (CPI) refers to when one program invokes the instructions of another program. This mechanism allows for the composability of Solana programs.
You can think of instructions as API endpoints that a program exposes to the network and a CPI as one API internally invoking another API.
Learn more about [Cross Program Invocation](https://solana.com/docs/</docs/core/cpi>) here.
## Tokens on Solana [#](https://solana.com/docs/<#tokens-on-solana>)
Tokens are digital assets that represent ownership over diverse categories of assets. Tokenization enables the digitalization of property rights, serving as a fundamental component for managing both fungible and non-fungible assets.
  * Fungible Tokens represent interchangeable and divisible assets of the same type and value (ex. USDC).
  * Non-fungible Tokens (NFT) represent ownership of indivisible assets (e.g. artwork).


Learn more about [Tokens on Solana](https://solana.com/docs/</docs/core/tokens>) here.
## Clusters and Endpoints [#](https://solana.com/docs/<#clusters-and-endpoints>)
The Solana blockchain has several different groups of validators, known as [Clusters](https://solana.com/docs/</docs/core/clusters>). Each serving different purposes within the overall ecosystem and containing dedicated api nodes to fulfill [JSON-RPC](https://solana.com/docs/</docs/rpc>) requests for their respective Cluster.
The individual nodes within a Cluster are owned and operated by third parties, with a public endpoint available for each.
There are three primary clusters on the Solana network, each with a different public endpoint:
  * Mainnet - `https://api.mainnet-beta.solana.com`
  * Devnet - `https://api.devnet.solana.com`
  * Testnet - `https://api.testnet.solana.com`


Learn more about [Clusters and Endpoints](https://solana.com/docs/</docs/core/clusters>) here.
[Previous« Wallets](https://solana.com/docs/</docs/intro/wallets>)[NextSolana Account Model »](https://solana.com/docs/</docs/core/accounts>)
  * [Getting Started](https://solana.com/docs/</docs>)
    * [Quick Start](https://solana.com/docs/</docs/intro/quick-start>)
      * [Reading from Network](https://solana.com/docs/</docs/intro/quick-start/reading-from-network>)
      * [Writing to Network](https://solana.com/docs/</docs/intro/quick-start/writing-to-network>)
      * [Deploying Programs](https://solana.com/docs/</docs/intro/quick-start/deploying-programs>)
      * [Program Derived Address](https://solana.com/docs/</docs/intro/quick-start/program-derived-address>)
      * [Cross Program Invocation](https://solana.com/docs/</docs/intro/quick-start/cross-program-invocation>)
    * [Installation](https://solana.com/docs/</docs/intro/installation>)
    * [Intro to Development](https://solana.com/docs/</docs/intro/dev>)
    * [Wallets](https://solana.com/docs/</docs/intro/wallets>)
  * [Core Concepts](https://solana.com/docs/</docs/core>)
    * [Solana Account Model](https://solana.com/docs/</docs/core/accounts>)
    * [Transactions and Instructions](https://solana.com/docs/</docs/core/transactions>)
    * [Fees on Solana](https://solana.com/docs/</docs/core/fees>)
    * [Programs on Solana](https://solana.com/docs/</docs/core/programs>)
    * [Program Derived Address](https://solana.com/docs/</docs/core/pda>)
    * [Cross Program Invocation](https://solana.com/docs/</docs/core/cpi>)
    * [Tokens on Solana](https://solana.com/docs/</docs/core/tokens>)
    * [Clusters & Endpoints](https://solana.com/docs/</docs/core/clusters>)
  * [The Solana Toolkit](https://solana.com/docs/</docs/toolkit>)
    * [Getting Started](https://solana.com/docs/</docs/toolkit/getting-started>)
    * Creating a Project
      * [Overview](https://solana.com/docs/</docs/toolkit/projects/overview>)
      * [Basic Anchor](https://solana.com/docs/</docs/toolkit/projects/anchor-init>)
      * [Solana Programs](https://solana.com/docs/</docs/toolkit/projects/solana-program>)
      * [Web App](https://solana.com/docs/</docs/toolkit/projects/web-app>)
      * [Mobile App](https://solana.com/docs/</docs/toolkit/projects/mobile-app>)
      * [Existing Projects](https://solana.com/docs/</docs/toolkit/projects/existing-project>)
      * [Project layout](https://solana.com/docs/</docs/toolkit/projects/project-layout>)
    * [Best Practices](https://solana.com/docs/</docs/toolkit/best-practices>)
    * [Local Validator](https://solana.com/docs/</docs/toolkit/local-validator>)
    * Test Suite
      * [Overview](https://solana.com/docs/</docs/toolkit/test-suite/overview>)
      * [Testing Basics](https://solana.com/docs/</docs/toolkit/test-suite/basics>)
      * [Code Coverage](https://solana.com/docs/</docs/toolkit/test-suite/code-coverage>)
      * [Fuzz Tester](https://solana.com/docs/</docs/toolkit/test-suite/fuzz-tester>)
      * [Security Scanner](https://solana.com/docs/</docs/toolkit/test-suite/security-scanner>)
      * [JavaScript Tests](https://solana.com/docs/</docs/toolkit/test-suite/js-test>)
      * [Rust Tests](https://solana.com/docs/</docs/toolkit/test-suite/rust-tests>)
    * [Troubleshooting](https://solana.com/docs/</docs/toolkit/troubleshooting>)
  * Solana Clients
    * [Rust](https://solana.com/docs/</docs/clients/rust>)
    * [JavaScript / TypeScript](https://solana.com/docs/</docs/clients/javascript>)
    * [Web3.js API Examples](https://solana.com/docs/</docs/clients/javascript-reference>)
  * Developing Programs
    * [Anchor Framework](https://solana.com/docs/</docs/programs/anchor>)
      * [Program Structure](https://solana.com/docs/</docs/programs/anchor/program-structure>)
      * [IDL File](https://solana.com/docs/</docs/programs/anchor/idl>)
      * [JS/TS Client](https://solana.com/docs/</docs/programs/anchor/client-typescript>)
      * [PDAs with Anchor](https://solana.com/docs/</docs/programs/anchor/pda>)
      * [CPIs with Anchor](https://solana.com/docs/</docs/programs/anchor/cpi>)
    * [Rust Programs](https://solana.com/docs/</docs/programs/rust>)
      * [Program Structure](https://solana.com/docs/</docs/programs/rust/program-structure>)
    * [Deploying Programs](https://solana.com/docs/</docs/programs/deploying>)
    * [Program Examples](https://solana.com/docs/</docs/programs/examples>)
    * [Testing with NodeJS](https://solana.com/docs/</docs/programs/testing>)
    * [Limitations](https://solana.com/docs/</docs/programs/limitations>)
    * [FAQ](https://solana.com/docs/</docs/programs/faq>)
  * Advanced Topics
    * [Confirmation & Expiration](https://solana.com/docs/</docs/advanced/confirmation>)
    * [Retrying Transactions](https://solana.com/docs/</docs/advanced/retry>)
    * [Versioned Transactions](https://solana.com/docs/</docs/advanced/versions>)
    * [Address Lookup Tables](https://solana.com/docs/</docs/advanced/lookup-tables>)
    * [State Compression](https://solana.com/docs/</docs/advanced/state-compression>)
    * [Actions and Blinks](https://solana.com/docs/</docs/advanced/actions>)
  * [Economics](https://solana.com/docs/</docs/economics>)
    * Inflation
      * [Proposed Inflation Schedule](https://solana.com/docs/</docs/economics/inflation/inflation-schedule>)
      * [Inflation Terminology](https://solana.com/docs/</docs/economics/inflation/terminology>)
    * [Staking](https://solana.com/docs/</docs/economics/staking>)
      * [Stake Accounts](https://solana.com/docs/</docs/economics/staking/stake-accounts>)
      * [Stake Programming](https://solana.com/docs/</docs/economics/staking/stake-programming>)
  * More Information
    * [Add Solana to Your Exchange](https://solana.com/docs/</docs/more/exchange>)


Managed by
[](https://solana.com/docs/</>)
[](https://solana.com/docs/</youtube>)[](https://solana.com/docs/</twitter>)[](https://solana.com/docs/</discord>)[](https://solana.com/docs/</reddit>)[](https://solana.com/docs/</github>)[](https://solana.com/docs/</telegram>)
© 2025 Solana Foundation. All rights reserved.
Solana
  * [Grants](https://solana.com/docs/<https:/solana.org/grants>)
  * [Break Solana](https://solana.com/docs/<https:/break.solana.com/>)
  * [Media Kit](https://solana.com/docs/</branding>)
  * [Careers](https://solana.com/docs/<https:/jobs.solana.com/>)
  * [Disclaimer](https://solana.com/docs/</tos>)
  * [Privacy Policy](https://solana.com/docs/</privacy-policy>)


Get Connected
  * [Blog](https://solana.com/docs/</news>)
  * [Newsletter](https://solana.com/docs/</newsletter>)


en
© 2025 Solana Foundation. All rights reserved.

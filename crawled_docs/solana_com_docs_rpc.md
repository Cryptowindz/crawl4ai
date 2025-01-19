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
  * [Configuring State Commitment](https://solana.com/docs/</docs/rpc#configuring-state-commitment>)
  * [Default Commitment](https://solana.com/docs/</docs/rpc#default-commitment>)
  * [RpcResponse Structure](https://solana.com/docs/</docs/rpc#rpcresponse-structure>)
  * [Parsed Responses](https://solana.com/docs/</docs/rpc#parsed-responses>)
  * [Filter criteria](https://solana.com/docs/</docs/rpc#filter-criteria>)


* [Edit Page](https://solana.com/docs/<https:/github.com/solana-foundation/developer-content/blob/main/docs/rpc/index.mdx?plain=1>)
* Scroll to Top
[Home](https://solana.com/docs/</>)>[Solana Documentation](https://solana.com/docs/</docs>)
# [Solana RPC Methods & Documentation](https://solana.com/docs/</docs/rpc>)
Interact with Solana nodes directly with the JSON RPC API via the HTTP and Websocket methods.
## Configuring State Commitment [#](https://solana.com/docs/<#configuring-state-commitment>)
For preflight checks and transaction processing, Solana nodes choose which bank state to query based on a commitment requirement set by the client. The commitment describes how finalized a block is at that point in time. When querying the ledger state, it's recommended to use lower levels of commitment to report progress and higher levels to ensure the state will not be rolled back.
In descending order of commitment (most finalized to least finalized), clients may specify:
  * `finalized` - the node will query the most recent block confirmed by supermajority of the cluster as having reached maximum lockout, meaning the cluster has recognized this block as finalized
  * `confirmed` - the node will query the most recent block that has been voted on by supermajority of the cluster. 
    * It incorporates votes from gossip and replay.
    * It does not count votes on descendants of a block, only direct votes on that block.
    * This confirmation level also upholds "optimistic confirmation" guarantees in release 1.3 and onwards.
  * `processed` - the node will query its most recent block. Note that the block may still be skipped by the cluster.


For processing many dependent transactions in series, it's recommended to use `confirmed` commitment, which balances speed with rollback safety. For total safety, it's recommended to use `finalized` commitment.
### Default Commitment [#](https://solana.com/docs/<#default-commitment>)
If commitment configuration is not provided, the node will [default to `finalized` commitment](https://solana.com/docs/<https:/github.com/anza-xyz/agave/blob/aa0922d6845e119ba466f88497e8209d1c82febc/sdk/src/commitment_config.rs#L199-L203>)
Only methods that query bank state accept the commitment parameter. They are indicated in the API Reference below.
## RpcResponse Structure [#](https://solana.com/docs/<#rpcresponse-structure>)
Many methods that take a commitment parameter return an RpcResponse JSON object comprised of two parts:
  * `context` : An RpcResponseContext JSON structure including a `slot` field at which the operation was evaluated.
  * `value` : The value returned by the operation itself.


## Parsed Responses [#](https://solana.com/docs/<#parsed-responses>)
Some methods support an `encoding` parameter, and can return account or instruction data in parsed JSON format if `"encoding":"jsonParsed"` is requested and the node has a parser for the owning program. Solana nodes currently support JSON parsing for the following native and SPL programs:
Program| Account State| Instructions  
---|---|---  
Address Lookup| v1.15.0| v1.15.0  
BPF Loader| n/a| stable  
BPF Upgradeable Loader| stable| stable  
Config| stable  
SPL Associated Token Account| n/a| stable  
SPL Memo| n/a| stable  
SPL Token| stable| stable  
SPL Token 2022| stable| stable  
Stake| stable| stable  
Vote| stable| stable  
The list of account parsers can be found [here](https://solana.com/docs/<https:/github.com/solana-labs/solana/blob/master/account-decoder/src/parse_account_data.rs>), and instruction parsers [here](https://solana.com/docs/<https:/github.com/solana-labs/solana/blob/master/transaction-status/src/parse_instruction.rs>).
## Filter criteria [#](https://solana.com/docs/<#filter-criteria>)
Some methods support providing a `filters` object to enable pre-filtering the data returned within the RpcResponse JSON object. The following filters exist:
  * `memcmp: object` - compares a provided series of bytes with program account data at a particular offset. Fields:
    * `offset: usize` - offset into program account data to start comparison
    * `bytes: string` - data to match, as encoded string
    * `encoding: string` - encoding for filter `bytes` data, either "base58" or "base64". Data is limited in size to 128 or fewer decoded bytes. **NEW: This field, and base64 support generally, is only available in solana-core v1.14.0 or newer. Please omit when querying nodes on earlier versions**
  * `dataSize: u64` - compares the program account data length with the provided data size


[Previous« Solana Documentation](https://solana.com/docs/</docs>)[NextData Structures as JSON »](https://solana.com/docs/</docs/rpc/json-structures>)
  * [Solana RPC Methods](https://solana.com/docs/</docs/rpc>)
    * [Data Structures as JSON](https://solana.com/docs/</docs/rpc/json-structures>)
    * [HTTP Methods](https://solana.com/docs/</docs/rpc/http>)
      * [getAccountInfo](https://solana.com/docs/</docs/rpc/http/getaccountinfo>)
      * [getBalance](https://solana.com/docs/</docs/rpc/http/getbalance>)
      * [getBlock](https://solana.com/docs/</docs/rpc/http/getblock>)
      * [getBlockCommitment](https://solana.com/docs/</docs/rpc/http/getblockcommitment>)
      * [getBlockHeight](https://solana.com/docs/</docs/rpc/http/getblockheight>)
      * [getBlockProduction](https://solana.com/docs/</docs/rpc/http/getblockproduction>)
      * [getBlockTime](https://solana.com/docs/</docs/rpc/http/getblocktime>)
      * [getBlocks](https://solana.com/docs/</docs/rpc/http/getblocks>)
      * [getBlocksWithLimit](https://solana.com/docs/</docs/rpc/http/getblockswithlimit>)
      * [getClusterNodes](https://solana.com/docs/</docs/rpc/http/getclusternodes>)
      * [getEpochInfo](https://solana.com/docs/</docs/rpc/http/getepochinfo>)
      * [getEpochSchedule](https://solana.com/docs/</docs/rpc/http/getepochschedule>)
      * [getFeeForMessage](https://solana.com/docs/</docs/rpc/http/getfeeformessage>)
      * [getFirstAvailableBlock](https://solana.com/docs/</docs/rpc/http/getfirstavailableblock>)
      * [getGenesisHash](https://solana.com/docs/</docs/rpc/http/getgenesishash>)
      * [getHealth](https://solana.com/docs/</docs/rpc/http/gethealth>)
      * [getHighestSnapshotSlot](https://solana.com/docs/</docs/rpc/http/gethighestsnapshotslot>)
      * [getIdentity](https://solana.com/docs/</docs/rpc/http/getidentity>)
      * [getInflationGovernor](https://solana.com/docs/</docs/rpc/http/getinflationgovernor>)
      * [getInflationRate](https://solana.com/docs/</docs/rpc/http/getinflationrate>)
      * [getInflationReward](https://solana.com/docs/</docs/rpc/http/getinflationreward>)
      * [getLargestAccounts](https://solana.com/docs/</docs/rpc/http/getlargestaccounts>)
      * [getLatestBlockhash](https://solana.com/docs/</docs/rpc/http/getlatestblockhash>)
      * [getLeaderSchedule](https://solana.com/docs/</docs/rpc/http/getleaderschedule>)
      * [getMaxRetransmitSlot](https://solana.com/docs/</docs/rpc/http/getmaxretransmitslot>)
      * [getMaxShredInsertSlot](https://solana.com/docs/</docs/rpc/http/getmaxshredinsertslot>)
      * [getMinimumBalanceForRentExemption](https://solana.com/docs/</docs/rpc/http/getminimumbalanceforrentexemption>)
      * [getMultipleAccounts](https://solana.com/docs/</docs/rpc/http/getmultipleaccounts>)
      * [getProgramAccounts](https://solana.com/docs/</docs/rpc/http/getprogramaccounts>)
      * [getRecentPerformanceSamples](https://solana.com/docs/</docs/rpc/http/getrecentperformancesamples>)
      * [getRecentPrioritizationFees](https://solana.com/docs/</docs/rpc/http/getrecentprioritizationfees>)
      * [getSignatureStatuses](https://solana.com/docs/</docs/rpc/http/getsignaturestatuses>)
      * [getSignaturesForAddress](https://solana.com/docs/</docs/rpc/http/getsignaturesforaddress>)
      * [getSlot](https://solana.com/docs/</docs/rpc/http/getslot>)
      * [getSlotLeader](https://solana.com/docs/</docs/rpc/http/getslotleader>)
      * [getSlotLeaders](https://solana.com/docs/</docs/rpc/http/getslotleaders>)
      * [getStakeMinimumDelegation](https://solana.com/docs/</docs/rpc/http/getstakeminimumdelegation>)
      * [getSupply](https://solana.com/docs/</docs/rpc/http/getsupply>)
      * [getTokenAccountBalance](https://solana.com/docs/</docs/rpc/http/gettokenaccountbalance>)
      * [getTokenAccountsByDelegate](https://solana.com/docs/</docs/rpc/http/gettokenaccountsbydelegate>)
      * [getTokenAccountsByOwner](https://solana.com/docs/</docs/rpc/http/gettokenaccountsbyowner>)
      * [getTokenLargestAccounts](https://solana.com/docs/</docs/rpc/http/gettokenlargestaccounts>)
      * [getTokenSupply](https://solana.com/docs/</docs/rpc/http/gettokensupply>)
      * [getTransaction](https://solana.com/docs/</docs/rpc/http/gettransaction>)
      * [getTransactionCount](https://solana.com/docs/</docs/rpc/http/gettransactioncount>)
      * [getVersion](https://solana.com/docs/</docs/rpc/http/getversion>)
      * [getVoteAccounts](https://solana.com/docs/</docs/rpc/http/getvoteaccounts>)
      * [isBlockhashValid](https://solana.com/docs/</docs/rpc/http/isblockhashvalid>)
      * [minimumLedgerSlot](https://solana.com/docs/</docs/rpc/http/minimumledgerslot>)
      * [requestAirdrop](https://solana.com/docs/</docs/rpc/http/requestairdrop>)
      * [sendTransaction](https://solana.com/docs/</docs/rpc/http/sendtransaction>)
      * [simulateTransaction](https://solana.com/docs/</docs/rpc/http/simulatetransaction>)
    * [Websocket Methods](https://solana.com/docs/</docs/rpc/websocket>)
      * [accountSubscribe](https://solana.com/docs/</docs/rpc/websocket/accountsubscribe>)
      * [accountUnsubscribe](https://solana.com/docs/</docs/rpc/websocket/accountunsubscribe>)
      * [blockSubscribe](https://solana.com/docs/</docs/rpc/websocket/blocksubscribe>)
      * [blockUnsubscribe](https://solana.com/docs/</docs/rpc/websocket/blockunsubscribe>)
      * [logsSubscribe](https://solana.com/docs/</docs/rpc/websocket/logssubscribe>)
      * [logsUnsubscribe](https://solana.com/docs/</docs/rpc/websocket/logsunsubscribe>)
      * [programSubscribe](https://solana.com/docs/</docs/rpc/websocket/programsubscribe>)
      * [programUnsubscribe](https://solana.com/docs/</docs/rpc/websocket/programunsubscribe>)
      * [rootSubscribe](https://solana.com/docs/</docs/rpc/websocket/rootsubscribe>)
      * [rootUnsubscribe](https://solana.com/docs/</docs/rpc/websocket/rootunsubscribe>)
      * [signatureSubscribe](https://solana.com/docs/</docs/rpc/websocket/signaturesubscribe>)
      * [signatureUnsubscribe](https://solana.com/docs/</docs/rpc/websocket/signatureunsubscribe>)
      * [slotSubscribe](https://solana.com/docs/</docs/rpc/websocket/slotsubscribe>)
      * [slotUnsubscribe](https://solana.com/docs/</docs/rpc/websocket/slotunsubscribe>)
      * [slotsUpdatesSubscribe](https://solana.com/docs/</docs/rpc/websocket/slotsupdatessubscribe>)
      * [slotsUpdatesUnsubscribe](https://solana.com/docs/</docs/rpc/websocket/slotsupdatesunsubscribe>)
      * [voteSubscribe](https://solana.com/docs/</docs/rpc/websocket/votesubscribe>)
      * [voteUnsubscribe](https://solana.com/docs/</docs/rpc/websocket/voteunsubscribe>)
    * Deprecated Methods
      * [confirmTransaction](https://solana.com/docs/</docs/rpc/deprecated/confirmtransaction>)
      * [getConfirmedBlock](https://solana.com/docs/</docs/rpc/deprecated/getconfirmedblock>)
      * [getConfirmedBlocks](https://solana.com/docs/</docs/rpc/deprecated/getconfirmedblocks>)
      * [getConfirmedBlocksWithLimit](https://solana.com/docs/</docs/rpc/deprecated/getconfirmedblockswithlimit>)
      * [getConfirmedSignaturesForAddress2](https://solana.com/docs/</docs/rpc/deprecated/getconfirmedsignaturesforaddress2>)
      * [getConfirmedTransaction](https://solana.com/docs/</docs/rpc/deprecated/getconfirmedtransaction>)
      * [getFeeCalculatorForBlockhash](https://solana.com/docs/</docs/rpc/deprecated/getfeecalculatorforblockhash>)
      * [getFeeRateGovernor](https://solana.com/docs/</docs/rpc/deprecated/getfeerategovernor>)
      * [getFees](https://solana.com/docs/</docs/rpc/deprecated/getfees>)
      * [getRecentBlockhash](https://solana.com/docs/</docs/rpc/deprecated/getrecentblockhash>)
      * [getSignatureConfirmation](https://solana.com/docs/</docs/rpc/deprecated/getsignatureconfirmation>)
      * [getSignatureStatus](https://solana.com/docs/</docs/rpc/deprecated/getsignaturestatus>)
      * [getSnapshotSlot](https://solana.com/docs/</docs/rpc/deprecated/getsnapshotslot>)
      * [getStakeActivation](https://solana.com/docs/</docs/rpc/deprecated/getstakeactivation>)


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

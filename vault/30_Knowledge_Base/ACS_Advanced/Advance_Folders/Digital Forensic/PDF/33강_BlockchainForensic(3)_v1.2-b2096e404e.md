---
title: "33강_BlockchainForensic(3)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\33강_BlockchainForensic(3)_v1.2.pdf"
source_size_bytes: 564944
source_modified: 2025-10-18T20:21:50
imported_at: 2026-06-14T14:25:22
tags:
  - acs
  - acs-advanced
  - imported
---

# 33강_BlockchainForensic(3)_v1.2

- Source: [33강_BlockchainForensic(3)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/33%EA%B0%95_BlockchainForensic%283%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Blockchain Forensic (2)
• Why Bitcoin is hard to trace
• CoinJoin and CoinShuffle
• Atomic swaps and coin swaps
33
1

## Page 2

2
01. current page topic
Why Bitcoin is hard to trace01
Why Bitcoin is hard to trace
03
04
05
01
02
Anonymity and pseudonymity
The Bitcoin network provides pseudo-anonymity that doesn't
directly reveal a user's real identity
Challenges of international collaboration
Cryptocurrencies like Bitcoin are used globally and are subject
to laws and regulations in many different countries.
New technologies and protocols evolve
The ecosystem of Bitcoin and other cryptocurrencies is
constantly evolving, with new technologies and protocols
being introduced that make tracking more difficult.
Mixing Services
Allow users to exchange their bitcoins with each other,
making transactions more difficult to trace.
Distributed network structure
Bitcoin is a decentralized network run by many computers
(nodes) distributed around the world with no centralized
authority.

## Page 3

3
01. current page topic
Why Bitcoin is hard to trace01
Privacy coins and dark coins
Privacy Coins
Refers to cryptocurrencies that are primarily focused on
protecting users' transaction history and identity information.
Dark Coins
Sometimes used in a similar sense to privacy coin, but this is
often used in a negative way in the media or among the
general public.
Why Bitcoin is hard to trace

## Page 4

4
01. current page topic
Why Bitcoin is hard to trace01
Privacy Coin
02
03
Protect the privacy of your
transactions with an encryption
technique called zk-SNARKs
(Zero-Knowledge Succinct Non-
Interactive Arguments of
Knowledge)
A feature called PrivateSend allows you to
blend a user's transactions to hide the
source and destination of their
transactions
01
One of the most widely used
cryptocurrencies for privacy, it uses
technologies like Ring Signatures,
Stealth Addresses, and RingCT (Ring-
based Confidential Transactions) to
hide the source, amount, and
recipient of transactions.
Dash
Monero JetCash
Why Bitcoin is hard to trace

## Page 5

5
01. current page topic
Why Bitcoin is hard to trace01
Stealth addresses How it works
Create a disposable address : Stealth address systems have the sender use the recipient's
public key to generate a one-time, unique address for each transaction. This address can only
be accessed by the recipient using their private key.
Ensure anonymity of transactions: In this way, each transaction recorded on the blockchain
has an address that is uniquely identifiable to the recipient, so it's impossible for an outsider
to know who it belongs to. Therefore, the recipient's actual wallet address is not exposed.
Recipient privacy: Recipients can securely transfer funds to their primary wallet for a single-
use address, which is also externally untraceable
Pros
Privacy: Stealth addresses greatly enhance recipient privacy in cryptocurrency transactions.
Since transactions are harder to trace, users can keep their finances and activities more
secure.
Increased security: The use of single-use addresses makes transactions more secure because a
new address is generated for each transaction, making it more difficult for hackers to target
specific addresses.
Cons
Increased complexity: The use of stealth addresses may complicate the processing of
transactions and place additional processing burdens on wallet software or blockchain
networks
Usability issues: The concept and use of stealth addresses can be a bit complicated for the
average user, and requires a user-friendly interface
Why Bitcoin is hard to trace

## Page 6

6
01. current page topic
Why Bitcoin is hard to trace01
Mixing
Mixing, or coin mixing, is a way to protect user privacy by making cryptocurrency
transactions harder to trace. Coin mixing services are used to enhance user anonymity,
especially on publicly traceable blockchain networks like Bitcoin, by mixing coins from
multiple users to further obscure the connection between the origin and destination of
a transaction
How it works
Mixing of many transactions: The user sends their coins to the mixing service and the
service mixes them with many other transactions. As a result, the mixed coins appear to
come from many different sources.
Return to new address: At the end of the mixing process, the service returns the mixed
coins to a new address specified by the user, which usually involves several steps,
making it difficult to trace the original source of the coins.
Purpose and use
Privacy: The main purpose of mixing services is to protect the privacy of users. In a public
blockchain, both sides of a transaction can be linked because every transaction is
recorded and can be viewed by anyone.
Increase security: By hiding the origin and destination of transactions, it makes it more
difficult for hackers to target specific wallets or individuals.
Why Bitcoin is hard to trace

## Page 7

7
01. current page topic
CoinJoin and CoinShuffle02
Coin Join
CoinJoin is one of the methods used to protect user privacy in cryptocurrency transactions
such as Bitcoin. CoinJoin is a technique that combines transactions from multiple users into
one large transaction, making it more difficult to link the origin and destination of individual
transactions. This method increases user anonymity by complicating the tracking of
transactions and the identification of transaction participants.
Pros
Privacy: CoinJoin obscures the link between individual transactions,
making it harder to trace and identify transactions, which greatly contributes to user privacy.
No need for centralized services: Since coinjoining is done through direct collaboration
between participants, it can reduce the need for centralized mixing services
Considerations
Finding participants: Executing a coin join requires collaboration with other participants;
sometimes these participants can be difficult to find
Transaction costs: The more complex the transaction, the more transaction fees you may incur
Execution complexity: Technical understanding is required to execute a coin join,
execution can be complex as all participants must sign the transaction

## Page 8

8
01. current page topic
CoinJoin and CoinShuffle02
Users signal to a service or platform that they
want to do a coinjoin transaction
Recruit participants
Trade inputs from multiple users are combined
into a single trade
Combine transaction inputs
Each participant provides a new address
 where they will receive their coins
Provide an output address
Requires a signature for all inputs in the transaction
Signing transactions
Completed transactions are sent to the Bitcoin
network and recorded on the blockchain
Sending transactions to the blockchain
1
2
3
4
5
Key ways to use CoinJoin
CoinJoin and CoinShuffle

## Page 9

9
01. current page topic
CoinJoin and CoinShuffle02
Centralized Coin Join Service
Centrally coordinate the coinjoin process, combining transactions from multiple participants into one,
further blurring the connection between the source and destination of each transaction.
Service feesRecruit
participants
Combine
transactions
Generate an
output address
CoinJoin and CoinShuffle

## Page 10

10
01. current page topic
CoinJoin and CoinShuffle02
Decentralized CoinJoin Protocol
An alternative to centralized services, providing a way for users to collaborate with each other to
make Bitcoin transactions harder to trace and more private.
Broadcasting
transactions
Distributed
signatures
Recruiting
volunteers
Combine
transactions
Generate an output
address
CoinJoin and CoinShuffle

## Page 11

11
01. current page topic
CoinJoin and CoinShuffle02
Coin Shuffle and Coin Shuffle++
A
B
Coin Shuffle
 A decentralized transaction
mixing protocol in which users
directly participate. The protocol
exchanges information with other
participants about new addresses
created by each participant, while
ensuring that no one can directly
link an individual transaction to
the identity of another participant.
Coinshuffle ++
A protocol that improves upon Coin
Shuffle, providing additional security
mechanisms and efficiencies. The
protocol introduces a more efficient way
to exchange messages between
participants, reducing the
communication overhead of the mixing
process and speeding up the process.
A
B
CoinJoin and CoinShuffle

## Page 12

12
01. current page topic
CoinJoin and CoinShuffle02
Coinshuffle
Coin Shuffle
A type of protocol for increasing the anonymity of cryptocurrency transactions.
Transaction creation
and name
Recruit participants Mixing addresses Encrypted
communication
CoinJoin and CoinShuffle

## Page 13

13
01. current page topic
Atomic swaps and coin swaps03
Coin Swap
01 Add your texts here
01
Exchanging coins via
exchanges
02 Decentralized coin swaps via DeFi platforms
03 Coin swap for token migration
04 Atomic Swaps

## Page 14

14
01. current page topic
Atomic swaps and coin swaps03
Coin migration
The process of transferring a specific cryptocurrency token from one blockchain network to another.
Deactivate an existing
token
Announcements and
preparation Create a new token Token exchange
Atomic swaps and coin swaps

## Page 15

15
01. current page topic
Atomic swaps and coin swaps03
Decentralized finance platform
An ecosystem of financial services built using blockchain technology to replace or complement
traditional financial systems.
■ Loans
■ Exchange
■ Staking
■ Asset Management
■ Insurance
➢ Examples of services offered by DeFi platforms
■ Unauthorized
■ Transparency
■ Programmability
■ Interoperability
➢ Key features of DeFi platforms
Atomic swaps and coin swaps

## Page 16

16
01. current page topic
Atomic swaps and coin swaps03
Atomic
Atomic in Computer Science
In computer science, "atomic" means that a
task is executed "all or nothing" with no
intermediate steps
 In other words, the task is considered either
fully completed or never started
 This is an important property that can be
applied to a wide variety of computing tasks
 including database transactions,
computation in a multithreading
environment, etc.
Expanded implications in the crypto world
In the cryptocurrency world, "atomic" can be
used to refer to a property that guarantees
that a transaction or swap is executed in full
or not at all In addition to atomic swaps, the
term can be applied in a variety of contexts
related to smart contracts, transaction
processing, or the security mechanisms of
cryptocurrencies For example, in a smart
contract,
 atomic operations guarantee that the
contract is fully fulfilled or remains
unchanged.
Atomic swaps and coin swaps

## Page 17

17
01. current page topic
Atomic swaps and coin swaps03
Atomic Swaps
Decentralized trading technology that allows cryptocurrencies based on different blockchains to be
exchanged directly without a centralized exchange or third party.
Transaction
Completed
Revealing and
unlocking passwords
Create a smart
contract
Share password
hashes
Locking with
password hashes
Atomic swaps and coin swaps

## Page 18

18
01. current page topic
Atomic swaps and coin swaps03
Blockchain bridges (cross-chain bridges)
Technology that enables the transfer of assets, data, or smart contract commands between different
blockchain networks.
UnlockingLocking Minting
Oracle RelayersSmart contracts
Atomic swaps and coin swaps

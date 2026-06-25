---
title: "31강_BlockchainForensic(1)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\31강_BlockchainForensic(1)_v1.2.pdf"
source_size_bytes: 725610
source_modified: 2025-10-18T20:18:10
imported_at: 2026-06-14T14:25:20
tags:
  - acs
  - acs-advanced
  - imported
---

# 31강_BlockchainForensic(1)_v1.2

- Source: [31강_BlockchainForensic(1)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/31%EA%B0%95_BlockchainForensic%281%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Blockchain Forensic (1)
• What is Blockchain
• Blockchain Address
• Transaction
• Token
31
1

## Page 2

2
01. current page topic
What is Blockchain01
How blockchain technology came to be
01
02
03
Computer failures affect the entire system
Financial burden of security
Existence of a single point of failure

## Page 3

3
01. current page topic
What is Blockchain01
Blockchain
Peer-to-peer (P2P)
A distributed network architecture where each participant can
act as both client and server at the same time
What is Blockchain
Blockchain is a revolutionary technology designed around the
core principle of decentralization.
It allows data to be reliable and stable without the need for a
centralized authority or intermediary.
Each "block" in a blockchain contains data from multiple
transactions, which are chained together in chronological order.
In a peer-to-peer based blockchain system, all nodes validate the
blocks containing transaction data, and when a new block is
added, copies are distributed and stored on all nodes
participating in the network. All transactions that occur during
this process are encrypted and recorded, and once added to the
blockchain, the data cannot be altered.

## Page 4

4
01. current page topic
What is Blockchain01
Problems with Blockchain
Scaling Solution
Refers to technical methods or improvements to increase the processing capacity of a blockchain network, speed up transactions, and reduce fees.
01
Blockchain's processing speed is relatively
slow compared to centralized systems
02
The problem with blockchain's data error rate
What is Blockchain

## Page 5

5
01. current page topic
What is Blockchain01
Blockchain by Operating Entity
Public blockchains: A fully decentralized blockchain that anyone can join.
Any individual or organization that wants to participate in such a network
can confirm, send, and receive transactions without special permission, and
even participate in the network's consensus process. The most well-known
examples of public blockchains are Bitcoin and Ethereum.
Private blockchain: A closed or private blockchain is a network with
limited participation. It is run by a specific organization or group and
requires an invitation or permission to become a participant. It is typically
optimized for the internal processes of a specific business or organization
and can provide more efficient transaction processing speeds and improved
privacy controls. For example, used for things like supply chain
management, transferring funds, and processing business-to-business
transactions.
What is Blockchain

## Page 6

6
01. current page topic
What is Blockchain01
Cryptocurrencies and cryptoassets
Categorization Definition Use cases Regulation By Value
Cryptocurrency
A type of digital or
virtual currency that
uses cryptography
for security.
Use for trading and
investing
Often subject to
financial regulation
Value is determined
by market demand,
scarcity, and use
within the economy
Virtual Assets
A digital
representation of
value that can be
traded or
transferred and
used for payments
or investments.
Includes
cryptocurrencies as
well as other types
of digital assets
such as utility
tokens or securities
tokens
It is regulated by
local laws and
varies widely.
Value can be based
on underlying
assets, rights, or
utilities provided
What is Blockchain

## Page 7

7
01. current page topic
What is Blockchain01
Bitcoin and altcoins
Lateral Bitcoin Altcoins
Founding The first cryptocurrency, founded in
2009
Emerged after Bitcoin, includes many
cryptocurrencies
Market
capitalization Largest market capitalization Typically smaller market capitalization
Dominance Most widely recognized and used Vastly vary in market share
Techniques
Use of blockchain technology,
specifically the Proof of Work
algorithm.
Use multiple consensus mechanisms,
including different technologies
Purpose Initial purpose as a decentralized
digital currency
Serves a variety of purposes, from
digital currency to asset tokenization
Diversity One major blockchain Include a variety of blockchains and
tokens
What is Blockchain

## Page 8

8
01. current page topic
Blockchain Address02
Address type Description. Features
P2PKH
(Pay to Public Key Hash)
Starts with '1'
 A way to pay for a hash of a public key
 The original form of a Bitcoin address
The first version of Bitcoin addresses,
providing basic functionality for
sending and receiving Bitcoin
P2SH
(Pay to Script Hash)
Starts with '3'
 Allows users to pay with a script hash (address)
Enables more complex transaction types,
increasing security and flexibility
Supports complex transactions, e.g.
multi-signature transactions,
increasing security and flexibility
over P2PKH
Bech32
Starts with "bc1"
 Used for SegWit (Segregated Witness)
transactions reduces transaction fees and
provides benefits such as efficiency
Lower transaction cost,
 better error detection, and supports
native SegWit transactions
Types of Blockchain Addresses

## Page 9

9
01. current page topic
Blockchain Address02
Bitcoin exchanges
Exchange wallet address
Managed by the exchange.
Users do not have access to private
keys, and the exchange manages the
storage, sending, and receiving of
assets on behalf of the user.
Primarily focused on trading and
storage of cryptocurrency, and
designed to make it easy for users to
trade within the exchange.
Users are dependent on the exchange's
security levels and policies
Personal wallet address
Managed directly by the user.
You hold the private keys to this wallet
and have full control over your assets.
A private wallet provides a secure place
to store cryptocurrency and a private
means to transfer assets whenever you
want.
The security of a private wallet depends
on how well you manage it.
With strong security practices, private
wallets can be more secure than
exchange wallets.
Blockchain Address

## Page 10

10
01. current page topic
Blockchain Address02
Searchable information using the address
Sender and recipient addresses
Balance
Transaction history
Trading volume
Transaction fees
Block information
Blockchain Address

## Page 11

11
01. current page topic
Blockchain Address02
Identifying wallet addresses with address lookups
Blockchain Analytics Services
Blockchain analytics companies such as
Chainalysis, Elliptic, and others use
advanced analytics tools and vast databases
to provide a variety of information,
including whether a particular address is
associated with an exchange
Public information
Some exchanges disclose their
wallet addresses for security,
regulatory compliance, or
transparency reasons
Transaction frequency and size
Exchange wallet addresses typically
handle a very high frequency and
volume of transactions.
Clustering techniques
Blockchain analytics tools use clustering
techniques to analyze transaction patterns
between multiple addresses, which can
infer whether a particular address is
associated with an exchange.
Multiple inputs and outputs
Exchanges create transactions with
multiple inputs and outputs to process
your transactions.
Blockchain Address

## Page 12

12
01. current page topic
Blockchain Address02
Bitcoin and altcoins
A digital tool for storing Bitcoin or other cryptocurrencies.
Unlike physical wallets that store real money, wallets do not directly
store cryptocurrency, but rather store the private keys and public keys
needed to transact cryptocurrency.
Bitcoin wallets
A unique identifier used as a destination for receiving cryptocurrency.
Consists of a series of numbers and letters, which allows anyone to
send bitcoin to a specific wallet. The address is generated from a
hashed version of the public key, which is usually only used once for
added security.
Bitcoin address
Create Relationships
Proof of ownership
Management
Blockchain Address

## Page 13

13
01. current page topic
Transaction03
Components of a transaction
Version
Indicates the format of the
transaction, specifying the
specific rules or protocol version
that the transaction uses.
Outputs
Amount
Locking Script
Script PubKey
Transaction Size and Fees
The size of a transaction,
measured in bytes, depends on
the amount of data it contains
Inputs
See previous transaction output
Unlocking Script
ScriptSig
Locktime
Optional field to specify that the
transaction should not be processed
before a certain point in time.
Signature
The signature embedded in the
transaction input proves its validity by
signing the transaction with the
sender's private key.
01 02
03 04
05 06

## Page 14

Lock
time
Example
: 0
Version
Example
: 1
14
01. current page topic
Transaction03
Components of a transaction
When the transaction is
Alice sending 0.5 BTC to BoB
Inputs
 See previous
transaction output:
referring to the
output of the previous
transaction that Alice
uses to send the 1
BTC she received
earlier
First output (sending 0.5 BTC to Bob):
 Value: 0.5 BTC
 Locking Script /
 Script PubKey:
Script to specify Bob's bitcoin address
Second output
 (change, sent back to Alice):
 Value: 0.4999 BTC (0.0001 BTC paid as
transaction fee)
 Lock script: a script that specifies Alice's other
address
Transaction

## Page 15

15
01. current page topic
Transaction03
How transactions work
Create a transaction
Signing transactions
Transaction propagation
Transaction validation
Include transactions in blocks
Adding blocks to the blockchain
Finalizing a transaction
Transaction

## Page 16

16
01. current page topic
Transaction03
What you can learn from transaction analysis
Track the flow
of Bitcoin
Understand
the type of
transaction
and
complexity
Market activity
and
Liquidity assessment
Check transaction amounts and fees
Transfer amount: 0.5 BTC sent to
BoBTransaction feeAmount sent - minus the
change returned to Alice, paid as transaction
fee
Identify the sender and receiver
Sender: The bitcoin held by Alice in the
output of the previous transaction that appears in
the input part of the transaction.
Recipient: BoB's address appears in the
output part of the transaction.
Transaction
When the transaction is
Alice sending 0.5 BTC to BoB

## Page 17

17
01. current page topic
Token04
Tshark
Token
A digital asset or digital representation.
Used to represent value, assets, certain rights, or utilities on a particular blockchain network.
Utility Tokens
Provides the right to use certain services or
features on a blockchain-based platform
Security Tokens
Digital representations of traditional financial assets
(e.g., stocks, bonds, real estate)

## Page 18

18
01. current page topic
Token04
ERC
 Ethereum Request for Comments
ERC-20 (Utility Token Standard)
Defines a standard interface for tokens used on the Ethereum network. The standard specifies basic token
behavior, such as sending tokens, tracking minting, and checking a user's token balance ERC-20 tokens are
interchangeable, which means that all tokens have the same value and are interchangeable.
Transfer(address to, uint256 value):
Transfers a token to another address.
balanceOf(address owner):
Retrieves the balance of tokens at a specific address.
approve(address spender, uint256 value):
Allows another address to send a certain amount of tokens on its behalf.
ERC-721 (Non-Fungible Token, NFT standard)
A standard for non-fungible tokens (NFTs) where each token has unique properties and can be distinguished
from other tokens. This standard is used to represent unique digital assets such as digital art, collectibles, and
game items.
transferFrom(address from, address to, uint256 tokenId): transfers a specific token to another address.
ownerOf(uint256 tokenId): Retrieves the owner of a specific token.
Approve(address to, uint256 tokenId): Allows another address to send a specific token on its behalf.
Refers to standards proposed by the Ethereum community
Token

## Page 19

19
01. current page topic
Token04
Where tokens are used
Voting rights and governance
Rewards and incentives
Funding
Platform access and utilities
Representative assets
Digital currency
Token
Non-crypto token NTF

## Page 20

20
01. current page topic
Token04
What you can learn by analyzing token transactions
Transaction amount Complexity and type of transaction
Transaction hash and block information Calling smart contracts
Sender and sender address Analyze network activity and trends
Gas costs and transaction fees
Token

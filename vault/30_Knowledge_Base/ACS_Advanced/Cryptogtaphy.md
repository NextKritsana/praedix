---
title: "Cryptogtaphy"
type: acs-course-pdf
course: "ACS Advanced"
source_pdf: "E:\\ProJect\\ACS File\\Cryptogtaphy.pdf"
source_size_bytes: 5052719
source_modified: 2025-08-22T20:09:19
imported_at: 2026-06-14T14:14:50
pages: 238
tags:
  - acs
  - imported-pdf
  - cybersecurity
---

# Cryptogtaphy

- Source PDF: `E:\ProJect\ACS File\Cryptogtaphy.pdf`
- Pages: 238
- Pages with extracted text: 238

> Imported from PDF for Obsidian search and review. Verify formatting against the original PDF when precision matters.

## Page 1

Cryptography
ACS Education 8th

## Page 2

Index
• Cryptography overview
• Symmetric key Encryption
• Public-key Encryption
• Integrity
• Lab

## Page 3

Cryptography
overview
01
• Overview
• Fundamental theories of
Cryptography
• Mathematical Basics for
Understanding modern
Cryptography
• Security of Cryptographic
algorithms

## Page 4

4
Overview
⚫ Cryptology
Academically speaking, cryptography includes cryptography, which creates various encryption
and decryption methods, and cryptanalysis, which interprets and analyzes them.
Cryptos
(κρψπτοσ)
secret
Logos
(λογοσ)
discipline
(science)
+
Cryptography
 Cryptanalysis
Research cryptographic
algorithms to protect
plaintext.
Study the encryption
process and ciphertext in
order to decrypt plaintext.

## Page 5

5
Overview
⚫ Discrete mathematics
- Means performing operations on numbers that are discrete rather than continuous.
- Excludes subjects such as calculus and Euclidean geometry, which deal with continuity in
mathematics.
- Mostly works with integers.
- The development of digital computers has
stimulated the study of discrete mathematics.
• Computer algorithms, programming languages,
cryptography, software fields, etc.
Discrete means scattered apart. In the same vein, discrete mathematics means that the values
are scattered rather than continuous.

## Page 6

6
Fundamental theories of cryptography
⚫ Cryptography
- References : American National Standards Institute (ANSI) X9.31-1998*
US National Institute of Standards and Technology (NIST) SP 800-2-1991**
• "The discipline which embodies principles, means and methods"* "for the transformation
of ordinary text (plaintext) into coded form (ciphertext) by encryption, and transformation
of ciphertext into plaintext by decryption."**
Academically speaking, cryptography includes cryptography, which creates various encryption
and decryption methods, and cryptanalysis, which interprets and analyzes them.
Introduction to cryptography
Converting plaintext to unintelligible
ciphertext by encryption
Converting ciphertext into intelligible
plaintext by decryption
Discipline or science that deals with principles, means and methods
Source : https://csrc.nist.rip/projects/cryptographic-module-validation-program

## Page 7

7
Technologies that provide information security services
Fundamental theories of cryptography
⚫ Information security and cryptography
⚫ Modern cryptography extends to the study of various problems related to secret
communication and their solutions, encompassing the field of information security.
Academically speaking, cryptography includes cryptography, which creates various encryption
and decryption methods, and cryptanalysis, which interprets and analyzes them.
Introduction to cryptography
Confidentiality Integrity Authentication

## Page 8

8
Fundamental theories of cryptography
⚫ Encryption flows
Traditionally, cryptography consists of transforming a human-readable plaintext into an
unrecognizable ciphertext using a specific method, and then transforming it back into a human-
readable plaintext.
Understanding cryptographic terminology
Plaintext Plaintext
Ciphertext
Encrypt
Key
 Key
Plaintext (P) - plain,
unencrypted data
or messages.
Ciphertext (C) - an
encrypted form of
data or message.
Encryption (E) - the
process of turning
plaintext into
ciphertext
Decryption (D) - a reverse
operation of encryption,
restoring a ciphertext to its
original plaintext.
Encryption key (Ke ) - a
parameter used in the
encryption process
Encryption key (Kd ) - a
parameter used in the
decryption process
Cryptographic algorithm -
a mathematical function
(process) used for
encryption and decryption.

## Page 9

9
Fundamental theories of cryptography
⚫ Other cryptography terms
- Cryptanalysis - the process of obtaining the original plaintext or key without having the key.
- Cryptosystem - a set of processes for securing information, including the encryption and
decryption processes, the encryption and decryption keys used, and key management.
- Attacker - a third party who attempts to decrypt the ciphertext into plaintext.
- Entity - a person who can send, receive, and modify information.
Traditionally, cryptography consists of transforming a human-readable plaintext into an
unrecognizable ciphertext using a specific method, and then transforming it back into a human-
readable plaintext.
Understanding cryptographic terminology

## Page 10

10
Fundamental theories of cryptography
⚫ Cryptographic principles
- Classic cryptography
• Transposition cipher
• Substitution cipher - simple substitution cipher
- Modern cryptography
• Substitution cipher - polyalphabetic substitution cipher
- Contemporary cryptography
• Confusion and diffusion
One way to categorize cryptographic techniques is to group the four cryptographic principles
into three eras.
Categorizing cryptographic techniques
Cryptographic
algorithm
Substitution Transposition
Confusion Diffusion
Number of keys used
Symmetric key Public key
Plaintext processing
Block Stream

## Page 11

11
Fundamental theories of cryptography
⚫ Characters used in discussions of cryptography (how it's represented)
- Alice and Bob
• Alice : the person sending the message
• Bob : the person receiving the message.
- Eve and Mallory
• Eve : eavesdropper
• Mallory : malicious attacker
- Trent and Victor
• Trent : trusted arbitrator
• Victor : verifier
Fundamental concepts in such difficult cryptography can be understood in a storytelling way,
using fictional characters. They are known as Alice and Bob and were first used in 1978 in the
paper "A method for obtaining digital signatures and public-key cryptosystems."
Basic cryptography concepts
Alice
Bob
Eve
Mallory
Trent
Victor

## Page 12

12
Fundamental theories of cryptography
Basic cryptography concepts
Alice
Bob
Alice
Bob
Eve
Eavesdropping
Alice
Bob
Mallory
Plaintext forwarding
Forging and tampering
Fundamental concepts in such difficult cryptography can be understood in a storytelling way,
using fictional characters. They are known as Alice and Bob and were first used in 1978 in the
paper "A method for obtaining digital signatures and public-key cryptosystems."

## Page 13

13
Fundamental theories of cryptography
Basic cryptography concepts
Ciphertext
Plaintext
 Encrypt
Alice
Bob
Eve
Decrypt
Ciphertext
 Plaintext
Ciphertext
Mallory
Fundamental concepts in such difficult cryptography can be understood in a storytelling way,
using fictional characters. They are known as Alice and Bob and were first used in 1978 in the
paper "A method for obtaining digital signatures and public-key cryptosystems."

## Page 14

14
Fundamental theories of cryptography
⚫ Separate cryptographic algorithms and keys
- Cryptographic algorithms
• Using a new algorithm each time results in poor performance.
• Designed to use one algorithm repeatedly
- Keys
• Designed to use different keys for different users
• Build a more secure encryption system
When implementing cryptographic algorithms in information security, cryptographic algorithms
and key management are the most important aspects.
Basic cryptography concepts
Plaintext Plaintext
Ciphertext
Encrypt
Key
 Key
Key

## Page 15

15
Fundamental theories of cryptography
⚫ Prohibit the use of secret cryptographic algorithms
- Implementing the company's own cryptographic algorithms is a risky practice.
• Keeping a cryptographic algorithm secret can only be secure to the extent that it is not
exposed to create a larger problem.
• This is called "security by obscurity."
⚫ Encrypting weak cryptography is risky.
- This is the feel of security that the word "cryptography"
gives off, which is problematic.
⚫ All encrypted cryptography can eventually be broken.
- Should change your cryptography every 6 months
under the Korean Personal Information Protection Act.
- The Guide on Critical Information Infrastructure Protection
in South Korea recommends changing it every 3 months.
When implementing cryptographic algorithms in information security, cryptographic algorithms
and key management are the most important aspects.
Cryptography and security common sense

## Page 16

16
Fundamental theories of cryptography
⚫ Classification by number of keys used for encryption and decryption
- Secret Key Cryptography (SKC)
• Use a single key for both encryption and decryption
• Also called symmetric encryption
• Used mainly for privacy and confidentiality
- Public Key Cryptography (PKC)
• Separate encryption and decryption keys
• Also called asymmetric encryption
• Used mainly for authentication, non-repudiation, and key exchange
- Hash Function
• Use mathematical transformations for irreversible encryption
• Used mainly for integrity verification (digital fingerprinting)
The main categories of cryptographic algorithms in use in the field of information security are
the following.
Classification of cryptographic algorithms
DES AES
RSA PKCS
MD5 SHA1

## Page 17

17
Fundamental theories of cryptography
⚫ Classic ciphers were developed based on existing languages.
- Traditional methods of encrypting messages
⚫ They were designed to be simple.
- Some features of plaintext appear in ciphertext.
- Cryptographic algorithms are highly vulnerable because ciphertext-only attacks and known-
plaintext attacks are similar in type.
- Not currently used by cryptographers using computers
⚫ They are still useful in some way.
- Classic ciphers are not used alone, but are used as one step or in combination with another
method in modern cryptosystems.
- The basic principles of classical cryptosystems are still used in modern cryptosystems,
greatly aiding cryptographic research.
Classical cryptography is based on ciphers that were used in the past but are rarely used today.
Its focus was mainly on languages.
Concepts of classical cryptography

## Page 18

18
Fundamental theories of cryptography
⚫ Composition of classic cipher
- Transposition
• Method of creating ciphertext by changing the position of each character
- Substitution (simple substitution)
• Method of creating ciphertext by substituting different characters according to certain
predetermined criteria.
- Number of keys used
• Symmetric keys
- Plaintext processing
• In blocks
Classic cryptography is based on ciphers that were used in the past but are rarely used today. Its
focus was mainly on languages.
Concepts of classical cryptography

## Page 19

19
Fundamental theories of cryptography
⚫ Modern ciphers were developed based on existing languages as well.
- Traditional methods for encrypting messages
- Have more complex forms comparing with classic ciphers
⚫ Modern cryptography began to be the subject of proofs in journal articles.
- William F. Friedman, 1920, The Index of Coincidence and Its Applications in Cryptography.
• Index of coincidence is a probabilistic method of calculating how closely two messages
match (part of cryptanalysis)
• It helped deciphering the Japanese PURPLE (Type B Cipher Machine) code in World War II.
- Claude E. Shannon, 1949, Communication Theory of Secrecy Systems.
• Prove the security of cryptographic schemes, presenting theories of confusion and
diffusion.
Modern cryptography evolved from simple ancient ciphers as mathematics advanced. Multiple
combinatorial ciphers were developed into machine ciphers during World War II.
Concepts of modern cryptography

## Page 20

20
Fundamental theories of cryptography
⚫ Applied advanced mathematical theory
⚫ The rise of civilian cryptography
- Civilian use refers to the transfer of technology, products, etc. from military to civilian use.
⚫ Using computer bits
- As computing power increased, so did the difficulty
of cryptography.
- Cryptography began to have a close relationship with
the computer information security.
• Bitwise operations
Contemporary cryptography was advanced by Stanford Univ. and MIT. In 1976, W. Diffie and M.
E. Hellman of Stanford Univ. published the concept of public-key cryptography in their paper,
New Directions in Cryptography. In 1978, R. Rivest, A. Shamir, and L. Adleman of MIT developed
the RSA public-key cryptosystem based on the prime factorization method.
Contemporary cryptography
Safety
Efficiency
IntegrityAuthentication
Non-
repudiation
Features

## Page 21

21
Fundamental theories of cryptography
⚫ Classification of contemporary cryptography by technology
Contemporary cryptography was advanced by Stanford Univ. and MIT. In 1976, W. Diffie and M.
E. Hellman of Stanford Univ. published the concept of public-key cryptography in their paper,
New Directions in Cryptography. In 1978, R. Rivest, A. Shamir, and L. Adleman of MIT developed
the RSA public-key cryptosystem based on the prime factorization method.
Contemporary cryptography
Cryptosystem
Unidirectional
Bidirectional
Symmetric keys
Asymmetric keys
Stream cipher
Block cipher
Synchronous
Asynchronous
Feistel
SPN
Prime factorisation
Discrete algebra
RSA
Rabin
ElGamal
DSA
ECC
Unkeyed
Keyed
MDC
MAC

## Page 22

22
Fundamental theories of cryptography
⚫ Classification of contemporary cryptography by functionality
Contemporary cryptography was advanced by Stanford Univ. and MIT. In 1976, W. Diffie and M.
E. Hellman of Stanford Univ. published the concept of public-key cryptography in their paper,
New Directions in Cryptography. In 1978, R. Rivest, A. Shamir, and L. Adleman of MIT developed
the RSA public-key cryptosystem based on the prime factorization method.
Contemporary cryptography
Confidentiality Integrity Authentication Non-repudiation
Encryption Data integrity Message
authentication Identification Digital signature
Symmetric
key
(stream)
Symmetric
key
(block)
Asymmetric
key
Hash
(unkeyed)
Hash
(keyed)
Asymmetric
key
(signature)
Symmetric
key
(signature)
Random
number
generator
Efficient
implementation
Patents and
standards Key exchange protocols Key management Public key security
Public key
parameters

## Page 23

23
Mathematical Basics for Understanding modern
Cryptography
⚫ Proposition
- A statement or mathematical expression that can be clearly determined as either true or
false.
⚫ Truth value
- The value that a proposition represents as true or false
⚫ Examples
- The sum of the interior angles of a triangle is 360 degrees.
• The sum of the interior angles of a triangle is 180 degrees, so the truth value is false (𝐹).
- 9 is a multiple of 3.
• The truth value is true (𝑇).
- 𝑥 is an integer, then if 𝑥 + 1 = 5 , 𝑥 is equal to 4 .
• The truth value is true (𝑇).
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Propositions

## Page 24

24
Mathematical Basics for Understanding modern
Cryptography
⚫ Negation
- That which negates a proposition
- Denoted by  ¬ 𝑃, ~ 𝑃,  or ! 𝑃
• Also called a unary operator because it operates on a single term.
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Negation
𝑃 ~𝑃
𝑇 𝐹
𝐹 𝑇

## Page 25

25
Mathematical Basics for Understanding modern
Cryptography
⚫ Conjunction
- If the statements 𝑃 and 𝑄 are propositions, 𝑃 𝐴𝑁𝐷 𝑄
- Denoted by 𝑃 ∧ 𝑄
• Can also be written as 𝑃 𝐴𝑁𝐷 𝑄 or 𝑃 & 𝑄
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Conjunction
𝑃 𝑄 𝑃 𝐴𝑁𝐷 𝑄
𝑇 𝑇 𝑇
𝑇 𝐹 𝐹
𝐹 𝑇 𝐹
𝐹 𝐹 𝐹

## Page 26

26
Mathematical Basics for Understanding modern
Cryptography
⚫ Disjunction
- If the statements 𝑃 and 𝑄 are propositions, 𝑃 𝐴𝑁𝐷 𝑄
- Denoted by 𝑃 ∨ 𝑄
• Can also be written as 𝑃 𝑂𝑅 𝑄
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Disjunction
𝑃 𝑄 𝑃 𝑂𝑅 𝑄
𝑇 𝑇 𝑇
𝑇 𝐹 𝑇
𝐹 𝑇 𝑇
𝐹 𝐹 𝐹

## Page 27

27
Mathematical Basics for Understanding modern
Cryptography
⚫ Exclusive-or
- If the statements 𝑃 and 𝑄 are propositions, 𝑃 𝑒𝑥𝑐𝑙𝑢𝑠𝑖𝑣𝑒− 𝑜𝑟 𝑄
- Denoted by 𝑃 ⊕ 𝑄
• Can also be written as 𝑃 𝑋𝑂𝑅 𝑄
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Exclusive-or
𝑃 𝑄 𝑃 𝑋𝑂𝑅 𝑄
𝑇 𝑇 𝐹
𝑇 𝐹 𝑇
𝐹 𝑇 𝑇
𝐹 𝐹 𝐹

## Page 28

28
Mathematical Basics for Understanding modern
Cryptography
⚫ Implication
- If the statements 𝑃 and 𝑄 are propositions, 𝑃 𝑖𝑚𝑝𝑙𝑖𝑒𝑠𝑄
• A proposition where 𝑃 is a cause and 𝑄 is an effect
- Denoted by 𝑃 → 𝑄
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Implication
𝑃 𝑄 𝑃 → 𝑄
𝑇 𝑇 𝑇
𝑇 𝐹 𝐹
𝐹 𝑇 𝑇
𝐹 𝐹 𝑇

## Page 29

29
Mathematical Basics for Understanding modern
Cryptography
⚫ Biconditional
- If the statements 𝑃 and 𝑄 are propositions, 𝑃 𝑖𝑓 𝑎𝑛𝑑 𝑜𝑛𝑙𝑦𝑖𝑓 𝑄
• A proposition where both 𝑃 and 𝑄 are causes as well as effects
- Denoted by 𝑃
 𝑄
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Biconditional
𝑃 𝑄 𝑃
 𝑄
𝑇 𝑇 𝑇
𝑇 𝐹 𝐹
𝐹 𝑇 𝐹
𝐹 𝐹 𝑇

## Page 30

30
Mathematical Basics for Understanding modern
Cryptography
⚫ Converse
- For two propositions 𝑃 and 𝑄, if 𝑃 → 𝑄, then 𝑄 → 𝑃
⚫ Inverse
- For two propositions 𝑃 and 𝑄, if 𝑃 → 𝑄, then ~𝑃 → ~𝑄
⚫ Contraposition
- For two propositions 𝑃 and 𝑄, if 𝑃 → 𝑄, then ~𝑄 → ~𝑃
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Converse, inverse, and contraposition
𝑃 𝑄 𝑃 → 𝑄 𝑄 → 𝑃
(𝒄𝒐𝒏𝒗𝒆𝒓𝒔𝒆)
~𝑃 → ~𝑄
(𝑖𝑛𝑣𝑒𝑟𝑠𝑒)
~𝑃 → ~𝑄
(𝑐𝑜𝑛𝑡𝑟𝑎𝑝𝑜𝑠𝑖𝑡𝑖𝑜𝑛)
𝑇 𝑇 𝑇 𝑇 𝑇 𝑇
𝑇 𝐹 𝐹 𝑇 𝑇 𝐹
𝐹 𝑇 𝑇 𝐹 𝐹 𝑇
𝐹 𝐹 𝑇 𝑇 𝑇 𝑇

## Page 31

31
Mathematical Basics for Understanding modern
Cryptography
⚫ Tautology
- A proposition whose compound proposition is always true, regardless of the truth value of
each proposition.
⚫ Contradiction
- A proposition whose compound proposition is always false, regardless of the truth value of
each proposition.
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Tautology and contradiction

## Page 32

32
Mathematical Basics for Understanding modern
Cryptography
⚫ Logical equivalence
- When different compound propositions have the same truth value
- Denoted by the symbol  or the symbol ⇔
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Logical equivalence
𝑝 ∧ 𝑇 ≡ 𝑝 𝑝 ∨ 𝐹 ≡ 𝑝 Identity laws
𝑝 ∧ 𝐹 ≡ 𝐹 𝑝 ∨ 𝑇 ≡ 𝑇 Domination laws
𝑝 ∧ ￢𝑝 ≡ 𝐹 𝑝 ∨ ￢𝑝 ≡ 𝑇 Negation laws
￢(￢𝑝) ≡ 𝑝 Double negation law
𝑝 ∧ 𝑝 ≡ 𝑝 𝑝 ∨ 𝑝 ≡ 𝑝 Idempotent laws
𝑝 ∧ 𝑞 ≡ 𝑞 ∧ 𝑝 𝑝 ∨ 𝑞 ≡ 𝑞 ∨ 𝑝 Commutative laws
(𝑝 ∧ 𝑞) ∧ 𝑟 ≡ 𝑝 ∧ (𝑞 ∧ 𝑟) (𝑝 ∨ 𝑞) ∨ 𝑟 ≡ 𝑝 ∨ (𝑞 ∨ 𝑟) Associative laws
𝑝 ∨ (𝑞 ∧ 𝑟) ≡ (𝑝 ∨ 𝑞) ∧ (𝑝 ∨ 𝑟) 𝑝 ∧ (𝑞 ∨ 𝑟) ≡ (𝑝 ∧ 𝑞) ∨ (𝑝 ∧ 𝑟) Distributive laws

## Page 33

33
Mathematical Basics for Understanding modern
Cryptography
⚫ Logical equivalence
- When different compound propositions have the same truth value
- Denoted by the symbol 
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Logical equivalence
￢(𝑝 ∧ 𝑞) ≡ ￢𝑝 ∨ ￢𝑞 ￢(𝑝 ∨ 𝑞) ≡ ￢𝑝 ∧ ￢𝑞 De Morgan’s law
𝑝 ∧ (𝑝 ∨ 𝑞) ≡ 𝑝 𝑝 ∨ (𝑝 ∧ 𝑞) ≡ 𝑝 Absorption laws
𝑝 → 𝑞 ≡ ￢𝑝 ∨ 𝑞 Implication law
𝑝 → 𝑞 ≡ ￢𝑝 → ￢𝑞 Contraposition law
𝑝 → 𝑞 ≡ (𝑝 ∧ ￢𝑞) → 𝐹 Reductio ad absurdum law

## Page 34

34
Mathematical Basics for Understanding modern
Cryptography
⚫ Quantifier
- Refers to words that indicate quantity in a statement
• Examples
▪ Some, at least one
- Universe of discourse
• Specify a certain scope to clarify a sentence, usually represented as 𝐷
- Propositional function
• A proposition 𝑃(𝑥) about the variable 𝑥 contained in the universe of discourse 𝐷
• Example
▪ 𝑃 𝑥 = 𝑥2 is even. (𝐷 : a set of positive integers)
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Quantifier

## Page 35

35
Mathematical Basics for Understanding modern
Cryptography
⚫ Types of quantifier
- Universal quantifier
• Denoted by the symbol ∀𝑥 and written as for all 𝑥
• Examples
▪ ∀𝑥 𝑃 𝑥
▪ The propositional function 𝑃(𝑥) is true for all domains 𝑥 in the universe of discourse 𝐷
- Existential quantifier
• Denoted by the symbol ∃𝑥 and written as for some 𝑥
• Example
▪ ∃𝑥 𝑃 𝑥
− For each domain 𝑥 belonging to D, there exists at least one such that the
propositional function 𝑃(𝑥) is true.
A proposition is a statement or mathematical expression that can be clearly distinguished as
either true or false. The essence of logic is to determine whether a proposition is true or false by
using negation, conjunction, disjunction, exclusive-or, etc. in such a statement or mathematical
expression.
Quantifier

## Page 36

36
Mathematical Basics for Understanding modern
Cryptography
⚫ Set
- A collection of objects (elements) that share common characteristics.
- If element 𝑥 belongs to set 𝐴, then,
• Written as 𝑥 is an element of the set 𝐴.
• Denoted by 𝑥 ∈ 𝐴
- If the element is not an element 𝑥 of the set 𝐴, then,
• Denoted by 𝑥 ∉ 𝐴
A set is a collection of elements that have a common characteristic. Sets allow us to compute and
represent sets in various forms, such as union, co-union, difference, and union.
Set

## Page 37

37
Mathematical Basics for Understanding modern
Cryptography
⚫ Types of sets
- Universal set
• A set that contains all the elements of a given set.
• Denoted by 𝑈
- Empty set
• A set that does not contain a single element
• Denoted by { } or ∅
- Exercises
• Explain what the set A={ a | , where a is a positive integer} is.
- Solve
• It is a union because positive integers do not exist.
A set is a collection of elements that share a common characteristic. Sets allow us to compute
and express membership in various forms, such as universal set, empty set, relative complement,
and union.
Types of sets
 Practice question
• Explain what the set 𝐴 =  𝑥 𝑥 + 1 < 0, 𝑥 𝑖𝑠 𝑎 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒 𝑖𝑛𝑡𝑒𝑔𝑒𝑟} is.
 Answer
• It is an empty set because there are no positive integers.

## Page 38

38
Mathematical Basics for Understanding modern
Cryptography
⚫ Types of sets
- Subset
• Define 𝐴 to be a subset of 𝐵 if 𝐴 and 𝐵 are sets and all elements of 𝐴 are contained in 𝐵.
• Denoted by 𝐴 ⊆ 𝐵
• 𝐴 ⊆ 𝐵 ≡ (𝑎 ∈ 𝐴 → 𝑎 ∈ 𝐵), ∀𝑎
- Proper subset
• 𝐴 is a subset of 𝐵, but 𝐴 and 𝐵 are not the same.
• Denoted by 𝐴 ⊂ 𝐵
A set is a collection of elements that share a common characteristic. Sets allow us to compute
and express membership in various forms, such as universal set, empty set, relative complement,
and union.
Types of sets

## Page 39

39
Mathematical Basics for Understanding modern
Cryptography
⚫ Types of sets
- Finite set
• A set of a finite number of elements
- Infinite set
• That which is not a finite set.
• Well-known infinite sets
▪ 𝑅 = 𝑥 𝑥 𝑖𝑠 𝑎 𝑟𝑒𝑎𝑙𝑛𝑢𝑚𝑏𝑒𝑟}
▪ 𝑄 = 𝑥 𝑥 𝑖𝑠 𝑎 𝑟𝑎𝑡𝑖𝑜𝑛𝑎𝑙𝑛𝑢𝑚𝑏𝑒𝑟}
▪ 𝑍 = 𝑥 𝑥 𝑖𝑠 𝑎𝑛 𝑖𝑛𝑡𝑒𝑔𝑒𝑟}
▪ 𝑁 = 𝑥 𝑥 𝑖𝑠 𝑎 𝑛𝑎𝑡𝑢𝑟𝑎𝑙𝑛𝑢𝑚𝑏𝑒𝑟}
▪ 𝑅 + = {𝑥 ∈ 𝑅 | 𝑥 > 0}
▪ 𝐼 = {𝑥 ∈ 𝑅 | 0 ≤ 𝑥 ≤ 1}
A set is a collection of elements that share a common characteristic. Sets allow us to compute
and express membership in various forms, such as universal set, empty set, relative complement,
and union.
Types of sets

## Page 40

40
Mathematical Basics for Understanding modern
Cryptography
⚫ Element
- Roster notation
• A way of denoting a set by listing all the elements in a set within { } using commas.
- Set-builder notation
• A way of denoting a set by specifying the condition(s) of common properties of elements in a set.
• Represent the set A with elemental enumeration and conditional expressions so that set A
has elements 2, 4, 6, 8, and 10.
• Elemental sequencing
▪ Set A = {2, 4, 6, 8, 10}
• Conditional statements
▪ Set A = { a | , where a is an even number}
A set is a collection of elements that share a common characteristic. Sets allow us to compute
and express membership in various forms, such as universal set, empty set, relative complement,
and union.
Element
 Practice question
• Denote the set containing 2, 4, 6, 8, and 10 in roster notation and set-builder notation.
 Answer
• Roster notation
▪ Set 𝐴 =  {2, 4, 6, 8, 10}
• Set-builder notation
▪ Set 𝐴 =  𝑎 2 ≤ a ≤ 10, 𝑎 𝑖𝑠 𝑎𝑛 𝑒𝑣𝑒𝑛 𝑛𝑢𝑚𝑏𝑒𝑟}

## Page 41

41
Mathematical Basics for Understanding modern
Cryptography
⚫ Equality (equal sets)
- Two sets 𝐴 and 𝐵 have the same elements
- Sets are equal.
- Denoted by 𝐴 = 𝐵
- While 𝑎 ∈ 𝐴 is 𝑎 ∈ 𝐵, 𝑎 ∈ 𝐵 is 𝑎 ∈ 𝐴, then 𝐴 = 𝐵.
• A = B ≡ (a ∈ A
 a ∈ B)
A set is a collection of elements that share a common characteristic. Sets allow us to compute
and express membership in various forms, such as universal set, empty set, relative complement,
and union.
Element

## Page 42

42
Mathematical Basics for Understanding modern
Cryptography
⚫ Cardinality
- Number of elements in the finite set 𝐴
- Denoted by |𝐴|
⚫ Practice question
- Find the cardinality(ies) of the given set 𝐴 = 𝑎 a < 10, 𝑎 𝑖𝑠 𝑎 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑖𝑛𝑡𝑒𝑔𝑒𝑟}.
- Since the set is 𝐴={1, 2, 3, 4, 5, 6, 7, 8, 9}, the cardinality |𝐴|=9.
A set is a collection of elements that share a common characteristic. Sets allow us to compute
and express membership in various forms, such as universal set, empty set, relative complement,
and union.
Element
 Practice question
• Find the cardinality(ies) of the given set 𝐴 =  𝑎 a < 10, 𝑎 𝑖𝑠 𝑎 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒 𝑖𝑛𝑡𝑒𝑔𝑒𝑟}.
 Answer
• Since the set is 𝐴={1, 2, 3, 4, 5, 6, 7, 8, 9}, the cardinality |𝐴|=9.

## Page 43

43
Mathematical Basics for Understanding modern
Cryptography
⚫ Basic relation
- The representation of a relationality between elements is called a relation.
• Denotes this relation as the symbol 𝑅
• 𝑎 has a relationship of 𝑅 to 𝑏
• sometimes denoted by 𝑎𝑅𝑏
• Example
▪ Two sets 𝐴, 𝐵, are in a binary relation where a subset of 𝐴×𝐵 is
− in (𝑎, 𝑏) ∈ 𝑅 in which 𝑎 ∈ 𝐴 and 𝑏 ∈ 𝐵.
• Domain
▪ The set of all first elements in the order pairs of the relation 𝑅 : 𝑑𝑜𝑚(𝑅)
• Range
▪ The set of all second elements : 𝑟𝑎𝑛(𝑅)
A relation is a structure for expressing associations between elements of a set. These structures
can be represented using schema such as arrow diagrams and coordinate diagrams. To
understand the properties of relations, we study types of relations such as reflection relations,
symmetry relations.
Relation

## Page 44

44
Mathematical Basics for Understanding modern
Cryptography
⚫ An 𝑛-ary relation
- A relation between elements in two or more sets
- Often used to express databases
• Database
▪ A set of data that is integrated, stored, and operated so that multiple application
systems in an organization can share it.
− Relational database model
− Developed based on the concept of 𝑛-ary relation in a database.
- Exercises
• Find the number of relationships that can be created in when A={a,b} and B={1,2}.
- Solve
• 𝐴 × 𝐵 = 𝑎, 1 , 𝑎, 2 , 𝑏, 1 , 𝑏, 2
• 24 = 16
A relation is a structure for expressing associations between elements of a set. These structures
can be represented using schema such as arrow diagrams and coordinate diagrams. To
understand the properties of relations, we study types of relations such as reflection relations,
symmetry relations.
Relation
 Practice question
• Find the number of relations that can be created from 𝐴 × 𝐵 in 𝐴 = {𝑎, 𝑏}, 𝐵 = {1, 2}.
 Answer
• 𝐴 × 𝐵 = {(𝑎, 1), (𝑎, 2), (𝑏, 1), (𝑏, 2)}
• 24 =  16

## Page 45

45
Mathematical Basics for Understanding modern
Cryptography
⚫ Inverse relation
- A relation consisting of the inverses of elements of two or more sets.
• Denoted by 𝑅−1
• 𝑅−1 = 𝑏, 𝑎 ∈ 𝐵 × 𝐴 𝑎, 𝑏 ∈ 𝑅}
- Exercises
• Find , the inverse of the relationship
- Solve
• 𝑅−1 = { 4,1 , 3,2 , 5,2 , 3,3 }
A relation is a structure for expressing associations between elements of a set. These structures
can be represented using schema such as arrow diagrams and coordinate diagrams. To
understand the properties of relations, we study types of relations such as reflection relations,
symmetry relations.
Relation
 Practice question
• Find , the inverse relation 𝑅−1 of the relation 𝑅 = {(1,4), (2,3), (2,5), (3,3)}.
 Answer
• 𝑅−1 = { 4,1 , 3,2 , 5,2 , 3,3 }

## Page 46

46
Mathematical Basics for Understanding modern
Cryptography
⚫ Matrix
- A rectangular array of numbers
- The matrix with m rows and n columns if m and n are positive integers :
•
𝑎11 ⋯ 𝑎1𝑛
⋮ ⋱ ⋮
𝑎𝑚1 ⋯ 𝑎𝑚𝑛
- The element in the i-th row and the element in the j-th column : 𝑎𝑖𝑗
- The matrix with elements 𝑎𝑖𝑗 : 𝑎𝑖𝑗
We will understand matrices expressed in a form of arrays and familiarize ourselves with the
different types of matrices: zero, square, unit, and transposed.
Matrix

## Page 47

47
Mathematical Basics for Understanding modern
Cryptography
⚫ Matrix
- Equality
• Given an 𝑚 × 𝑛 matrix 𝐴 = 𝑎𝑖𝑗 and an 𝑟 × 𝑠 matrix 𝐵 = 𝑏𝑖𝑗 , for all 𝑖, 𝑗, if 𝑚 = 𝑟, 𝑛 = 𝑠 and
1 ≤ 𝑖 ≤ 𝑚, 1 ≤ 𝑗 ≤ 𝑛, then 𝐴 and 𝐵 are said to be equal.
▪ Denoted by 𝐴 = 𝐵
- Matrix addition and subtraction
• Given 𝑚 × 𝑛 matrices 𝐴 = 𝑎𝑖𝑗 and 𝐵 = 𝑏𝑖𝑗 , the two matrices can be added or subtracted :
▪ 𝐴 + 𝐵 = 𝑎𝑖𝑗 + 𝑏𝑖𝑗
▪ 𝐴 − 𝐵 = 𝑎𝑖𝑗 − 𝑏𝑖𝑗
- Scalar multiplication
• Given a 𝑚 × 𝑛matrix𝐴 = 𝑎𝑖𝑗 and a real (scalar) number 𝑘, the scalar multiplication of 𝐴 and 𝑘 ∶
▪ 𝐴𝑘 = 𝑘𝐴 = [𝑘𝑎𝑖𝑗]
We will understand matrices expressed in a form of arrays and familiarize ourselves with the
different types of matrices: zero, square, unit, and transposed.
Matrix

## Page 48

48
Mathematical Basics for Understanding modern
Cryptography
⚫ Matrix
- Properties of scalar addition and multiplication (𝑂 is a matrix where all elements are zero.)
• 𝐴 + 𝐵 = 𝐵 + 𝐴
• 𝐴 + (𝐵 + 𝐶) = (𝐴 + 𝐵) + 𝐶
• 𝐴 + 𝑂 = 𝐴 = 𝑂 + 𝐴
• 𝐴 + (−𝐴) = 𝑂 = (−𝐴) + 𝐴
• (−1)𝐴 = −𝐴
• 𝑐(𝐴 + 𝐵) = 𝑐𝐴 + 𝑐𝐵
• (𝑐 + 𝑑)𝐴 = 𝑐𝐴 + 𝑑𝐴
• (𝑐𝑑)𝐴 = 𝑐(𝑑𝐴)
We will understand matrices expressed in a form of arrays and familiarize ourselves with the
different types of matrices: zero, square, unit, and transposed.
Matrix

## Page 49

49
Mathematical Basics for Understanding modern
Cryptography
⚫ Matrix
- Exercises
• Find A+B, A+C, A+2B if the matrices A, B, and C are as follows.
• , ,
- Solve
• 𝐴 + 𝐵 = 1 2
−2 5 + 3 4
6 1 = 4 6
4 6
• A + C is not computable because they are different matrices of different sizes
• 𝐴 + 2𝐵 = 1 2
−2 5 + 2 3 4
6 1 = 1 2
−2 5 + 6 8
12 2 = 7 10
10 7
We will understand matrices expressed in a form of arrays and familiarize ourselves with the
different types of matrices: zero, square, unit, and transposed.
Matrix
 Practice question
• Find 𝐴 + 𝐵, 𝐴 + 𝐶, 𝐴 + 2𝐵, given that the matrices 𝐴, 𝐵, and 𝐶 are as follows :
• 𝐴 = 1 2
−2 5 , 𝐵 = 3 4
6 1 , 𝐶 = −1 8 0
2 0 4
 Answer
• 𝐴 + 𝐵 = 1 2
−2 5 + 3 4
6 1  = 4 6
4 6
• 𝐴 + 𝐶 are not computable because they are matrices of different sizes.
• 𝐴 + 2𝐵 = 1 2
−2 5 + 2 3 4
6 1 = 1 2
−2 5 + 6 8
12 2 = 7 10
10 7

## Page 50

50
Mathematical Basics for Understanding modern
Cryptography
⚫ Matrix
- Matrix multiplication
• Given an 𝑚 × 𝑛 matrix 𝐴 = 𝑎𝑖𝑗 and an 𝑟 × 𝑠 matrix 𝐵 = 𝑏𝑖𝑗 , if 𝑛 = 𝑟, then the
multiplication of the matrices can be expressed as :
▪ 𝑚 × s matrix 𝐴𝐵 = c𝑖𝑗
▪ 𝑐𝑖𝑗 = 𝑎𝑖1𝑏1𝑗 + 𝑎𝑖2𝑏2𝑗 + ⋯ + 𝑎𝑖𝑛𝑏𝑛𝑗 = σ𝑘=1
𝑛 𝑎𝑖𝑘𝑏𝑘𝑗
• Properties of products and scalars
▪ (𝐴𝐵)𝐶 = 𝐴(𝐵𝐶)
▪ 𝐴(𝐵 + 𝐶) = 𝐴𝐵 + 𝐴𝐶
▪ (𝐵 + 𝐶)𝐴 = 𝐵𝐴 + 𝐶𝐴
▪ 𝑘(𝐴𝐵) = (𝑘𝐴)𝐵 = 𝐴(𝑘𝐵)
We will understand matrices expressed in a form of arrays and familiarize ourselves with the
different types of matrices: zero, square, unit, and transposed.
Matrix

## Page 51

51
Mathematical Basics for Understanding modern
Cryptography
⚫ Matrix
- Matrix multiplication
• Practice question
▪ Find the product of the following two matrices 𝐴𝐵.
▪ 𝐴 = 1 2
3 4 , 𝐵 = 2 −1
−1 2
• Answer
▪ 𝐴𝐵 = 1 2
3 4
2 −1
−1 2 = 0 3
2 5
We will understand matrices expressed in a form of arrays and familiarize ourselves with the
different types of matrices: zero, square, unit, and transposed.
Matrix
 Practice question
• Find the product of the following two matrices 𝐴𝐵.
• 𝐴 = 1 2
3 4 , 𝐵 = 2 −1
−1 2
 Answer
• 𝐴𝐵 = 1 2
3 4
2 −1
−1 2 = 0 3
2 5

## Page 52

52
Security of cryptographic algorithms
⚫ Cryptanalysis attacks
- Ciphertext-only attacks
• Exhaustive search attacks
• Statistical attacks
• Pattern attacks
- Known-plaintext attacks
- Chosen-plaintext attacks
- Chosen-ciphertext attacks
- Chosen text attacks
Just as cryptography is the science and art of creating a secret code, cryptanalysis is the science
and art of breaking codes. Cryptanalytic techniques are needed to measure the vulnerability of a
system, not to hack someone else's code.
Cryptanalysis

## Page 53

53
Security of cryptographic algorithms
⚫ Ciphertext-only attacks
- Eve obtains a ciphertext and finds the corresponding plaintext and key.
• Assuming Eve knows the encryption algorithm and can intercept the ciphertext.
- This is the easiest attack to apply because it only attempts to crack a ciphertext.
• Exhaustivesearch attacks: repeats the attack until a meaningfulplaintextis obtained.
• Statistical attacks : exploits the frequency of alphabet usage.
• Pattern attacks : exploits any pattern that may be present in a ciphertext.
Just as cryptography is the science and art of creating a secret code, cryptanalysis is the science
and art of breaking codes. Cryptanalytic techniques are needed to measure the vulnerability of a
system, not to hack someone else's code.
Cryptanalysis
Alice
Ciphertext
Ciphertext
BobEve
Plaintext
Analyze
Ciphertext

## Page 54

54
Security of cryptographic algorithms
⚫ Known-plaintext attacks
- Known-plaintext attacks use boilerplate or common phrases.
• Common phrases in emails and text messages, such as "hello" and "thank you"
- Used to determine a secret key based on a known plaintext/ciphertext pair.
Just as cryptography is the science and art of creating a secret code, cryptanalysis is the science
and art of breaking codes. Cryptanalytic techniques are needed to measure the vulnerability of a
system, not to hack someone else's code.
Cryptanalysis
Alice
Ciphertext
Ciphertext
BobEve
Plaintext
Analyze
Ciphertext
Previous pair

## Page 55

55
Security of cryptographic algorithms
⚫ Chosen-plaintext attacks
- Similar to known-plaintext attacks
- An attacker selects a plaintext/ciphertext pair.
- Used when an attacker has access to the encryption module.
Just as cryptography is the science and art of creating a secret code, cryptanalysis is the science
and art of breaking codes. Cryptanalytic techniques are needed to measure the vulnerability of a
system, not to hack someone else's code.
Cryptanalysis
Alice
Ciphertext
Ciphertext
Bob
Eve
Plaintext
Analyze
Ciphertext
Pair created from
chosen plaintext

## Page 56

56
Security of cryptographic algorithms
⚫ Chosen-ciphertext attacks
- Similar to chosen-plaintext attacks
- An attacker selects a ciphertext and obtains the corresponding plaintext.
- Used when an attacker has access to the decryption module.
Just as cryptography is the science and art of creating a secret code, cryptanalysis is the science
and art of breaking codes. Cryptanalytic techniques are needed to measure the vulnerability of a
system, not to hack someone else's code.
Cryptanalysis
Alice
Ciphertext
Ciphertext
Bob
Eve
Plaintext
Analyze
Ciphertext
Pair created from
chosen ciphertext

## Page 57

57
Security of cryptographic algorithms
⚫ Chosen text attacks
- An attacker selects a ciphertext/plaintext or plaintext/ciphertext pair.
- Used when an attacker has access to both the encryption and decryption modules.
Just as cryptography is the science and art of creating a secret code, cryptanalysis is the science
and art of breaking codes. Cryptanalytic techniques are needed to measure the vulnerability of a
system, not to hack someone else's code.
Cryptanalysis
Ciphertext
Bob
Eve
Plaintext
Analyze
Ciphertext
Pair created from
chosen ciphertext
Alice
Ciphertext
Pair created from
chosen plaintext

## Page 58

58
Security of cryptographic algorithms
⚫ Transposition ciphers
- Rearranges text character by character for encryption
• Permutation – an attacker picks a few specific
characters and lists them in order.
• Performs a permutation to obtain plaintext.
- Types of transposition ciphers
• Rail fence cipher
• Route cipher
• Columnar transposition cipher
A transposition cipher is a method of repositioning characters on a character-by-character basis.
It was used in ancient battles to covertly convey messages, but is no longer used directly, but
rather in conceptual applications.
Transposition cipher
C
Y
B
E
B
Y
E
R
R C

## Page 59

59
Security of cryptographic algorithms
⚫ Transposition ciphers
- Rail fence cipher
• What feels like organizing characters in a rail fence to encrypt them.
- Example
• Plaintext - WE ARE ACS CYBER SECURITY
• Key - 3
• Ciphertext - WECRUYERASYESCRTACBEI
A transposition cipher is a method of repositioning characters on a character-by-character basis.
It was used in ancient battles to covertly convey messages, but is no longer used directly, but
rather in conceptual applications.
Transposition cipher
W E C R U Y
E R A S Y E S C R T
A C B E I
Key

## Page 60

60
Security of cryptographic algorithms
⚫ Transposition ciphers
- Route cipher
• Transpose characters along a specified path, as indicated by the name “route.”
• Specify path rules in addition to keys.
• Fill in the X for spaces.
- Example
• Plaintext - WE ARE ACS
• Key - 3
• Path – counter-clockwise from top left
• Passphrase - WRCSXAAEE
A transposition cipher is a method of repositioning characters on a character-by-character basis.
It was used in ancient battles to covertly convey messages, but is no longer used directly, but
rather in conceptual applications.
Transposition cipher
W E A
R E A
C S X
Key

## Page 61

61
Security of cryptographic algorithms
⚫ Transposition ciphers
- Columnar transposition cipher
• Use columnar transposition for encryption.
• Assign a specific character to each column and use it as the key
- Example
• Plaintext - WE ARE ACS
• Key - KEY
• Ciphertext - EWAERASCX
- This can be mixed with the route cipher :
• Path – counter-clockwise from top left
• Ciphertext - EESCXAAWR
A transposition cipher is a method of repositioning characters on a character-by-character basis.
It was used in ancient battles to covertly convey messages, but is no longer used directly, but
rather in conceptual applications.
Transposition cipher
W E A
R E A
C S X
K E Y
E W A
E R A
S C X
E K Y

## Page 62

62
Security of cryptographic algorithms
⚫ Transposition ciphers
- Other types of transposition ciphers
• Double transposition
• Myszkowski transposition
• Disrupted Transposition
• Grille
• Scytale
A transposition cipher is a method of repositioning characters on a character-by-character basis.
It was used in ancient battles to covertly convey messages, but is no longer used directly, but
rather in conceptual applications.
Transposition cipher
Scytale ciphertext

## Page 63

63
Security of cryptographic algorithms
⚫ Simple substitution ciphers
- Character-by-character substitutions based on a given rule
A simple substitution cipher is one in which characters are substituted according to a certain
rule. Some elements are currently in use, but as in the case of transposition ciphers, the concept
is applied indirectly rather than directly.
C
Y
B
E
H
D
G
J
R W
E
Simple substitution cipher

## Page 64

64
Security of cryptographic algorithms
⚫ Caesar cipher
- Swipe an alphabet a certain distance to replace it with another alphabet
- Also known as shift cipher, Caesar shift, and additive cipher
- All operations are performed within 𝑍26, assuming that plaintext is lowercase and ciphertext
is uppercase.
- The encryption algorithm is the key plus the plaintext character.
- The decryption algorithm is the key minus the ciphertext character.
A simple substitution cipher is one in which characters are substituted according to a certain
rule. Some elements are currently in use, but as in the case of transposition ciphers, the concept
is applied indirectly rather than directly.
Alice Bob
𝑪 = 𝑷 + 𝑲 𝒎𝒐𝒅 𝟐𝟔 𝑷 = 𝑪 − 𝑲 𝒎𝒐𝒅 𝟐𝟔
Encryption Decryption
Ciphertext
Plaintext Plaintext
Simple substitution cipher

## Page 65

65
Security of cryptographic algorithms
⚫ ROT13 (Rotate by 13)
- Used in information security
- This is a Caesar cipher with the key 13.
- In the registry, the UserAssist key is configured as ROT13.
A simple substitution cipher is one in which characters are substituted according to a certain
rule. Some elements are currently in use, but as in the case of transposition ciphers, the concept
is applied indirectly rather than directly.
Simple substitution cipher
ROT13
UEME_CTLSESSION
UEME_CTLSESSION
UserAssist ID

## Page 66

66
Security of cryptographic algorithms
⚫ Multiplication cipher
- The encryptionalgorithmperformsmodulo operationsby multiplyingthe plaintextby the key.
- The decryption algorithm performs modulo operations by multiplying the ciphertext by the
inverse of the key.
- The key mustbe an elementof 𝑍26
∗ to ensurethatthe encryption/decryptionare inverselyrelated.
- Contains only the numbers for which gcd(26, 𝑥) ≡ 1 holds when Euclidean algorism is applied.
• Key space : 12 from 𝑍26
∗ = {1,3,5,7,9,11,15,17,19,21,23,25}
• 13 is a prime number, but excluded from the keyspace since gcd(26,13) ≡ 13 comes out.
A simple substitution cipher is one in which characters are substituted according to a certain
rule. Some elements are currently in use, but as in the case of transposition ciphers, the concept
is applied indirectly rather than directly.
Simple substitution cipher
Alice Bob
𝑪 = 𝑷 ∗ 𝑲 𝒎𝒐𝒅 𝟐𝟔 𝑷 = 𝑪 ∗ 𝑲−𝟏 𝒎𝒐𝒅 𝟐𝟔
Encryption Decryption
Ciphertext
Plaintext Plaintext

## Page 67

67
⚫ Multiplication cipher
- Euclidean algorithm
• Euclidean algorithm for finding the greatest common divisor
of two natural numbers.
• Denoted by gcd(𝑥, 𝑦)
• E.g., gcd 26,7 𝑋 = 𝐴 − 𝐵 ∗ 𝑅 ∴ 𝑋 = 26 − 7 ∗ 3 = 5
- Extended Euclidean algorithm
• In 𝑍26, find the inverse element of 7.
▪ Apply the extended algorithm, to the part where 1 appears by the Euclidean algorithm.
▪ The number at the position of 1 is
the inverse element of 7.
▪ In 𝑍26, the number ranges from 0 to 25,
so -11mod26
▪ Therefore, the inverse element of 7 is 15
▪ Validation : 15 ∗ 7𝑚𝑜𝑑26 ≡ 1
Security of cryptographic algorithms
Simple substitution cipher
3 26 7 5
1 7 5 2
2 5 2 1
2 1
A BR X
3 26 7 5 0 1 -3
1 7 5 2 1 -3 4
2 5 2 1 -3 4 -11
2 1 4 -11
A BR X

## Page 68

68
Security of cryptographic algorithms
⚫ Polyalphabetic substitution cipher (PSC)
- Character-by-character substitution based on multiple types of set rules
Polyalphabetic substitution ciphers were developed to address the shortcomings of simple
substitution ciphers. It uses multiple iterations of the simplex algorithm, which increased in
complexity as machines were built and advanced during the war.
Polyalphabetic substitution cipher
C
Y
B
E
V
W
N
I
R N
E1 E2 E3

## Page 69

69
Security of cryptographic algorithms
⚫ Vigenère cipher
- There are key, plaintext, and Vigenère tables.
- Key and Vigenère tables are freely configurable, but require fixed principles.
- Can be decrypted to plaintext with key, ciphertext, and Vigenère tables together.
• E.g., key - CRYPTO, plaintext - INFORMATION SECURITY
Polyalphabetic substitution ciphers were developed to address the shortcomings of simple
substitution ciphers. It uses multiple iterations of the simplex algorithm, which increased in
complexity as machines were built and advanced during the war.
Polyalphabetic substitution cipher
Key C R Y P T O C R Y P T O C R Y P T O C
P I N F O R M A T I O N S E C U R I T Y
C K E D D K A C K G D G G G T S G B H A

## Page 70

70
Security of cryptographic algorithms
Polyalphabetic substitution cipher
Vigenère Table

## Page 71

71
Security of cryptographic algorithms
⚫ Playfair cipher
- Developed by the British physicist Charles Wheatstone and the mathematician and geologist
John Playfair.
- Features
• Key - a 5x5 alphabetical matrix containing certain words
• Matrix organization
▪ Represent all spellings, with keys, in a matrix of 25
without duplicates.
▪ In 26 alphabet letters, I/J or Q/Z count as one letter.
▪ The order is up to the array creator, except for
certain words.
• Example
▪ Matrix containing a certain word (CYBER)
Polyalphabetic substitution ciphers were developed to address the shortcomings of simple
substitution ciphers. It uses multiple iterations of the simplex algorithm, which increased in
complexity as machines were built and advanced during the war.
Polyalphabetic substitution cipher
C Y B E R
A D F G H
I/J K L M N
O P Q S T
U V W X Z

## Page 72

72
Security of cryptographic algorithms
⚫ Playfair cipher
- Encryption
• Plaintext - HELLO EVERYONE
▪ Pair two letters of the alphabet and insert a random alphabet (usually X) between the
repeated letters.
▪ HE LX LO EV ER YO NE
• Key - matrix
Polyalphabetic substitution ciphers were developed to address the shortcomings of simple
substitution ciphers. It uses multiple iterations of the simplex algorithm, which increased in
complexity as machines were built and advanced during the war.
Polyalphabetic substitution cipher
C Y B E R
A D F G H
I/J K L M N
O P Q S T
U V W X Z

## Page 73

73
Security of cryptographic algorithms
⚫ Playfair cipher
- Encryption
• Ciphertext 1
▪ HE are diagonal to each other, so choose words on opposite diagonals of the same
square size.
▪ H to E is down → up
− The move to the same direction creates a GR pair.
• Ciphertext 2
▪ LX creates MW in the same way.
Polyalphabetic substitution ciphers were developed to address the shortcomings of simple
substitution ciphers. It uses multiple iterations of the simplex algorithm, which increased in
complexity as machines were built and advanced during the war.
Polyalphabetic substitution cipher
Plaintext - HELLO EVERYONE
Variation - HE LX LO EVER YO NE
C Y B E R
A D F G H
I/J K L M N
O P Q S T
U V W X Z

## Page 74

74
Security of cryptographic algorithms
⚫ Playfair cipher
- Encryption
• Ciphertext 3
▪ LO creates IQ.
• Ciphertext 4
▪ EV creates YX.
• Ciphertext 5
▪ ER is on the same line and in this case move
one space to the right.
▪ For the right end, move to the opposite side
of the same row.
▪ Since the direction is from E to R, ER creates RC.
Polyalphabetic substitution ciphers were developed to address the shortcomings of simple
substitution ciphers. It uses multiple iterations of the simplex algorithm, which increased in
complexity as machines were built and advanced during the war.
Polyalphabetic substitution cipher
C Y B E R
A D F G H
I/J K L M N
O P Q S T
U V W X Z
Plaintext - HELLO EVERYONE
Variation - HE LX LO EVER YO NE

## Page 75

75
Security of cryptographic algorithms
⚫ Playfair cipher
- Encryption
• Ciphertext 6
▪ YO creates CP.
• Ciphertext 7
▪ NE creates MR.
• Final ciphertext :
▪ GR MW IQ YX RC CP MR
• Although this is not present in the current example,
if a pair of two letters exists in the same column,
▪ Replace them with the characters in the set direction.
▪ E.g., EM would create GS.
Polyalphabetic substitution ciphers were developed to address the shortcomings of simple
substitution ciphers. It uses multiple iterations of the simplex algorithm, which increased in
complexity as machines were built and advanced during the war.
Polyalphabetic substitution cipher
C Y B E R
A D F G H
I/J K L M N
O P Q S T
U V W X Z
Plaintext - HELLO EVERYONE
Variation - HE LX LO EVER YO NE

## Page 76

76
Security of cryptographic algorithms
⚫ Playfair cipher
- Decryption
• Final ciphertext - GR MW IQ YX RC CP MR
▪ GR is diagonal to each other, so this pair is replaced by HE.
▪ MW is replaced by LX.
▪ RC moves one place to the left, i.e., to the opposite side of the algorithm,
which creates ER.
▪ ...
Polyalphabetic substitution ciphers were developed to address the shortcomings of simple
substitution ciphers. It uses multiple iterations of the simplex algorithm, which increased in
complexity as machines were built and advanced during the war.
Polyalphabetic substitution cipher
C Y B E R
A D F G H
I/J K L M N
O P Q S T
U V W X Z

## Page 77

77
Security of cryptographic algorithms
⚫ Mechanical substitution ciphers
- Enigma
• German cryptographic system invented during World War II
• Enigma cryptanalysis system
▪ The Bombe in the UK
A machine substitution cipher is a mathematically based cryptosystem invented during World
War II to encrypt military and strategic messages that needed to be kept secret. Most of these
machines are complex implementations of polyalphabetic substitution ciphers.
Mechanical substitution cipher
Enigma
Bomb

## Page 78

78
Security of cryptographic algorithms
⚫ Mechanical substitution ciphers
- There were a variety of mechanical substitution ciphers other than the examples listed here.
- These became obsolete with the advent of computers.
A machine substitution cipher is a mathematically based cryptosystem invented during World
War II to encrypt military and strategic messages that needed to be kept secret. Most of these
machines are complex implementations of polyalphabetic substitution ciphers.
Mechanical substitution cipher
Purple (Type B Cipher Machine) in JapanColossus in UK
Boris Hagelin  in Switzerland

## Page 79

Symmetric Key
Encryption
02
• Block cipher overview
• Block ciphers : operation modes
• Block ciphers : DES, 3DES, AES
• Stream cipher

## Page 80

80
⚫ Symmetric-key cipher : an algorithm that uses the same secret key for encryption and
decryption.
- Advantages : fast encryption and decryption speeds
- Disadvantages : requires sharing of the same symmetric key for encrypted communication
- Plaintext : an original message sent by Alice to Bob
- Ciphertext : an encrypted message sent over a channel
- Alice and Bob use an encryption and decryption algorithm and a shared secret key.
Block cipher overview
Symmetric key cipher
Alice
Plaintext
Ciphertext
 Ciphertext
Plaintext
Bob
Encryption
algorithm
Decryption
algorithm
Secure key-exchange channel
Insecure channel

## Page 81

81
⚫ Alice's encryption : 𝐶 = 𝐸𝑘(𝑃)
⚫ Bob's decryption : 𝑃 = 𝐷𝑘 𝐶 , 𝑃 = 𝐷𝑘 𝐶 = 𝐷𝑘 𝐸𝑘 𝑃 = 𝑃
⚫ Assuming that encryption /decryption are inversely related, 𝐷𝑘 𝐸𝑘 𝑥 = 𝐸𝑘 𝐷𝑘 𝑥 = 𝑥 is
established.
⚫ Claude Shannon’s information theory
- Diffusion : the property that changes in the plaintext cannot affect changes in the ciphertext
- Non-linear function
• Hide the relationship between plaintext and ciphertext
• Make ciphertexts unbreakable by the frequency of occurrence of the language
- Chaos : the property of breaking a plaintext into multiple ciphertexts - Linear function
• Hide the relationship between ciphertext and key
• Make it impossible to find the key by using ciphertexts
- Kerckhoff's principle
• A cryptosystem should be secure even if an attacker knows the encryption/decryption
algorithm.
• This means that the cryptosystem should be secure based on the complexity of the key
alone.
Block cipher overview
Symmetric key cipher

## Page 82

82
Block cipher overview
⚫ Well-known block cipher algorithms
- Data Encryption Standard (DES)
• A cryptographic algorithm established by the US National Institute of Standards and
Technology (NIST) in 1977.
• Encrypted 64-bit blocks with 56-bit keys
• Small key lengths make it vulnerable to exhaustive key search attacks
• Perform 3-DES with triple encryption as a temporary alternative
- Advanced Encryption Standard (AES)
• A cryptographic algorithm established by the US NIST in 2001.
• The Rijndael cryptographic algorithm proposed in the contest became AES.
• Encrypted in 128-bit blocks with 128-bit or larger keys.
A symmetric-key cipher means that the keys used for encryption and decryption are the same.
Common types include block ciphers, which encrypt messages in blocks, and stream ciphers,
which are used to encrypt real-time communications.
Block cipher

## Page 83

83
Block cipher overview
⚫ Stream cipher is a type of symmetric-key cryptography.
⚫ Faster encryption than block ciphers
⚫ Generate a combined ciphertext with a logical exclusive-or (XOR) by generating a keystream
where the ciphertext is the same length as the plaintext.
⚫ Both the ciphertext generator and the receiver must share the same secret key and the same
initial state of the random number generator.
⚫ Usage
- Commonly used in wireless communications
⚫ Used with Linear Feedback Shift Register (LFSR) designs
- Used to generate random numbers to make keys more secure when generating keystreams
of the same length as plaintext.
A symmetric-key cipher means that the keys used for encryption and decryption are the same.
Common types include block ciphers, which encrypt messages in blocks, and stream ciphers,
which are used to encrypt real-time communications.
Stream cipher

## Page 84

84
Block cipher overview
⚫ Types
- Synchronous stream ciphers
• When decrypting a ciphertext to find the plaintext, there must be a synchronization
between the keystream and the ciphertext.
• The keystream is generated independently of the plaintext, so the ciphertext and the
keystream in the ciphertext are independent, reducing the chance of information leakage.
• High speed cryptographic processing and low error propagation rate are advantages, but
low diffusion effect and lack of self-motivation are disadvantages
- Self-synchronous stream ciphers
• Keystreams are generated by function relations from plaintext or ciphertext
• Even if bits of ciphertextare lost or alteredduringtransmission, the effect of the error is finite.
• May include the ability to correct errors
• Easy to break due to dependencies between keystream and ciphertext
A symmetric-key cipher means that the keys used for encryption and decryption are the same.
Common types include block ciphers, which encrypt messages in blocks, and stream ciphers,
which are used to encrypt real-time communications.
Stream cipher

## Page 85

85
Block cipher overview
⚫ An algorithm used as a cryptosystem based on a block cipher design.
- Often referred to as a symmetric key cipher
⚫ Well-known block cipher algorithms
- Lucifer / DES
- Rijndael / AES
- Blowfish
A block cipher algorithm is a fully developed algorithm that uses block-based cipher design and
operation. Well-known block cipher algorithms include DES, AES, and Blowfish.
Block cipher algorithm
DES AES
Year of
development 1976 1999
Block size 64 128
Key length 56 128, 192, 256
Number of rounds 16 9, 11, 13
Password
primitive
Substitution, permutation,
chaos, and diffusion
Substitution, shift, bit-
mixing, chaos, diffusion
Design Public Public
Design theory Private Public

## Page 86

86
Block cipher overview
⚫ Block cipher design
- Refers to the design approach underlying the block cipher algorithm.
- Basic block cipher design
• Key security and performance
▪ Whitening – performs round key XOR followed by encryption, and the final encryption
with the round key before generating the ciphertext.
▪ Tweakable - tweaks the encryption key one more time using a tweakable key that is
separate from the round key.
• Complexity requirements
▪ Avalanche - an avalanche-like increase in the size of a ciphertext compared to the size of
the plaintext.
▪ Nonlinearity - complexity increased by configuring the spread to be irregular (non-
linear).
There are three key elements to constructing a block cipher : whitening and tweakability to
increase key security and performance, ciphertext complexity requirements, and the structure
of the repeated block cipher.
Block cipher design

## Page 87

87
Block cipher overview
⚫ Block cipher design
- Refers to the design approach underlying the block cipher algorithm.
- Basic block cipher design
• Iterated block cipher structure
▪ Feistel
▪ Substitution-Permutation Network (SPN)
▪ Lai-Massey - rarely used
There are three key elements to constructing a block cipher : whitening and tweakability to
increase key security and performance, ciphertext complexity requirements, and the structure
of the repeated block cipher.
Block cipher design

## Page 88

88
Block cipher overview
⚫ Iterated block cipher
- Features
• Basic structure shared by most block ciphers
• Repeated use to create cryptographically strong structures
• Apply chaos and diffusion in each round
• As the number of rounds increases, so does the height.
- Requires a key scheduling process where a key is entered to generate a round key
• Primary key - the original encryption key
• Round key - an independent encryption key created by splitting the primary key
- Advantages - security improves as the number of rounds increases.
- Disadvantages - less practical as the number of rounds increases.
There are three key elements to constructing a block cipher : whitening and tweakability to
increase key security and performance, ciphertext complexity requirements, and the structure
of the repeated block cipher.
Block cipher design

## Page 89

89
Block cipher overview
⚫ Iterated block cipher
- Feistel structure
• Structure for which the inverse function does not exist
• Decryption algorithm uses the same components.
• Flexible in designing compared to SPN
▪ SPN changes its entire value in one round, but only half of the Feistel structure changes.
− Structures designed with different sizes or numbers of partitions are called
unbalanced Feistel structures.
• Have a strong cipher design by iterating over weak rounds
• Signature algorithm using Feistel structure – DES
▪ DES executes 16 rounds of the Feistel structure.
There are three key elements to constructing a block cipher : whitening and tweakability to
increase key security and performance, ciphertext complexity requirements, and the structure
of the repeated block cipher.
Block cipher design

## Page 90

90
Block cipher overview
⚫ Iterated block cipher
- Feistel structure
• Divide a 64-bit plaintext block back into 32 bits
• XOR the left 32-bit block with the encrypted right 32-bit block
• Write the result to the right 32 bits
• Store existing right 32 bits in left 32 bits
There are three key elements to constructing a block cipher : whitening and tweakability to
increase key security and performance, ciphertext complexity requirements, and the structure
of the repeated block cipher.
Block cipher design
L1 R1
L2 R2
Plaintext
Ciphertext
32bits
Round
F
MixerSwapper
Round
key

## Page 91

91
Block cipher overview
⚫ Iterated block cipher
- Substitution-Permutation Network (SPN) structure
• Designed by Claude Shannon, the architect of chaos and diffusion
• Uses two layers in each round
• If the substitution layer causes chaos, the permutation layer diffuses
▪ Substitution layer = S-boxes, permutation layer = P-boxes
▪ Replace with another value by S-box round key
▪ P-boxes mix S-boxes coming in as input with S-boxes going out as output to create a
diffusion
• Signature algorithm using SPN structure - AES
There are three key elements to constructing a block cipher : whitening and tweakability to
increase key security and performance, ciphertext complexity requirements, and the structure
of the repeated block cipher.
Block cipher design

## Page 92

92
⚫ Iterated block cipher
- Substitution-Permutation Network (SPN) structure (example - Round 2)
Block cipher overview
Block cipher design
S-box #1 S-box #2 S-box #3
P-box #1
S-box #1 S-box #2 S-box #3
P-box #2
Plaintext
Ciphertext
(XOR) Key1
(XOR) Key2
(XOR) Key3
Key
Round key
Alternate layer (chaos)
Permutation layer (diffusion)
Round
Key schedule
Primary key

## Page 93

93
⚫ Diffie-Hellman key exchange consensus
- Theory that computing someone else's public key and your private key yields a secret key.
- Used for symmetric key exchange, not encryption or signing.
- Use discrete algebra problems
• When 𝑦 = 𝑔𝑥𝑚𝑜𝑑𝑝, it's easy to get 𝑦 if you know 𝑔, 𝑥, 𝑝, but hard to get 𝑥 if you know 𝑔, 𝑦, 𝑝.
- Both communicating parties generate symmetric keys without a KDC.
- Procedure
• Alice chooses a random large number 𝑥 inside 0 ≤ 𝑥 ≤ 𝑝 − 1 and calculates 𝑅1 = 𝑔𝑥𝑚𝑜𝑑𝑝.
• Bob chooses another random large number 𝑦 inside 0 ≤ 𝑦 ≤ 𝑝 − 1 and calculates 𝑅2 = 𝑔𝑦𝑚𝑜𝑑𝑝.
• Alice sends to Bob 𝑅1. Here Alice is not sending the value 𝑥, but only 𝑅1.
• Bob sends to Alice 𝑅2. Here Bob does not send 𝑦, but only 𝑅2
• Alice calculates 𝐾 = (𝑅2)𝑥𝑚𝑜𝑑𝑝.
• Bob calculates 𝐾 = (𝑅1)𝑦𝑚𝑜𝑑𝑝.
Block cipher overview
Key exchange algorithm
𝑲 = (𝒈𝒙 𝒎𝒐𝒅 𝒑)𝒚 𝒎𝒐𝒅 𝒑 = (𝒈𝒚 𝒎𝒐𝒅 𝒑)𝒙 𝒎𝒐𝒅 𝒑 = 𝒈𝒙𝒚𝒎𝒐𝒅 𝒑

## Page 94

94
⚫ Diffie-Hellman key exchange consensus
- Bob's calculation result : 𝐾 = (𝑅1)𝑦𝑚𝑜𝑑𝑝 = 𝑔𝑥 𝑚𝑜𝑑𝑝)𝑦 𝑚𝑜𝑑𝑝 = 𝑔𝑥𝑦𝑚𝑜𝑑𝑝
- Alice's calculation result : 𝐾 = (𝑅2)x𝑚𝑜𝑑𝑝 = 𝑔𝑦 𝑚𝑜𝑑𝑝)𝑥 𝑚𝑜𝑑𝑝 = 𝑔𝑥𝑦𝑚𝑜𝑑𝑝
- Alice doesn't know the value of 𝑦 and Bob of 𝑥, but they both get the same 𝐾.
Block cipher overview
Key exchange algorithm
Alice Bob
𝑹𝟏 = 𝒈𝒙𝒎𝒐𝒅 𝒑1
2 𝑹𝟏
𝑹𝟐 = 𝒈𝒚𝒎𝒐𝒅 𝒑 3
4𝑹𝟐
𝑲 = (𝑹𝟐)𝒙𝒎𝒐𝒅 𝒑 𝑲 = (𝑹𝟏)𝒚𝒎𝒐𝒅 𝒑
Shared Secret Key
5 6
𝑲 = 𝒈𝒙𝒚𝒎𝒐𝒅 𝒑
In the Diffie-Hellman method, the symmetric key is 𝑲 = 𝒈𝒙𝒚𝒎𝒐𝒅 𝒑

## Page 95

95
⚫ Diffie-Hellman key exchange consensus
- For example, find 𝐾 when 𝑔 = 7, 𝑝 = 23 (calculate with small numbers).
• Alice selects 𝑥 = 3 and calculates 𝑅1 = 73𝑚𝑜𝑑23 = 21.
• Bob selects 𝑦 = 6 and calculates 𝑅2 = 76𝑚𝑜𝑑23 = 4.
• Alice sends to Bob 21.
• Bob sends to Alice 4.
• Alice computes the symmetric key 𝐾 = 43𝑚𝑜𝑑23 = 18.
• Bob computes the symmetric key 𝐾 = 216𝑚𝑜𝑑23 = 18.
• Alice and Bob each receive 𝐾 and see the same value of 18 for both Alice and Bob.
▪ 𝑔𝑥𝑦𝑚𝑜𝑑𝑝 = 718𝑚𝑜𝑑23 = 18
Block cipher overview
Key exchange algorithm

## Page 96

96
Block ciphers : operation modes
⚫ Features
Method for solving the problem of how to
enforce a cipher when the length of the
plaintext is greater than the block size.
- Use both the block operating mode and
the cryptographic algorithm.
• E.g., implementing IPSec encapsulated
secure payloads using AES-CTR RFC :
https://tools.ietf.org/html/rfc3686
- Block operating mode is not only used for
block ciphers.
• It is used for block ciphers, stream
ciphers, hash functions, and more.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Block operation mode

## Page 97

97
Block ciphers : operation modes
⚫ Understanding padding
- In cryptography, padding is the addition of data at the beginning, middle, or end of plaintext
when encrypting it.
• It is used to correct incorrectly sized blocks when plaintext is divided into blocks.
- Types of padding
• Bit padding
▪ Start with bit 1 and fill it with bit 0 (e.g., 100...)
• Byte padding
▪ Fill specific bytes according to a specified rule
− ANSI x9.23, ISO 10126, PKCS#5 and PKCS#7, ISO/IEC 7816-4
• Zero padding
▪ Fill with bit 0 (e.g., 000...)
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Block operation mode

## Page 98

98
Block ciphers : operation modes
⚫ Error propagation
- Refers to whether or not one block affects other blocks when it fails.
• Claimed to be manipulable by malicious users through error multiplication
- This property was discussed until it evolved into message authentication codes and
authenticated encryption.
• Because it validates whether the message is corrupt or not.
⚫ Parallel implementation
- Refers to whether or not each block can be decrypted in isolation.
• Has a significant impact on performance metrics
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Block operation mode

## Page 99

99
Block ciphers : operation modes
⚫ Block operation modes
- Common operating modes
• Electronic Codebook (ECB)
• Cipher Block Chaining (CBC)
• Propagating Cipher Block Chaining (PCBC)
- Operation modes converted to stream ciphers
• Cipher Feedback (CFB)
• Output Feedback (OFB)
• Counter (CTR)
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Types of block operation modes

## Page 100

100
Block ciphers : operation modes
⚫ Authentication uses the following message block.
- Message Authentication Code (MAC)
- Authenticated Encryption (AE)
• Authenticated Encryption with Associated Data (AEAD)
• Encrypt-then-MAC (EtM)
• Encrypt-and-MAC (E&M)
• MAC-then-Encrypt (MtE)
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Types of block operation modes

## Page 101

101
Block ciphers : operation modes
⚫ Electronic Codebook (ECB)
- Encrypt plaintext blocks without any algorithm
- Not used because it's simple and has weaknesses
- Relationship between plaintext and ciphertext
• Encryption : 𝐶𝑖 = 𝐸𝑘(𝑃𝑖), Decryption : 𝑃𝑖 = 𝐷𝑘(𝐶𝑖)
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Electronic codebook
Plaintext #1
Encryption
System
Ciphertext #1
Key
Plaintext #2
Encryption
System
Ciphertext #2
Key
Plaintext #3
Encryption
System
Ciphertext #3
Key

## Page 102

102
Block ciphers : operation modes
⚫ Electronic Codebook (ECB)
- Decryption is done in reverse order because it uses a symmetric key.
- Error propagation
• An error in one block will only propagate to related blocks because each operates separately.
• However, even if Ciphertext #2 is partiallydamaged, Plaintext #2 will be completelydamaged.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Electronic codebook
Ciphertext #1
Decryption
System
Plaintext #1
Key
Ciphertext #2
Decryption
System
Plaintext #2
Key
Ciphertext #3
Decryption
System
Plaintext #3
Key
damaged
damaged

## Page 103

103
Block ciphers : operation modes
⚫ Cipher-Block Chaining (CBC)
- XOR the Initialization Vector (IV) in the first block and the ciphertext in the next block.
• IVs can be predefined and kept secret, or they can be made public
▪ However, the IV must not be modulated, and modulation will change the bit values in
the first block.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Crypto blockchain
Plaintext #1
Encryption
System
Ciphertext #1
Key
IV
Plaintext #2
Encryption
System
Ciphertext #2
Key
Plaintext #3
Encryption
System
Ciphertext #3
Key
Use padding when block
size is insufficient

## Page 104

104
Block ciphers : operation modes
⚫ Cipher-Block Chaining (CBC)
- Decryption is done in reverse order because it uses a symmetric key.
- Error propagation : an error propagates to the corresponding block in the broken ciphertext
and the even plaintext of the next block.
• However, if Ciphertext #2 is partially damaged, Plaintext #2 will be completely damaged,
but Plaintext #3, which performs the XOR operation, will be partially damaged.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Crypto blockchain
Ciphertext #1
Decryption
System
Plaintext #1
Key
IV
Ciphertext #2
Decryption
System
Plaintext #2
Key
Ciphertext #3
Decryption
System
Plaintext #3
Key
damageddamaged
damaged

## Page 105

105
Block ciphers : operation modes
⚫ Propagating Cipher Block Chaining (PCBC)
- The method of using the initial vector for the first block is the same as in CBC mode.
- Blocks from the second on are used to create the next ciphertext, which includes not only
ciphertext but also plaintext.
- The value of the XOR operation of ciphertext and plaintext
is XORed when encrypting the next block of plaintext.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Proliferative crypto blockchain
Plaintext #1
Encryption
System
Ciphertext #1
Key
IV
Plaintext #2
Encryption
System
Ciphertext #2
Key
Plaintext #3
Encryption
System
Ciphertext #3
Key
Use padding when block
size is insufficient

## Page 106

106
Block ciphers : operation modes
⚫ Propagating Cipher Block Chaining (PCBC)
- Decryption is done in reverse order because it uses a symmetric key.
- Error propagation : an error propagates to the corresponding block in the broken ciphertext
and the even plaintext of the next block.
• However, even if Ciphertext #2 is partially damaged, Plaintext #2 and Plaintext #3 will be
completely damaged.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Proliferative crypto blockchain
Ciphertext #1
Decryption
System
Plaintext #1
Key
IV
Ciphertext #2
Decryption
System
Plaintext #2
Key
Ciphertext #3
Decryption
System
Plaintext #3
Key
damaged
damaged damaged

## Page 107

107
Block ciphers : operation modes
⚫ Cipher Feedback (CFB)
- CBC variant that classifies block ciphers as self-synchronous stream ciphers
- Characterized by feeding the generated cipher into the next cryptosystem
• Consider input to a cryptosystem as feedback (cipher feedback from feeding back a cipher)
- Encrypted use of initialization vectors (IVs)
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Cipher feedback
Encryption
System
C #1
Key
bits
P #1
IV
T1
r bits
Encryption
System
C #2
bits
P #2
T2
r bits
Key Encryption
System
C #3
bits
P #3
T3
r bits
Key

## Page 108

108
Block ciphers : operation modes
⚫ Cipher Feedback (CFB)
- Decryption is done in reverse order because it uses a symmetric key.
- Error propagation : an error propagates to the corresponding block in the broken ciphertext
and the even plaintext of the next block.
• Yet, if part of Ciphertext #2 is damaged, it will perform an XOR operation with Plaintext #2,
resulting in partial damaged of Plaintext #2 and complete damaged of Plaintext #3.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Cipher feedback
Encryption
SystemKey
bitsIV
T1
r bits
P #1C #1
Encryption
SystemKey
bits
T2
r bits
P #2C #2
Encryption
SystemKey
bits
T3
r bits
P #3C #3
damaged damaged damaged

## Page 109

109
Block ciphers : operation modes
⚫ Output Feedback (OFB)
- Similar to CFB mode, but different input to the cryptographic algorithm
• Consider the input to a cryptosystem as feedback (output feedback from feeding the
output)
- Use the output of the cryptosystem to generate another block cipher before XORing it with
plaintext.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Output feedback
Encryption
System
C #1
Key
bits
P #1
IV
T1
r bits
Encryption
System
C #3
Key
bits
P #3
T3
r bits
Encryption
System
C #2
Key
bits
P #2
T2
r bits

## Page 110

110
Block ciphers : operation modes
⚫ Output Feedback (OFB)
- Decryption is done in reverse order because it uses a symmetric key.
- Error propagation: an error propagates to a block that is related to its own block, because
each block operates independently.
• However, if Ciphertext #2 is partially damaged, Plaintext #2 will also be partially damaged.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Output feedback
Encryption
System
P #1
Key
bits
C #1
IV
T1
r bits
Encryption
System
P #3
Key
bits
C #3
T3
r bits
Encryption
System
P #2
Key
bits
C #2
T2
r bits
damaged damaged

## Page 111

111
Block ciphers : operation modes
⚫ CTR (Counter)
- Applying the CTR operation mode to a block cipher algorithm converts it to a stream cipher.
- Proposed by Diffie and Hellman in 1979
- Encrypt a counter with IV incremented by 1.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Counter (CTR)
Encryption
System
Ciphertext #1
Key
CTR
Encryption
System
Ciphertext #2
Key Encryption
System
Ciphertext #3
Key
Plaintext #1 Plaintext #2 Plaintext #3
CTR+1 CTR+2
3AC4F.. ..0000 3AC4F.. ..0001 3AC4F.. ..0002

## Page 112

112
Block ciphers : operation modes
⚫ CTR (Counter)
- A combination of a randomvalueIV that can only be used once and a nonce used as a counting
- Error propagation: an error propagates to a block that is related to its own block, because
each block operates independently.
• Yet, if Ciphertext #2 is partially damaged, Plaintext #2 will also be partially damaged.
A block cipher is a method of encrypting a long plaintext by dividing it into blocks of a certain
length and encrypting them block by block. The problem of how to apply the cipher when the
length of the plaintext is greater than the block size gives rise to various block operating modes.
Counter (CTR)
Decryption
System
Plaintext #1
Key
CTR
Decryption
System
Plaintext #2
Key Decryption
System
Plaintext #3
Key
Ciphertext
#1
Ciphertext
#2
Ciphertext
#3
CTR+1 CTR+2
3AC4F.. ..0000 3AC4F.. ..0001 3AC4F.. ..0002
Nonce
IV
damaged
damaged

## Page 113

113
⚫ Comparing block operation modes
Block ciphers : operation modes
Block cipher
Mode Advantage Disadvantage Application Remark
ECB
• Simple and fast
processing
• Enables parallel
encryption/decryption
• Resistant to error
propagation
• Plaintexts produce
identical ciphertexts.
• Can manipulate
ciphertext
• Encrypted
transmission of short
phrases, such as
encryption keys
Not
recommended
for use
CBC
• Repetition in plaintext is
not reflected in
ciphertext.
• Only decryption can be
parallelized.
• Can decrypt random
blocks of ciphertext
• Encryption cannot be
parallelized.
• Vulnerable to error
propagation
• Universal block
cipher
• Authentication
Recommended
CFB
• No padding required
• Only decryption can be
parallelized.
• Can decrypt random
blocks of ciphertext
• Encryption cannot be
parallelized.
• Replaying attacks is
possible
• Vulnerable to error
propagation
• Universal block
cipher
• Authentication
Replaced to
CTR

## Page 114

114
⚫ Comparing block operation modes
Block ciphers : operation modes
Block cipher
Mode Advantage Disadvantage Application Remark
OFB
• No padding required
• Can be pre-configured for
encryption/decryption
• Encryption/decryption
are identical.
• Resistant to error
propagation
• Unable to parallelize
• If an active attacker bit-
reverses a block of
ciphertext, the
corresponding plaintext
block is bit-reversed.
• Transmitting noisy
streams (e.g., satellite
communications)
Replaced to
CTR
CTR
• No padding required
• Encryption/decryption
can be prepared in
advance.
• Encryption/decryption
are identical.
• Resistant to error
propagation
• Enables parallel
encryption/decryption
• If an active attacker bit-
reverses a block of
ciphertext, the
corresponding plaintext
block is bit-reversed.
• Universal block-
oriented transport
• High-speed
encryption processing
Recommended

## Page 115

115
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- Developed by IBM
• Symmetric-key cipher, a modification of the Lucifer cipher system
- Adopted as a US federal standard in 1977 (published as a draft in 1975)
• Used as the standard until 1997
- Use 64-bit blocks, 56-bit keys
• Split and use a 64-bit block in 32 bits
• 8 bits of the 64-bit key are used for parity checking
▪ Use 56 bits to generate the 48-bit key in actual use
▪ 48-bit keys are called round keys
- Provided a starting point for block cipher research
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years. However, it has been gradually replaced by the AES block cipher algorithm due to
bit size limitations caused by advances in computer performance. As a workaround, 3-DES, which
uses DES three times, is recommended.
DES block cipher algorithm
DES
cipher
DES
cipher
Encryption
Decryption
Plaintext (64bit)
Ciphertext (64bit)
Plaintext (64bit)
Ciphertext (64bit)
Key(56bit)

## Page 116

116
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- Since DES was created, there has been a security debate about two things.
• The key size is too small at 56 bits, which is a security risk.
• There has been a debate over the existence of trapdoors in S-boxes.
▪ Trapdoor - an intentional implementation of a feature that allows users to look through
plaintext
- Differential cryptanalysis was published in 1990, proving that attacks are possible.
• S-boxes were configured for differential attack at the time of DES design.
- Proposed 56-bit key exhaustive enumeration research by RSA company
• Decryption engine discovered in 1998.
- Uses triple DES (3-DES) with extended key length for security
• Promoted gradual migration to AES ciphers
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years. However, it has been gradually replaced by the AES block cipher algorithm due to
bit size limitations caused by advances in computer performance. As a workaround, 3-DES, which
uses DES three times, is recommended.
DES block cipher algorithm

## Page 117

117
Block ciphers : DES, 3DES, AES
⚫ DES overall structure
64bit Plaintext
Round 1
L0
F
R0
Initial Permutation
Encryption
⋯
L16
F
Final Permutation
R16
64bit Ciphertext
Round 16
64bit Plaintext
Final Permutation
Decryption
⋯
Initial Permutation
64bit Ciphertext
Round
1
R16
F
L16
R0
F
L0
Round 16
𝐾16
𝐾1
⋯

## Page 118

118
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Initial and final substitutions
• Each substitution takes 64 bits of input and rearranges them according to predefined rules.
• Has 64 input ports and corresponding output ports
• Initial and final substitutions are inversely related to each other.
• Keyless simple substitution
 1 2 8 25 40 58 64
1 2 8 25 40 58 64
1 2 8 25 40 58 64
1 2 8 25 40 58 64
16 Rounds
Initial
Permutation
Final
Permutation

## Page 119

119
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Initial and final substitutions
• Initial/final substitution table
▪ The 1st input of the initial substitution is the 40th output, and the 58th input of the final
substitution is the 55th output.
• The initial substitution and the final substitution are fixed functions that are independent
of the value of the key.
• It is not clear why these two substitutions are included in DES, and the design logic is not
publicly available.
Initial Permutation
58 50 42 34 26 18 10 2
60 52 44 36 28 20 12 4
62 54 46 38 30 22 14 6
64 56 48 40 32 24 16 8
57 49 41 33 25 17 9 1
59 51 43 35 27 19 11 3
61 53 45 37 29 21 13 5
63 55 47 39 31 23 15 7
Final Permutation
40 8 48 16 56 24 64 32
39 7 47 15 55 23 63 31
38 6 46 14 54 22 62 30
37 5 45 13 53 21 61 29
36 4 44 12 52 20 60 28
35 3 43 11 51 19 59 27
34 2 42 10 50 18 58 26
33 1 41 9 49 17 57 25

## Page 120

120
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- Feistel structure
• Principle of the F function
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years, but has been gradually replaced by the AES block cipher algorithm due to bit size
limitations caused by advances in computer performance. As a workaround, we recommend
3-DES, which uses DES three times.
DES block cipher algorithm
Round Key (48bit)
In
S1 S2 S3 S4 S5 S6 S7 S8
32bits
Extension D-box
48bits
L1 R1
L2 R2
Plaintext
Ciphertext
32bits
Round
F
MixerSwapper
Round
Key 48bits
Straight D-box
32bits
Out
8 S-boxies
...
section 1 section 2 section 3 section 8
From bit 32 From bit 1
Extension D-box
S-Box 1 S-Box 2 S-Box 3 ... S-Box 8
8 S-boxies

## Page 121

121
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- DES uses 16 rounds.
• Each round is a Feistel cipher.
• Each round contains two cipher elements.
▪ Mixer
− 32 bits on the right are XORed with the key.
▪ Swapper
− The left 32 bits swap places with the right 32 bits.
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years, but has been gradually replaced by the AES block cipher algorithm due to bit size
limitations caused by advances in computer performance. As a workaround, we recommend
3-DES, which uses DES three times.
DES block cipher algorithm
L1 R1
L2 R2
32bits
Round
𝑓(𝑅𝐼−1, 𝐾𝐼)
MixerSwapper
32bits
32bits 32bits

## Page 122

122
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Apply a 48-bit key to the 32 bits on the right to yield a 32-bit output value
- Organization of DES functions
• Expansion P-box
• Key XOR
• 8 S-boxes
• Simple P-box
In
32 bits
Expansion P-box
48 bits
KI
(48 bits)
48 bits
s s s s s s s s
32 bits
Straight P-box
32 bits
Out
⨍(RI−1, KI)
S-Boxes
XOR

## Page 123

123
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Expansion P-box
• The input value, which is 32 bits, but because the key is 48 bits, is expanded to 48 bits.
• The number of output ports is 48, but their value can be any value from 1 to 32.
• Some bits of the input value affect the value of one or more output bits.
From bit 32 32-bit input
48-bit output

## Page 124

124
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Expansion P-box table
- XOR
• XOR round-keys with the expanded right 48 bits after expansion and substitution.
• Round keys are used in this operation.
32 1 2 3 4 5
4 5 6 7 8 9
8 9 10 11 12 13
12 13 14 15 16 17
16 17 18 19 20 21
20 21 22 23 24 25
24 25 26 27 28 29
28 29 30 31 32 1

## Page 125

125
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- S-box calculations
• Perform 1 S-box operation of 110110 - different table values per box
▪ Find rows : extract first 1 bit (1) and last bit (0) -> 10(2) = 2
▪ Find columns : convert the remaining 4 bits to decimal
-> 1011(2) = 11
- 8 S-boxes each have a different table.
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years, but has been gradually replaced by the AES block cipher algorithm due to bit size
limitations caused by advances in computer performance. As a workaround, we recommend
3-DES, which uses DES three times.
DES block cipher algorithm
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
0 14 04 13 01 02 15 11 08 03 10 06 12 05 09 00 07
1 00 15 07 04 14 02 13 10 03 06 12 11 09 05 03 08
2 04 01 14 08 13 06 02 11 15 12 09 07 03 10 05 00
3 15 12 08 02 04 09 01 07 05 11 03 14 10 00 06 13
S-Box 1 table 48-bit input
S-Box 1 S-Box 2 S-Box 3 ... S-Box 8
8 S-boxes

## Page 126

126
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- Straight P-box (simple substitution)
• Simple substitution table
• Last operation in DES
• Has 32 bits of input and 32 bits of output
• Follows the same rules as the previous initial/final substitution table
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years, but has been gradually replaced by the AES block cipher algorithm due to bit size
limitations caused by advances in computer performance. As a workaround, we recommend
3-DES, which uses DES three times.
DES block cipher algorithm
16 7 20 21 29 12 28 17
1 15 23 26 5 18 31 10
2 8 24 14 32 27 3 9
19 13 30 6 22 11 4 25

## Page 127

127
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- Key generation algorithm
• Round key generator generates 16 48-bit round keys
from a 56-bit encryption key.
• 64 bits become 56 bits when the first 8-bit parity is removed.
• In DES, rounds 1, 2, 9, and 16 proceed with a 1-bit shift left
• The other rounds proceed with a 2-bit shift left.
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years, but has been gradually replaced by the AES block cipher algorithm due to bit size
limitations caused by advances in computer performance. As a workaround, we recommend
3-DES, which uses DES three times.
DES block cipher algorithm
Parity bit drop
Key(64 bits)
Shift Left Shift Left
28bits 28bits
Compression D-box
Cipher Key (56 bits)
48bits
Shift Left Shift Left
Compression D-box
48bits
⋯
⋯

## Page 128

128
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Key generation algorithm
• The pre-processing before key expansion is a shrink substitution that removes the parity
bit.
• Drop parity bits (8, 16, ..., 64) in a 64-bit key.
• Remove parity and replace the remaining bits.
• Table with parity bits removed
57 49 41 33 25 17 9 1
58 50 42 34 26 18 10 2
59 51 43 35 27 19 11 3
60 52 44 36 63 55 46 39
31 23 15 7 62 54 46 38
30 22 14 6 61 53 45 37
29 21 13 5 28 20 12 4

## Page 129

129
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Key generation algorithm
• Cyclic left move
▪ Key is split into two parts of 28 bits each after simple substitution.
▪ Each part is cyclically shifted 1 or 2 bits to the left.
− Rounds 1, 2, 9, and 16 have a cyclic shift bit amount of 1 bit, and the rest have 2 bits.
▪ The divided parts are combined to form 56 bits.
▪ It is unclear why only a fraction of the shifted bits are 1 bit.
▪ The cyclic shift bit amount
Rounds 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Bit shifts 1 1 2 2 2 2 2 2 1 2 2 2 2 2 2 1

## Page 130

130
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- Key generation algorithm
• Collapsed substitution
▪ Used to convert 56 bits to 48 bits
▪ 48-bit output value is used as round key for one round.
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years, but has been gradually replaced by the AES block cipher algorithm due to bit size
limitations caused by advances in computer performance. As a workaround, we recommend
3-DES, which uses DES three times.
DES block cipher algorithm
14 17 11 24 1 5 3 28
15 6 21 10 23 19 12 4
26 8 16 7 27 20 13 2
41 52 31 37 47 55 30 40
51 45 33 48 44 49 39 56
34 53 46 42 50 36 29 32

## Page 131

131
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Repeat until Round 16
L1 R1
L2 R2
Plaintext
Round 1
 F
MixerSwapper
L3 R3
Round 2
 F
MixerSwapper
Parity bit drop
Key
64bits
Shift Left Shift Left
56bits
28bits 28bits
Compression D-box
Shift Left Shift Left
Cipher Key
Round 1 Key
Compression D-box
Shift Left Shift Left
Round 2 Key
...
48bits
48bits
...

## Page 132

132
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- Properties
• No statistical correlation exists between plaintext, key, and ciphertext
• All bits of plaintext and key participate in determining every bit of ciphertext
• Small changes in plaintext or key cause large changes in ciphertext
▪ Avalanche effect - also known as the landslide effect
• Completeness effect
▪ Each bit of the ciphertext means that it needs to rely on many bits of the plaintext.
▪ Diffusion and chaos caused by P-boxes and S-boxes in DES show very strong
completeness effects.
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years, but has been gradually replaced by the AES block cipher algorithm due to bit size
limitations caused by advances in computer performance. As a workaround, we recommend
3-DES, which uses DES three times.
DES block cipher algorithm

## Page 133

133
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- Properties
• Complementation property
▪ Let C be the ciphertext corresponding to a plaintext P and a key K. If P and K are
complementary, then the corresponding ciphertext C is also complementary.
− ҧ𝐶 = 𝐸𝐾(𝑃), ҧ𝐶 = 𝐸 ഥ𝐾 ത𝑃
− Since the complementation property is XORed with the key and plaintext in the
rounding function, if both the key and plaintext are complementary, they are
canceled out by the XOR operation and output the same value as if they were not
complementary in the first place.
− The complementation property can optimize the operation of 255 exhaustive key
searches using two known plaintexts (known-plaintext attack).
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years, but has been gradually replaced by the AES block cipher algorithm due to bit size
limitations caused by advances in computer performance. As a workaround, we recommend
3-DES, which uses DES three times.
DES block cipher algorithm

## Page 134

134
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- Properties
• Weak keys, semi-weak keys, and possible weak keys
▪ Weak keys
− Keys in a cipher that can be easily decrypted by certain operations.
− The type and nature of weak keys depend on the structure of the cipher, and if a weak
key exists in the cipher, it should be avoided.
▪ Weak keys in DES
− Assuming that the 16 round keys are K1, K2, ..., K16, where K1 = K16, K2 = K15 , ..., K8 =
K9 , the encryption process and decryption process match
− 𝐸𝐾 𝐸𝐾 𝑃 = 𝑃
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years, but has been gradually replaced by the AES block cipher algorithm due to bit size
limitations caused by advances in computer performance. As a workaround, we recommend
3-DES, which uses DES three times.
DES block cipher algorithm

## Page 135

135
Block ciphers : DES, 3DES, AES
⚫ Lucifer / DES
- Properties
• Weak keys, semi-weak keys, and possible weak keys
▪ Semi-weak keys
− If there are weak-key-like properties between two keys K and K’.
− DES does not become a group (if it did, it would be decrypted by a birthday attack with
a computation of 228 )
− 𝐸𝐾 𝐸𝐾′ 𝑃 = 𝑃
▪ Possible weak keys
− There are 48 possible weak keys that generate only four different round keys.
The DES block cipher algorithm was adopted as a standard in 1977 and has been in use for more
than 20 years, but has been gradually replaced by the AES block cipher algorithm due to bit size
limitations caused by advances in computer performance. As a workaround, we recommend
3-DES, which uses DES three times.
DES block cipher algorithm

## Page 136

136
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Multiple DES
• The main criticism of DES is its short key length.
▪ The first solution
− Abandon DES and design a new algorithm. E.g., AES
▪ The second solution
− Operate multiple encryptions of DES with multiple keys
− If DES is assumed to be a group, then using 2 keys 𝑘1, 𝑘2 makes no sense.
− For DES to be a group, it must satisfy log2 264! ≈ 270, but the key length of DES is
only 56 bits, which makes it impossible to be a group.
− Since DES is not a group, it is very difficult to find one that satisfies the following:
𝐸𝑘2 𝐸𝑘1 𝑃 = 𝐸𝑘3(𝑃)
− This means that double or triple DES can be used.

## Page 137

137
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Double DES
• Use two DES encryption algorithms for encryption and two decryption algorithms for
decryption
• Use different keys for each DES
• Double the key size to 112 bits, but still vulnerable to known plaintext attacks
- Meet-in-the-Middle Attack
• Double DES seems to increase the number
of key searches from 256 to 2112, but the
meet-in-the-middle attack keeps it at 257,
with only a slight improvement.
• In double DES, the middle text values of
the first encryption and the description
match.

## Page 138

138
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Triple DES
• Triple DES with two keys
▪ Use 𝑘1 for the first and third and 𝑘2 for the second
▪ Use decryption algorithm in the middle of the encryption process
▪ Triple DES with two keys is vulnerable to known-plaintext attacks, but stronger than
double DES.

## Page 139

139
Block ciphers : DES, 3DES, AES
DES block cipher algorithm
⚫ Lucifer / DES
- Triple DES
• Triple DES with three keys
▪ Because of the potential for known-plaintext attacks against two-key triple DES, some
programs use three-key Triple DES.
▪ Use the DES cryptographic algorithm three times for encryption and three times for
decryption
▪ But must be compatible with DES using the algorithm once
− The encryption process follows the EDE (Encryption/Decryption/Encryption) sequence.
− The decryption process follows the DED (Decryption/Encryption/Decryption) sequence.

## Page 140

140
Block ciphers : DES, 3DES, AES
⚫ Rijndael / AES
- 1997-01-02 : basic requirements for AES presented.
• Use block cipher algorithm.
• Key length is 128, 192, or 256 bits.
• Block size is 128 bits.
• Must be available for smart cards.
• Must be patent-free (royalty-free).
- 1997-09-12 : the US NIST officially called for AES candidates.
- 1998-08-20 : 15 first round AES candidate algorithms announced.
- 1999-08-09 : 5 second round AES candidate algorithms announced
(Rijndael, MARRS, RC6, SERPENT, and TWOFISH).
- 2000-10-02 : Rijndael was selected as AES.
- 2001-12-06 : officially registered and released to the public.
A symmetric key, also known as a secret key, means that the encryption key is the same as the
decryption key.
AES block cipher algorithm

## Page 141

141
Block ciphers : DES, 3DES, AES
⚫ Rijndael / AES
- Features
• Use SPN structure instead of Feistel
• Smart card use was the requirement, but designed to include software, hardware, etc.
• Support for block sizes of 192 and 256 bits as well as 128 bits
• Number of rounds (performance and reliability) depends on key length.
• 128 bits = 2128 = 3.4 x 1038
▪ A computer computing 2^55 keys (56 bits) per second would take 149 billion years to
break Rijndael using a brute force attack.
A symmetric key, also known as a secret key, means that the encryption key is the same as the
decryption key.
AES block cipher algorithm
Key length Block size Number of rounds
AES-128 4 4 10
AES-192 6 4 12
AES-256 8 4 14

## Page 142

142
Block ciphers : DES, 3DES, AES
⚫ Rijndael / AES
- Features
• Each round (except the last) operates uniformly with the following elements.
▪ These elements are called layers.
− SubBytes (byte-by-byte substitution using an S-box)
− ShiftRows (a permutation that cyclically shifts the last three rows in the state)
− MixColumns (substitution using Galois Fields, corps de Galois, GF(28) arithmetic)
− Add round key (bit-by-bit XOR with an expanded key)
▪ Rounds except the last : ByteSub → ShiftRow → MixColumn → Key XOR
▪ Last round : ByteSub → ShiftRow → Key XOR
A symmetric key, also known as a secret key, means that the encryption key is the same as the
decryption key.
AES block cipher algorithm
Source: https://www.lri.fr/~fmartignon/documenti/systemesecurite/5-AES.pdf

## Page 143

143
Block ciphers : DES, 3DES, AES
⚫ Rijndael / AES
- SubBytes (byte-by-byte substitution using an S-box)
• Unlike DES, AES uses the same S-box
▪ Responsiblefor the cipher’schaoticnature
• Use 28 as a Galois Field
▪ Finite field - a set with a finite number
of elements.
• Split 8 bits into 4 bits
▪ Leading 4 bits are rows,
trailing 4 bits are columns
▪ E.g., 0x8A → row 8 and column A → 0x7E
A symmetric key, also known as a secret key, means that the encryption key is the same as the
decryption key.
AES block cipher algorithm
AES Sub Bytes Table
0 1 2 3 4 5 6 7 8 9 A B C D E F
0 63 7C 77 7B F2 6B 6F C5 30 01 67 2B FE D7 AB 76
1 CA 82 C9 7D FA 59 47 F0 AD D4 A2 AF 9C A4 72 C0
2 B7 FD 93 26 36 3F F7 CC 34 A5 E5 F1 71 D8 31 15
3 04 C7 23 C3 18 96 05 9A 07 12 80 E2 EB 27 B2 75
4 09 83 3C 1A 1B 6E 5A A0 52 3B D6 B3 29 E3 2F 84
5 53 D1 00 ED 20 FC B1 5B 6A CB BE 39 4A 4C 58 CF
6 D0 EF AA FB 43 4D 33 85 45 F9 02 7F 50 3C 9F A8
7 51 A5 40 8F 92 9D 38 F5 BC B6 DA 21 10 FF F3 D2
8 CD 0C 03 EC 5F 97 44 17 C4 A7 7E 3D 64 5D 19 73
9 60 81 4F DC 22 2A 90 88 46 EE B8 14 DE 5E 0B DB
A E0 32 3A 0A 49 06 24 5C C2 D3 AC 62 91 95 E4 79
B E7 C8 37 6D 8D D5 4E A9 6C 56 F4 EA 65 7A AE 08
C BA 78 25 2E 1C A6 B4 C6 E8 DD 74 1F 4B BD 8B 8A
D 70 3E B5 66 48 03 F6 0E 61 35 57 B9 86 C1 1D 9E
E E1 F8 98 11 69 D9 8E 94 9B 1E 87 E9 CE 55 28 DF
F 8C A1 89 0D BF E6 42 68 41 99 2D 0F B0 54 BB 16

## Page 144

144
Block ciphers : DES, 3DES, AES
⚫ Rijndael / AES
- ShiftRows (a permutation that cyclically shifts the last three rows in the state)
• Organized in a 4x4 array because the block is 128 bits.
• Row 1 does not perform any shift operation.
• Shift to the left by the number of rows starting with the next row.
A symmetric key, also known as a secret key, means that the encryption key is the same as the
decryption key.
AES block cipher algorithm
a00 a01 a02 a03
a10 a11 a12 a13
a20 a21 a22 a23
a30 a31 a32 a33
a00 a01 a02 a03
a11 a12 a13 a10
a22 a23 a20 a21
a33 a30 a31 a32
Block Block with shifted rows

## Page 145

145
Block ciphers : DES, 3DES, AES
⚫ Rijndael / AES
- MixColumns (substitution that uses Galois Fields, corps de Galois, GF(28 ) arithmetic)
• Responsible for spreading ciphers
• Proceed to array operations
A symmetric key, also known as a secret key, means that the encryption key is the same as the
decryption key.
AES block cipher algorithm
a00 a01 a02 a03
a10 a11 a12 a13
a20 a21 a22 a23
a30 a31 a32 a33
b00 b01 b02 b03
b10 b11 b12 b13
b20 b21 b22 b23
b30 b31 b32 b33
02 03 01 01
01 02 03 01
01 01 02 03
03 01 01 02
MixColumn Block MixedColumn block

## Page 146

146
Block ciphers : DES, 3DES, AES
⚫ Rijndael / AES
- Add round key (bit-by-bit XOR with an expanded key)
• Perform an XOR operation on a block of data and a key.
• This operation is also performed on a matrix basis.
A symmetric key, also known as a secret key, means that the encryption key is the same as the
decryption key.
AES block cipher algorithm
a00 a01 a02 a03
a10 a11 a12 a13
a20 a21 a22 a23
a30 a31 a32 a33
c00 c01 c02 c03
c10 c11 c12 c13
c20 c21 c22 c23
c30 c31 c32 c33
k00 k01 k02 k03
k10 k11 k12 k13
k20 k21 k22 k23
k30 k31 k32 k33
Round key Block Cipher block

## Page 147

147
Block ciphers : DES, 3DES, AES
AES block cipher algorithm
⚫ Rijndael / AES
S-box #1 S-box #2 S-box #3
P-box #1
S-box #1 S-box #2 S-box #3
P-box #2
Plaintext
Ciphertext
(XOR) Key1
(XOR) Key2
(XOR) Key3
SubBytes
ShiftRows
Plaintext
Ciphertext
AddRoundKey
MixColumns
SPN block cipher structure AES algorithm
AddRoundKey
SubBytes
Main
Round
Initial
Round
Final
Round

## Page 148

148
Stream cipher
Stream ciphers generate a key stream of the same length as the plaintext, which is then
combined with the plaintext and the key binary sequence in a bitwise logical exclusive-or (XOR)
operation and proceed encryption.
Stream cipher
Plaintext byte
stream
Ciphertext byte
stream
Cipher byte
stream
Random
number
generator
Random
number
generator
Key

## Page 149

149
Stream cipher
⚫ Synchronous
⚫ Easy to create
⚫ No error propagation
⚫ Can detect insertions and deletions
⚫ Synchronization required
⚫ Require data authentication & integrity check
⚫ Require strong sequence
Stream ciphers generate a key stream of the same length as the plaintext, which is then
combined with the plaintext and the key binary sequence in a bitwise logical exclusive-or (XOR)
operation and proceed encryption.
Stream cipher
 Self-synchronous
 Limited error propagation
 Difficult to detect insertions and deletions
 Plaintext is diffused over ciphertext
 High resistance to eavesdropping
 Difficult to create
𝑓
ℎ𝑔
𝜎𝑙
𝑘
𝑚𝑖
𝐶𝑖
𝜎𝑙+1
𝑍𝑖
ℎ𝑔𝑘
𝑚𝑖
𝐶𝑖
𝑍𝑖
⋯

## Page 150

150
Stream cipher
⚫ Comparing stream ciphers with block ciphers
Stream ciphers generate a key stream of the same length as the plaintext, which is then
combined with the plaintext and the key binary sequence in a bitwise logical exclusive-or (XOR)
operation and proceed encryption.
Stream cipher
Stream cipher Block cipher
Can work with small chunks of plaintext Behave on large blocks of data
Faster than block ciphers Slower than stream ciphers
Implement with less code Implemented with a lot of code
Use secret key only once Repeatedly using passkeys
Example : One time pad Example : Data Encryption Standard (DES)
Well-known application : SSL Well-known application : databases, files
Better suited for hardware implementation Easy to implement in software
Stream
cipher
𝑥0𝑥1 ⋯ 𝑥𝑛 𝑦0𝑦1 ⋯ 𝑦𝑛
𝑘
Stream
cipher
𝑥𝑛
⋮
𝑥1
𝑥0
𝑘
𝑦𝑛
⋮
𝑦1
𝑦0

## Page 151

151
Stream cipher
⚫ Advantages of stream ciphers
- Use a random number generator
• Generate long-cycle binary sequences from short-length keys at low cost and high speed
- Enable real-time encryption
• Ideal for media and telecommunications environments
- Manipulating one bit of the ciphertext will only affect the decryption of that bit.
• Less vulnerable to communication errors than block ciphers
▪ Block ciphers can't be fully decrypted if one bit is tampered with.
- Allow mathematically rigorous analysis of the security of cryptosystems
- Ideal for protecting communication data, including telecommunications
Stream ciphers generate a key stream of the same length as the plaintext, which is then
combined with the plaintext and the key binary sequence in a bitwise logical exclusive-or (XOR)
operation and proceed encryption.
Stream cipher

## Page 152

152
Stream cipher
⚫ Security requirements for stream ciphers
- The security of a stream cipher depends on how resistant the key sequence is to various
types of cryptographic attacks.
- In general, Beker, Siegenthaler, and Golic meet the criteria listed below.
• Period : the output key sequence must have a guaranteed minimum value for the period
• Randomness : the output key sequence should have good randomness properties
• Linear complexity : the output key sequence must have a large linear complexity
• Correlation immunity : the output key sequence must have a high correlation immunity.
• Number of key stream cycles : the output key sequence must occur in at least one key
stream cycle
Stream ciphers generate a key stream of the same length as the plaintext, which is then
combined with the plaintext and the key binary sequence in a bitwise logical exclusive-or (XOR)
operation and proceed encryption.
Stream cipher

## Page 153

153
Stream cipher
⚫ Linear feedback shift registers
- Pseudorandom number generation function
• The use of LFSRs in stream ciphers is common.
• Random numbers generated by feedback
▪ Bits that influence the feedback are called tabs.
• Output is the bit that is discarded.
• Represent the underlying form as a seed
- Use linear functions
• Repeating operations at a given interval
• Use polynomials
• Typically operate as a logical exclusive-or (XOR)
Just as there are different types of block ciphers depending on their design, LFSR is a
representative design for stream ciphers.
Designing stream ciphers

## Page 154

154
Stream cipher
- Understanding how random number generation works with LFSR (4-bit)
• The number of all cases that can be generated with 4 bits minus one case (0000) is
generated (2𝑛 − 1).
- Types
• Fibonacci LFSR
• Galois LFSR
• Xorshift LFSR
Just as there are different types of block ciphers depending on their design, LFSR is a
representative design for stream ciphers.
Designing stream ciphers
1 1 0 0
0
0 1 1 0
1
1 0 1 1
0
0 1 0 1
1
Feedback
Output

## Page 155

155
Stream cipher
⚫ Fibonacci LFSR
- Also called external LFSR because the value is computed externally on the tab.
- In its most basic form
- E.g., as a tap, the role is responsible for bits 16, 14, 13, and 11.
• 𝑥16 + 𝑥14 + 𝑥13 + 𝑥11
Just as there are different types of block ciphers depending on their design, LFSR is a
representative design for stream ciphers.
LFSR
0 1 0 0 1 1 0 0 1 1 0 0 1 1 0 1
011
1 0 1 0 0 1 1 0 0 1 1 0 0 1 1 0
Feedback
Output
Seed
𝑥16
Operation
Result

## Page 156

156
Stream cipher
⚫ Galois LFSR
- Also called Internal LSFR because the value is computed internally on the tab.
- Designed to replace the existing Fibonacci LFSR – operates in reverse order.
- E.g., as a tap, the role is responsible for bits 16, 14, 13, and 11.
• 𝑥15 + 𝑥14 + 𝑥12 + 1
Just as there are different types of block ciphers depending on their design, LFSR is a
representative design for stream ciphers.
LFSR
1 0 1 1 0 0 1 1 0 0 1 1 0 0 1 0
0
Output
𝑥16 1 0
0 1 0 1 1 0 0 1 1 0 0 1 1 0 0 1
𝑥16
Operation
Result

## Page 157

Public-key
encryption
03
• Public-key encryption overview
• RSA
• ElGamal
• ECC

## Page 158

158
Public-key encryption overview
⚫ The encryption and decryption keys are different and is also known as public-key encryption
because some keys are public.
- Public key ≠ private key
- Use mathematical challenges to implement cryptosystems
An asymmetric-key cryptosystem means that the keys used for encryption and decryption are
different. These ciphers are created using diverse mathematical challenges.
Asymmetric encryption
Alice
Bob's public key
Encryption CiphertextPlaintext
Bob's private key
Bob
Insecure channel
Public key distribution channels
Key generation
procedure
Public
Decryption PlaintextCiphertext

## Page 159

159
Public-key encryption overview
⚫ Types
- Cryptosystems using a prime factorization problem
• A challenge that exploits the fact that the product of two given primes is easy, but finding the
two primes in the multiplied value is extremely difficult.
• Types - RSA, Rabin
• E.g., 89 ∗ 97 = 𝑋 8633 8633 = 𝑋 ∗ 𝑌
- Cryptosystems using a discrete algebra problem
• Discrete algebra problem : given a finite group 𝐺 and constructors 𝑔 and 𝑔𝑥,
find the exponential product 𝑥
• When 𝑦 = 𝑔𝑥𝑚𝑜𝑑𝑝, it's easy to calculate 𝒚 if you know 𝑔,𝑥,𝑝, but it's harder to find 𝑥 if you know
𝑦,𝑔,𝑝.
• That is, the difficulty of computing logarithms, which is the inverse of exponential computation
(𝑥 = 𝑙𝑜𝑔𝑔𝑦)
• Types - ElGamal, DSA, ECC
An asymmetric-key cryptosystem means that the keys used for encryption and decryption are
different. These ciphers are created using diverse mathematical challenges.
Asymmetric encryption

## Page 160

160
⚫ Symmetric -key and asymmetric -key ciphers are different . These differences are what
differentiate their purposes.
Public-key encryption overview
Symmetric-key vs. asymmetric-key ciphers
Division Symmetric-key cryptography Asymmetric-key cryptography
Key Symmetric key (secret key) Asymmetric key (public and private)
Encryption/decryption
key relationship Encryption key = decryption key Encryption key ≠ decryption key
Number of keys 𝑁 × (𝑁 − 1)/2 2 × 𝑁
Cipher method Symbol (character, bit) substitution Apply mathematical functions
Advantage Fast computation, multiple algorithms
No need to share private keys, easy to add
more communication destinations (public
key distribution)
Disadvantage Difficult in distributing and managing
keys Slow (exponential operations)
Well-known example DES, AES RSA
Cipher algorithm Secret/Public Public
Sending a secret key Required Not required
Security certification Hard Easy
Electronic signatures Complex Simple

## Page 161

161
⚫ Public-key cryptosystem developed in the US in 1978 by Rivest, Shamir and Adleman.
- The most popular public-key cryptosystems on the market today
- Use one-way trapdoor functions
• Given large prime numbers 𝑝 and 𝑞, it is easy to compute 𝑁 = 𝑝 × 𝑞, but difficult to find
large prime numbers 𝑝 and 𝑞 from the given 𝑁 - a mathematical challenge
- Use two exponents 𝑒 (public key) and 𝑑 (private key)
- Alice generates ciphertext C from plaintext P using 𝐶 = 𝑃𝑒𝑚𝑜𝑑𝑛.
- Bob obtains plaintext P from ciphertext C using 𝑃 = 𝐶𝑑𝑚𝑜𝑑𝑛.
- Modulo 𝑛 is generated by a very large number of key generation processes.
- The attacker must obtain
𝑒
𝐶 𝑚𝑜𝑑𝑛 for the attack
- Alic and Bob have polynomial complexity, while Eve faces exponential complexity.
RSA
Overview
Alice
𝑪 = 𝑷𝒆𝒎𝒐𝒅 𝒏
BobEve
𝑷 = 𝑪𝒅𝒎𝒐𝒅 𝒏𝑷 =
𝒆
𝑪 𝒎𝒐𝒅 𝒏
P P
C CC
?

## Page 162

162
RSA
RSA is a cryptosystem implemented using a mathematical challenge called prime factorization.
Block and stream ciphers are called symmetric-key ciphers because they encrypt and decrypt
using the same secret key, while RSA is called an asymmetric-key cipher because it encrypts and
decrypts using different secret keys.
Overview
(𝑒, 𝑛)
Private   (𝑑)
C: Ciphertext
Select 𝑝, 𝑞
𝑛 = 𝑝 × 𝑞
Select and 𝑒 and 𝑑
Decryption in
𝑅 =< 𝑍𝑛, +,×>
𝑮 =< 𝒁∅(𝒏) ∗,×>
𝑩𝒐𝒃
𝑃 = 𝐶𝑑𝑚𝑜𝑑 𝑛
Plaintext
P𝐶 = 𝑃𝑒𝑚𝑜𝑑 𝑛
𝑨𝒍𝒊𝒄𝒆
Plaintext
P
Encryption in
𝑅 =< 𝑍𝑛, +,×>
𝑒, 𝑛
To public

## Page 163

163
RSA
⚫ Two algebraic structures
- RSA uses two algebraic structures
• Encryption/decryption : a public circle
▪ Everyone knows the structure of this circle because N is public.
▪ Anyone can use this circle to encrypt and send to Bob.
• Key generation : a private group
▪ Perform multiplication and division only
▪ Use it to generate private and public keys
▪ Keep the private group secret
RSA is a cryptosystem implemented using a mathematical challenge called prime factorization.
Block and stream ciphers are called symmetric-key ciphers because they encrypt and decrypt
using the same secret key, while RSA is called an asymmetric-key cipher because it encrypts and
decrypts using different secret keys.
Overview
𝑹 =< 𝒁𝒏, +,×>
𝑹 =< 𝒁∅(𝒏) ∗,×>

## Page 164

164
RSA
⚫ How to generate keys
- Bob generates his public key (𝑒) and private key (𝑑) and declares the sequence pair (𝑒, 𝑛) as
his public key.
• 𝑛 = 𝑝 ∗ 𝑞
• ∅ 𝑛 = 𝑝 − 1 𝑞 − 1
• Choose 𝑒 that satisfies the condition that 1 < 𝑒 < ∅ 𝑛 , 𝑑 and ∅(𝑛) are disjoint.
• 𝑑 = 𝑒−1𝑚𝑜𝑑∅ 𝑛 , 𝑑 is an inverse element of 𝑒 𝑚𝑜𝑑∅ 𝑛 .
- Select two prime numbers 𝑝, 𝑞 with different values (each size is recommended to be 1024
bits for security).
• Each prime number has about 309 digits in decimal notation.
- Modulo 𝑛 is 2048 bits, which is about 618 digits in decimal notation.
- Discard 𝑝, 𝑞, ∅(𝑛) after generating the keys.
RSA is a cryptosystem implemented using a mathematical challenge called prime factorization.
Block and stream ciphers are called symmetric-key ciphers because they encrypt and decrypt
using the same secret key, while RSA is called an asymmetric-key cipher because it encrypts and
decrypts using different secret keys.
Overview

## Page 165

165
RSA
⚫ RSA proof
- If 𝑛 = 𝑝 ∗ 𝑞, 𝑎 < 𝑛 and 𝑘 is an integer, then 𝑎𝑘∗∅ 𝑛 +1 ≡ 𝑎(𝑚𝑜𝑑𝑛) is true.
- Plaintext when sent 𝑃
- Decrypted plain text 𝑃1
RSA is a cryptosystem implemented using a mathematical challenge called prime factorization.
Block and stream ciphers are called symmetric-key ciphers because they encrypt and decrypt
using the same secret key, while RSA is called an asymmetric-key cipher because it encrypts and
decrypts using different secret keys.
Overview
𝑷𝟏 = 𝑪𝒅𝒎𝒐𝒅 𝒏 = (𝑷𝒆𝒎𝒐𝒅 𝒏)𝒅𝒎𝒐𝒅 𝒏 =  𝑷𝒆𝒅𝒎𝒐𝒅 𝒏
𝒆𝒅 = 𝒌 ∗ ∅ 𝒏 + 𝟏
𝑷𝟏 = 𝑷𝒆𝒅𝒎𝒐𝒅 𝒏 →  𝑷𝟏 = 𝑷∅ 𝒏 +𝟏𝒎𝒐𝒅 𝒏
𝑷𝟏 = 𝑷𝒌∗∅ 𝒏 +𝟏𝒎𝒐𝒅 𝒏 = 𝒑 𝒎𝒐𝒅 𝒏

## Page 166

166
⚫ RSA example
- Bob selects as 𝑝 = 7, 𝑞 = 11, calculating with 𝑛 = 𝑞 ∗ 𝑝 = 7 ∗ 11 = 77.
- ∅ 𝑛 = 7 − 1 11 − 1 = 60
- Bob chooses two exponent 𝑒 and 𝑑 that belongs to 𝑍60
∗ (select 𝑒 = 13).
- If 𝑒 is 13, then 𝑑 becomes 37, which is an inverse element of 𝑒 (𝑒−1𝑚𝑜𝑑60 = 37).
- Alice (sender)
• Plaintext(𝑃) = 5
• 𝐶 = 513𝑚𝑜𝑑77 ≡ 26 𝑚𝑜𝑑77
• Ciphertext(𝐶) = 26
- Bob (recipient)
• Ciphertext(𝐶) = 26
• 𝑃 = 2637𝑚𝑜𝑑77 ≡ 5 𝑚𝑜𝑑77
• Plaintext(𝑃) = 5
RSA
Overview

## Page 167

167
RSA
RSA is a cryptosystem implemented using a mathematical challenge called prime factorization.
Block and stream ciphers are called symmetric-key ciphers because they encrypt and decrypt
using the same secret key, while RSA is called an asymmetric-key cipher because it encrypts and
decrypts using different secret keys.
Using RSA
Alice
Bob
2 Bob's public key
(register 𝑁 and 𝑒)
3 Obtain Bob's public key
(𝑁 and 𝑒)
4 𝐶 = Me 𝑚𝑜𝑑(𝑁)
5 Send 𝐶 to Bob
6
𝑀 = Cd 𝑚𝑜𝑑(𝑁)
1 Bob's private key
(Hold 𝑑)
Server with public-key safety authentication

## Page 168

168
RSA
⚫ Conditions for making RSA ciphers more secure
- Must not be factorizable by Fermat's method, Pollard Rho method, etc.
• 𝑝 and 𝑞 are not the same and have approximately the same size digits.
• 𝑝 − 1 and 𝑞 − 1 take large prime arguments, respectively.
• 𝑝 − 1 and 𝑞 − 1 must have a small greatest common divisor.
• 𝑝 and 𝑞 must be large enough (currently 2048 bits or larger is required).
RSA is a cryptosystem implemented using a mathematical challenge called prime factorization.
Block and stream ciphers are called symmetric-key ciphers because they encrypt and decrypt
using the same secret key, while RSA is called an asymmetric-key cipher because it encrypts and
decrypts using different secret keys.
Security of RSA

## Page 169

169
RSA
⚫ Conditions for making RSA ciphers more secure
- Conditions for other parameters
• The private key 𝑑 should be a moderately large number.
▪ It is usually chosen with max{𝑝, 𝑞} + 1 < 𝑑 < 𝑛 − 1.
• For efficiency reasons, choose the public key 𝑒 in 3, 17, 2𝑟 + 1 (small 𝑟), etc.
▪ Because it's an exponential operation, it uses a small number for efficiency.
▪ However, for reliability, 3, 5, 17, 257, and 65537 are often used.
− 21 + 1, 22 + 1, 24 + 1, 28 + 1, 216 + 1
▪ rfc4871 "Domain Keys Identified Mail (DKIM) Signatures"
− The e used in mail signatures is at least 65537 (216 + 1).
− Use larger values in special cases.
• Decryption is slower than encryption because 𝑑 is typically larger.
RSA is a cryptosystem implemented using a mathematical challenge called prime factorization.
Block and stream ciphers are called symmetric-key ciphers because they encrypt and decrypt
using the same secret key, while RSA is called an asymmetric-key cipher because it encrypts and
decrypts using different secret keys.
Security of RSA

## Page 170

170
RSA
Attacks on RSA
Potential attaks on
RSA
Factoring attacks
Chosen-
ciphertext attack
Encryption
exponent attacks
Decryption
exponent attacks
Plaintext attacks
Modulo attacks
Implementation
attacks
Coppersmith, Broadcast, Related Messages, Short pad
Revealed and low exponent
Short message, cyclic, unconcealed
Common modulus
Timing and power

## Page 171

171
⚫ Factoring attacks
- RSA has a large modulo value, making it impossible to perform prime factorization in a
reasonable amount of time.
- Bob chooses 𝑝 and 𝑞.
• He computes 𝑛 = 𝑝 × 𝑞 and makes 𝑛 public and 𝑝, 𝑞 private.
- If Eve can prime factorize 𝑛 to get 𝑝 and 𝑞,
• She can compute ∅ 𝑛 = (𝑝 − 1)(𝑞 − 1), which allows her to compute 𝑑 = 𝑒−1𝑚𝑜𝑑∅(𝑛) from
the public value 𝑒.
- Safety
• RSA requires that 𝑛 be at least 300 decimal digits long.
▪ The modulo value must be at least 1024 bits.
• The most recently recommended value is 2048 bits or higher (as of 2019).
RSA
Attacks on RSA

## Page 172

172
⚫ Chosen-ciphertext attacks
- Use the multiplicative properties of RSA.
- Suppose Bob decrypts a random ciphertext that is not the 𝐶 requested by Eve.
- Eve can intercept 𝐶 and obtain 𝑃 using the following procedure.
• Eve chooses a random integer𝑋 (𝑋 ∈ 𝑍𝑛
∗)
• She computes 𝑌 = 𝐶 × 𝑋𝑒𝑚𝑜𝑑𝑛.
• She then sends 𝑌 to Bob to decrypt and get 𝑍 = 𝑌𝑑𝑚𝑜𝑑𝑛.
RSA
Attacks on RSA
𝒁 = 𝒀𝒅𝒎𝒐𝒅 𝒏
     = (𝑪 × 𝑿𝒆)𝒅 𝒎𝒐𝒅 𝒏
     = 𝑪𝒅 × 𝑿𝒆𝒅  𝒎𝒐𝒅 𝒏
     = 𝑪𝒅 × 𝑿 𝒎𝒐𝒅 𝒏
     = 𝑷 × 𝑿 𝒎𝒐𝒅 𝒏
 𝒁 = 𝑷 × 𝑿 𝒎𝒐𝒅 𝒏
 ∴ 𝑷 = 𝒁 ×  𝑿−𝟏 𝒎𝒐𝒅 𝒏

## Page 173

173
⚫ Chosen-ciphertext attacks
- An example using the RSA formula from the previous page.
- 𝑝 = 7, 𝑞 = 11, 𝑒 = 13, 𝑑 = 37, 𝑃 = 5, 𝐶 = 26, 𝑛 = 77, ∅ 𝑛 = 60
- Eve selects a random integer 𝑋 that belongs to 𝑍77
∗ (where 𝑋 = 17, 𝑋−1 = 68).
- Eve computes 𝑌 = 𝐶 ∗ 𝑋𝑒 𝑚𝑜𝑑𝑛 (𝑌 = 26 ∗ 1713 𝑚𝑜𝑑77 = 50, ∴ 𝑌 = 50).
- Eve decrypts to get 𝑍 = 𝑌𝑑 𝑚𝑜𝑑𝑛 𝑍 = 5037 𝑚𝑜𝑑77 = 8, ∴ 𝑍 = 8 .
- She calculates 𝑃 using 𝑃 = 𝑍 × 𝑋−1 𝑚𝑜𝑑𝑛.
• 𝑃 = 8 ∗ 17−1 𝑚𝑜𝑑77
• 𝑃 = 8 ∗ 68 𝑚𝑜𝑑77 = 5
• ∴ 𝑃 = 5
RSA
Attacks on RSA

## Page 174

174
⚫ Encryption exponent attacks
- Use a cryptographic exponent of 𝑒, usually 3, to save encryption time.
- They do not break the cryptosystem itself, but we must be prepared for these attacks.
- Coppersmith’s (theorem) attacks
• When a polynomial 𝑓(𝑥) with modulo 𝑛 and exponent 𝑒 has one root less than or equal to
𝑛1/𝑒, then
• Complexity can be found in polynomial time for log 𝑛.
• Reduced time compared to traditional complexity
𝑒
𝐶 𝑚𝑜𝑑𝑛.
• Applicable to 𝐶 = 𝑓 𝑃 − 𝑃𝑒 𝑚𝑜𝑑𝑛.
• 𝑒 = 3 and if 2⁄3 of the bits in the plaintext 𝑃 are known, then all the remaining bits can be
determined.
RSA
Attacks on RSA

## Page 175

175
⚫ Encryption exponent attacks
- Broadcast attacks
• An attack is possible when one sender uses the same 𝑒 to send messages to members of a
group of people.
• Create and send ciphertext to 3 people using the same 𝑒 = 3 and different moduli 𝑛1, 𝑛2,
𝑛3 for each.
• Compute 𝑀 = 𝑛1 × 𝑛2 × 𝑛3 as a common modulo using Chinese remainder theorem.
• The attacker gets 𝐶′ = 𝑃3 𝑚𝑜𝑑𝑀.
• 𝑃3 < 𝑀, and therefore 𝐶′ = 𝑃3
• The attacker can compute a cubic equation to get 𝑃.
RSA
Attacks on RSA
𝑪𝟏 = 𝑷𝟑 𝒎𝒐𝒅 𝑛1          𝑪𝟐 = 𝑷𝟑 𝒎𝒐𝒅 𝑛2      𝑪𝟑 = 𝑷𝟑 𝒎𝒐𝒅 𝑛3

## Page 176

176
⚫ Encryption exponent attacks
- Related message attacks
• Encrypt two plaintexts 𝑃1, 𝑃2, with 𝑒 = 3.
• When sending encrypted 𝐶1 and 𝐶2, if 𝑃1 and 𝑃2 are in a linear relation, it is possible to
compute plaintext 𝑃1, 𝑃2 in a short period of time.
- Short pad attacks
• Alice pads 𝑟1 with the message in transit and then sends an encrypted 𝐶1.
• Eve intercepts 𝐶1 to prevent Bob from receiving the message, and Bob notifies Alice.
• Alice creates a new pad 𝑟2 and then sends an encrypted 𝐶2.
• Eve intercepts 𝐶2 as well.
• Eve receives 𝐶1 and 𝐶2 and knows that they both encrypt the same plaintext.
• Since 𝑟1 and 𝑟2 are short, Eve can obtain the source plaintext message 𝑀.
RSA
Attacks on RSA

## Page 177

177
⚫ Encryption exponent attacks
- Public decryption exponent attacks
• If the attacker knows the private key 𝑑, the ciphertext can be decrypted.
• Prime factorize 𝑛 and determine the values of 𝑝 and 𝑞 using a probabilistic algorithm
• If the recipient simply replaces the compromised encryption exponent and uses the same
modulo value,
▪ The attacker can also decrypt ciphertexts generated with new encryption exponents.
• This means that if the private key 𝑑 is compromised, 𝑝, 𝑞, 𝑛, 𝑒 and 𝑑 everything has to be
regenerated.
- Small decryption exponent attacks
• 𝑞 < 𝑝 < 2𝑞 and if the private key 𝑑 is 𝑑 < ( Τ1 3)𝑛 Τ1 4, then the security is threatened by a
special attack based on consecutive fractions, a topic in number theory.
• To prevent decryption exponent attacks, 𝑑 must be used that satisfies 𝑑 ≥ ( Τ1 3)𝑛 Τ1 4.
RSA
Attacks on RSA

## Page 178

178
⚫ Plaintext attacks
- In RSA, plaintext and ciphertext are integers between 0 and n -1.
- The attacker would have information about the plaintext.
- Short message attacks
• Encrypt all messages until a ciphertext appears that is identical to the intercepted message.
• When encrypting short messages, pad the message with additional random bits at the
beginning and end of the message before encrypting it.
- Cyclic attacks
• Substitution of plaintext for ciphertext
• Basedon the factthatsuccessiveencryptionsof a ciphertextwilleventuallyresultin a plaintext.
• When 𝐶𝑘 = 𝐶 is reached, the value obtained in the previous step is returned as a plaintext.
RSA
Attacks on RSA
𝐶1 = 𝐶𝑒 𝑚𝑜𝑑 𝑛    //C is the intercepted ciphertext.
𝐶2 = 𝐶1
𝑒 𝑚𝑜𝑑 𝑛
⋯
𝐶𝑘 = 𝐶𝑘−1
𝑒 𝑚𝑜𝑑 𝑛 → If 𝐶𝑘 = 𝐶, stop here.
𝑃 = 𝐶𝑘−1

## Page 179

179
⚫ Plaintext attacks
- Unconcealed attacks
• Based on the fact that ciphertext and plaintext are commutative.
• Messages that don't hide who you are when encrypted.
• Usually the encryption exponent is odd, so messages such as 𝑃=0 or 𝑃=1 are encrypted
with themselves.
• Cryptographic programs should always check that the computed ciphertext is the same as
the plaintext.
RSA
Attacks on RSA

## Page 180

180
⚫ Modulo attacks
- Generic modulo attacks
• Possible when certain populations use the same modulo value 𝑛.
• A group of trusted third parties select 𝑝 and 𝑞.
• Compute n and ∅(𝑛) to generate and serve (𝑒𝑖, 𝑑𝑖) to all members of the group.
• Alice sends the ciphertext 𝐶 = 𝑃𝑒𝐵 𝑚𝑜𝑑𝑛 to Bob.
• Bob decrypts the received ciphertext 𝑃 = 𝐶𝑑𝐵 𝑚𝑜𝑑𝑛 using the exponent 𝑑𝐵, which is used
as his private key.
• Eve can decrypt Alice's message if she is also a member of this group and the exponent
pair (𝑒𝐸, 𝑑𝐸) is provided by a trusted third party.
• Eve's own exponent (𝑒𝐸, 𝑑𝐸) allows for a probabilistic attack to prime factorize 𝑛.
• Bob's private key 𝑑𝐵 can be obtained.
• Each object must choose its own modulo value.
RSA
Attacks on RSA

## Page 181

181
⚫ How to generate keys
- Same key generation process as traditional RSA cryptosystems
- The signer chooses two prime numbers 𝑝, 𝑞 and computes 𝑛 = 𝑝 ∗ 𝑞.
- The signer computes ∅ n = (p − 1)(q − 1).
- Choose a public key 𝑒 and use 𝑑 as a secret key that satisfies 𝑒 ∗ 𝑑 = 1 𝑚𝑜𝑑∅(𝑛).
- Then make 𝑛 and 𝑒 public.
RSA
RSA digital signatures
(𝑑, 𝑛)
𝑩𝒐𝒃
𝑆𝑒 𝑚𝑜𝑑 𝑛𝑀𝑑 𝑚𝑜𝑑 𝑛
𝑨𝒍𝒊𝒄𝒆
𝑀
(𝑒, 𝑛)
𝑀
𝐶𝑜𝑚𝑝𝑎𝑟𝑒
𝑀′
𝑀′ = 𝑀
𝑀′ ≡ 𝑀 𝑚𝑜𝑑 𝑛 →  𝑆𝑒 ≡ 𝑀 𝑚𝑜𝑑 𝑛 →  𝑀𝑑∗𝑒 ≡ 𝑀(𝑚𝑜𝑑 𝑛)

## Page 182

182
⚫ RSA signature structures are slow.
⚫ Signing a message digest speeds up the signing and verification process.
⚫ Using strong cryptographic hash functions makes signatures harder to attack.
⚫ Create and use the message digest 𝐷 = ℎ(𝑀).
RSA
RSA signatures for message digests
(𝑑, 𝑛)
𝑩𝒐𝒃
𝐷′ = 𝑆𝑒 𝑚𝑜𝑑 𝑛𝑆 = 𝐷𝑑 𝑚𝑜𝑑 𝑛
𝑨𝒍𝒊𝒄𝒆
𝑀
(𝑒, 𝑛)
𝑀
𝐶𝑜𝑚𝑝𝑎𝑟𝑒𝐷 = ℎ(𝑀)
𝐷 = ℎ(𝑀)

## Page 183

183
⚫ Proposed cipher using a discrete algebra problem on a finite body
⚫ 𝑝 is a very large prime number, 𝑒1 is one primitive root of 𝐺 =< 𝑍𝑝
∗,×>, 𝑟 is an integer,
⚫ Fast exponential algorithm (square -squared method) can be used to easily compute
𝑒2 = 𝑒1𝑟 𝑚𝑜𝑑𝑝.
⚫ If 𝑒1, 𝑒2 and 𝑝 are known, it is impractical to compute 𝑟 = log𝑒1 𝑒2 𝑚𝑜𝑑𝑝 (discrete algebra
problem).
ElGamal
Overview
(𝑒1, 𝑒2, 𝑝)
𝑑
Ciphertext : 𝐶1, 𝐶2
𝑆𝑒𝑙𝑒𝑐𝑡 𝑝 𝑣𝑒𝑟𝑦 𝑙𝑎𝑟𝑔𝑒 𝑝𝑟𝑖𝑚𝑒
𝑆𝑒𝑙𝑒𝑐𝑡 𝑒1 𝑝𝑟𝑖𝑚𝑖𝑡𝑖𝑣𝑒 𝑟𝑜𝑜𝑡
𝑆𝑒𝑙𝑒𝑐𝑡 𝑑
𝑒2 = 𝑒1𝑑 𝑚𝑜𝑑 𝑝
Decryption
𝑩𝒐𝒃
𝑃 = 𝐶2 × 𝐶1
𝑑 −1
𝑚𝑜𝑑 𝑝
Plaintext
P𝐶1 = 𝑒1𝑟 𝑚𝑜𝑑 𝑝
𝐶1 = 𝑒2𝑟 × 𝑃 𝑚𝑜𝑑 𝑝
𝑨𝒍𝒊𝒄𝒆
Plaintext
P
Encryption
Public key : (𝑒1, 𝑒2, 𝑝)
Private key : 𝑑

## Page 184

184
⚫ How to generate a key
- Choose a sufficiently large prime number 𝑝.
- Select 𝑑 from 𝐺 =< 𝑍𝑝
∗,×> that satisfies 1 ≤ 𝑑 ≤ 𝑝 − 2.
- Select the primitive root 𝑒1 of 𝐺 =< 𝑍𝑝
∗,×>.
- Compute 𝑒2 = 𝑒1𝑑 𝑚𝑜𝑑𝑝.
- What’s public are 𝑒1, 𝑒2, 𝑝
- What's private is 𝑑.
⚫ Encryption
- Select 𝑟 on 𝐺 =< 𝑍𝑝
∗,×>.
- 𝐶1 = 𝑒1𝑟 𝑚𝑜𝑑𝑝
- 𝐶2 = 𝑃 ∗ 𝑒2𝑟 𝑚𝑜𝑑𝑝
ElGamal
Overview

## Page 185

185
⚫ Decryption
- 𝑃 = 𝐶2 𝐶1
𝑑 −1
𝑚𝑜𝑑𝑝
⚫ Proof
- The ElGamal decryption representation 𝐶2 × (𝐶1
𝑑)−1 becomes 𝑃, which can be seen through
substitution.
ElGamal
Overview
𝐶2 × 𝐶1
𝑑 −1
𝑚𝑜𝑑 𝑝 = 𝑒2𝑟 × 𝑃 × 𝑒1𝑟𝑑 −1
𝑚𝑜𝑑 𝑝 = 𝑒1𝑑𝑟 × 𝑃 × 𝑒1𝑟𝑑 −1
= 𝑃

## Page 186

186
⚫ Example
- Bob selects 11 for 𝑝 and 2 for 𝑒1 (where 2 is the primitive root of 𝑍11
∗).
- He computes 3 for the value 𝑑 and 𝑒2 = 𝑒1𝑑 = 8.
- Here, the public key is (2, 8, 11) and the private key is (3)
- Alice chooses 𝑟 = 4, 𝑃 = 7.
- Encryption
• 𝐶1 = 𝑒1𝑟 𝑚𝑜𝑑𝑝 = 16 𝑚𝑜𝑑11 = 5 𝑚𝑜𝑑11
• 𝐶2 = 𝑃 ∗ 𝑒2𝑟 𝑚𝑜𝑑𝑝 = 7 ∗ 84 𝑚𝑜𝑑11 7 ∗ 4096 𝑚𝑜𝑑11 = 6 𝑚𝑜𝑑11
• ∴ 𝐶1 = 5, 𝐶2 = 6
- Decryption
• 𝐶2 ∗ (𝐶1
𝑑)−1 𝑚𝑜𝑑𝑝 = 6 ∗ 53 −1 𝑚𝑜𝑑11 = 6 ∗ 3 𝑚𝑜𝑑11 = 7 𝑚𝑜𝑑11
• ∴ 𝑃 = 7
ElGamal
Overview

## Page 187

187
⚫ Alice sends 𝐶2 = 𝑒2𝑟 ∗ 𝑃 𝑚𝑜𝑑𝑝 = 𝑒1𝑟𝑑 ∗ 𝑃 𝑚𝑜𝑑𝑝.
- (𝑒1𝑟𝑑) acts as a mask to hide the value of 𝑃 and must be removed to obtain the value of 𝑃.
⚫ Because modulo operations are used, Bob can create a duplicate of the mask.
- Using the inverse element for multiplication to remove the effect of masks.
⚫ Alice sends Bob a potion of the mask, which is 𝐶1 = 𝑒1𝑟.
- Bob needs to compute 𝐶1
𝑑 to create a duplicate of the mask,
• Because 𝐶1
𝑑 = (𝑒1
𝑟)𝑑 = (𝑒1𝑟𝑑).
• Bob obtains a duplicate of the mask, calculates its inverse, and multiplies it by 𝐶2 to
remove the mask.
⚫ Bob helps Alice create the mask (𝑒1
𝑟𝑑) without exposing the value 𝑑.
⚫ Alice helps Bob create the mask (𝑒1
𝑟𝑑) without exposing the value 𝑟.
ElGamal
Analytics

## Page 188

188
⚫ Small modulo attacks
- If p is a small number, Eve can easily compute 𝑑 = log𝑒1 𝑒2 𝑚𝑜𝑑𝑝 and store it to decrypt all
messages sent to Bob.
- Eve uses 𝐶1 to find out the random number used in that Alice sends 𝑟 = log𝑒1 𝐶1 𝑚𝑜𝑑𝑝 to her.
- Relying on the fact that discrete algebra problems with very large modulo are unsolvable,
• For safety, 𝑝 must be chosen to be greater than or equal to 2048 bits.
⚫ Known-plaintext attacks
- If Alice encrypts two plaintexts 𝑃 and 𝑃′ with the same randomized exponent 𝑟, then if Eve
knows one of them, she also knows the other.
- 𝐶2 = 𝑃 × 𝑒2𝑟 𝑚𝑜𝑑𝑝
- 𝐶′2= 𝑃′ × 𝑒2𝑟 𝑚𝑜𝑑𝑝
ElGamal
Security in ElGamal
𝑒2𝑟 = 𝐶2 × 𝑃−1 𝑚𝑜𝑑 𝑝
𝑃′ = 𝐶′2 × (𝑒2𝑟)−1𝑚𝑜𝑑 𝑝

## Page 189

189
⚫ Example
- Use the expression from the previous procedure as an example.
If 𝑝 = 11, 𝑒1 = 2, 𝑑 = 3, 𝑒2 = 8, 𝑟 = 4, 𝑃 = 7, 𝐶1 = 5, 𝐶2 = 6,
- It is assumed that we have calculated an additional 𝑃′ = 9, 𝐶1
′ = 5, 𝐶2
′ = 3.
- Small modulo attacks
• Convertible to 𝑟 = log𝑒1 𝐶1 𝑚𝑜𝑑𝑝 → 𝐶1 = 𝑒1𝑟 𝑚𝑜𝑑𝑝.
• 𝑟 = log2 5 𝑚𝑜𝑑11 → 5 = 2𝑟 𝑚𝑜𝑑11
• ∴ 𝑟 = 4
- Known-plaintext attacks
• 𝑒2𝑟 = 𝐶2 × 𝑃−1 𝑚𝑜𝑑𝑝
• 𝑒2𝑟 = 6 × 7−1 𝑚𝑜𝑑11 → 𝑒2𝑟 = 6 × 8 𝑚𝑜𝑑11 → 𝑒2𝑟 = 4 𝑚𝑜𝑑11
• 𝑃′ = 𝐶2
′ × (𝑒2𝑟)−1 𝑚𝑜𝑑𝑝
• 𝑃′ = 3 × (4)−1 𝑚𝑜𝑑11 → 𝑃′ = 3 × 3 𝑚𝑜𝑑11 → 𝑃′ = 9 𝑚𝑜𝑑11
ElGamal
Security in ElGamal

## Page 190

190
⚫ Can sign and verify using the ElGamal cryptosystem
⚫ Use the same key but different algorithms
⚫ How to generate keys
- Same as the key generation process in the ElGamal cryptosystem.
- 𝑝 is a sufficiently large prime number that a discrete algebra problem cannot be solved
within 𝑍𝑃
∗.
- 𝑒1 is a primitive root in 𝑍𝑃
∗.
- The sender chooses his private key 𝑑 to be a number smaller than 𝑝 − 1.
- Compute 𝑒2 = 𝑒1𝑑,
- The signer's public key is 𝑒1, 𝑒2, 𝑃 , and the private key is 𝑑.
ElGamal
ElGamal digital signature

## Page 191

191
ElGamal
ElGamal digital signature
𝐶𝑜𝑚𝑝𝑎𝑟𝑒
Signing
Algorithm1(𝑒1, 𝑟, 𝑝) 𝑆1
𝑚𝑜𝑑 𝑝
Signing
Algorithm2(𝑀, 𝐴𝑙𝑖𝑐𝑒𝑃𝑟𝑖, 𝑒1, 𝑟, 𝑝, 𝑆1) 𝑆2
𝑚𝑜𝑑 𝑝
Verifying
Algorithm1
Verifying
Algorithm2
𝑉𝑒𝑟𝑖𝑓𝑦
(𝑒2, 𝑝, 𝑆1, 𝑆2)
(𝑒1, 𝑝, 𝑀)

## Page 192

192
⚫ Signature : signer signs the digest of the message.
- Public and private keys are used repeatedly, but each time with a different secret random
number.
- The signer computes the first signature 𝑆1 = 𝑒1𝑟 𝑚𝑜𝑑𝑝.
- Then calculates the second signature 𝑆2 = 𝑀 − 𝑑 ∗ 𝑆1 ∗ 𝑟−1𝑚𝑜𝑑 𝑝 − 1 .
• Here, 𝑟−1 is an inverse element of the multiplication of the modulo 𝑝.
- The signer sends 𝑀, 𝑆1, 𝑆2 to the verifier.
⚫ Validation : the validator performs the following steps after receiving 𝑀, 𝑆1, 𝑆2.
- Check that 0 < 𝑆1 < 𝑝 and 0 < 𝑆2 < 𝑝 − 1.
- Calculate 𝑉1 = 𝑒1𝑀 𝑚𝑜𝑑𝑝 and 𝑉2 = 𝑒2𝑆1 ∗ 𝑆1
𝑆2 𝑚𝑜𝑑𝑝.
- Compare 𝑉1 with 𝑉2.
⚫ Comparison procedure : use 𝑒2 = 𝑒1𝑑 and 𝑆1 = 𝑒1𝑟.
ElGamal
ElGamal digital signature
𝑉1 ≡ 𝑉2 𝑚𝑜𝑑 𝑝 →  𝑒1𝑀 ≡ 𝑒1𝑆1 ∗ 𝑆1
𝑆2 𝑚𝑜𝑑 𝑝
≡ 𝑒1𝑑 𝑆1
𝑒1𝑟 𝑆2 𝑚𝑜𝑑 𝑝
≡ 𝑒1𝑑𝑆1+𝑟𝑆2 (𝑚𝑜𝑑 𝑝)

## Page 193

193
⚫ Example
- Signer (Alice) selects 𝑝 = 3119, 𝑒1 = 2, 𝑑 = 127, calculates 𝑒2 = 2127𝑚𝑜𝑑3119 = 1702.
- She selects 𝑟 = 307, 𝑀 = 320.
- Signer (Alice)
- Validator (Bob)
ElGamal
ElGamal digital signature
𝑆1 = 𝑒1𝑟 = 2307 = 2083 𝑚𝑜𝑑 3119
 𝑆2 = 𝑀 − 𝑑 ∗ 𝑆1 ∗ 𝑟−1 = 320 − 127 ∗ 2083 ∗ 307−1 = 2105 𝑚𝑜𝑑 3118
𝑉1 = 𝑒1𝑀 = 3006 𝑚𝑜𝑑 3119
𝑉2 = 𝑑𝑆1 ∗ 𝑆1
𝑆2 = 17022083 ∗ 20832105 = 3006 𝑚𝑜𝑑 3119

## Page 194

194
⚫ Example
- Signer (Alice) selects 𝑝 = 3119, 𝑒1 = 2, 𝑑 = 127, calculates 𝑒2 = 2127𝑚𝑜𝑑3119 = 1702.
- She selects 𝑟 = 307, 𝑀 = 320.
ElGamal
ElGamal digital signature
𝑑 = 127
𝑩𝒐𝒃
𝑒2𝑆1𝑆1
𝑆2 𝑚𝑜𝑑 𝑝
𝑒1𝑟𝑚𝑜𝑑 𝑝
𝑨𝒍𝒊𝒄𝒆
𝑀
(𝑒1, 𝑒2, 𝑑)
𝑀
𝐶𝑜𝑚𝑝𝑎𝑟𝑒
𝑀 − 𝑑𝑆1 𝑟−1𝑚𝑜𝑑(𝑝 − 1)
𝑒1𝑀 𝑚𝑜𝑑 𝑝
𝑟 = 307
3006 𝑚𝑜𝑑 3119
𝑉1
𝑉2
17022083 ∗ 20832105
= 3006 𝑚𝑜𝑑 3119
2320 = 3306 𝑚𝑜𝑑 3119
2307𝑚𝑜𝑑 3119
= 2083 𝑚𝑜𝑑 3119
320 − 127 ∗ 2083 ∗ 307−1
= 2105 𝑚𝑜𝑑 3118
𝑆1
𝑆2

## Page 195

195
⚫ Key-only forgery : the attacker can only obtain the public key, the two kinds of forgery are
possible.
- The attacker has a pre-generated message M.
• The attacker chooses two legitimate signatures 𝑆1, 𝑆2 for this message (selective forgery
attack).
• The attacker selects 𝑆1 and calculates 𝑆2.
• 𝑆1
𝑆2 ≡ 𝑒1𝑀𝑑−𝑆1 𝑚𝑜𝑑𝑝 or 𝑆2 ≡ log𝑆1 𝑒1𝑀𝑑−𝑆1 (𝑚𝑜𝑑𝑝) is required.
• Conversely, when 𝑆2 is chosen, it becomes more difficult to compute 𝑆1.
- The attacker has random M, 𝑆1, 𝑆2.
• 𝑀 = 𝑥𝑆1 𝑚𝑜𝑑 𝑝 − 1 , 𝑆1 = −𝑦𝑆2𝑚𝑜𝑑 𝑝 − 1
• If satisfactory 𝑥, 𝑦 are obtained, the message can be forged.
• In the end, it is a meaningless forgery.
- Forging known messages
• Suppose an attacker intercepts the message 𝑀 and the signature 𝑆1 𝑆2.
▪ You can find a message 𝑀′with the signatures 𝑆1, 𝑆2 that has the signature.
▪ This is a useless forgery and not a useful attack.
ElGamal
ElGamal digital signature

## Page 196

196
ECC
⚫ Elliptic curve
- A curve in the plane, a group of points with coordinates 𝑥 and 𝑦.
- The equation of a curve defines all the points on that curve.
• 𝑦 = 3 is a horizontal line with vertical coordinates of 3. A curve of the form 𝑦 = 𝑎𝑥 + 𝑏 is
a straight line with a fixed number 𝑎 and 𝑏.
• 𝑥2 + 𝑦2 = 1 is a circle of radius 1 centered on the origin, and points on any curve are all
pairs of (𝑥, 𝑦) that satisfy the equation of that curve.
• Elliptic curves used in cryptography are curves whose equation typically looks like this :
𝑦2 = 𝑥3 + 𝑎𝑥 + 𝑏, where the constants 𝑎 and 𝑏 define the shape of the curve.
Elliptic Curve Cryptography (ECC) was proposed independently by Neil Koblitz and Victor Miller in
1985. The main advantage of elliptic curve ciphers over traditional public key cryptography, such
as RSA or ElGamal ciphers, is that they provide a similar level of security while using shorter keys.
Understanding elliptic curves
Source : https://en.wikipedia.org/wiki/Elliptic_curve

## Page 197

197
ECC
⚫ Elliptic curve example
- The figure below shows an elliptic curve that satisfies 𝑦2 = 𝑥3 − 4𝑥.
Elliptic Curve Cryptography (ECC) was proposed independently by Neil Koblitz and Victor Miller in
1985. The main advantage of elliptic curve ciphers over traditional public key cryptography, such
as RSA or ElGamal ciphers, is that they provide a similar level of security while using shorter keys.
Elliptic curve principle
<Elliptic curve with equation 𝑦2 =  𝑥3 −  4𝑥 shown above the real numbers>

## Page 198

198
ECC
⚫ Elliptic curve example
- All points that make up a curve that falls in the range where 𝑥 is between −3 and 4.
- These are points on the left part of the curve that look like a circle, or points on the right
part of the curve that represent a parabola.
- All of these points have (𝑥, 𝑦) coordinates that satisfy the equation 𝑦2 = 𝑥3 – 4𝑥 on the curve.
- For example, for 𝑥 = 0, 𝑦2 = 𝑥3 – 4𝑥 = 03 – 4 × 0 = 0. Therefore, 𝑦 = 0 is a solution, and
the point (0, 0) belongs to the curve. Similarly, for 𝑥 = 2, the solution of the equation is 𝑦 =
0, which means that the point (2, 0) belongs to the curve.
Elliptic Curve Cryptography (ECC) was proposed independently by Neil Koblitz and Victor Miller in
1985. The main advantage of elliptic curve ciphers over traditional public key cryptography, such
as RSA or ElGamal ciphers, is that they provide a similar level of security while using shorter keys.
Elliptic curve principle

## Page 199

199
ECC
⚫ Elliptic curve example
- Equations on a curve don't always have solutions
• Example 1
▪ To find the point corresponding to the coordinate 𝑥 = 1, use 𝑦2 = 𝑥3 − 4𝑥 to find 𝑦2.
▪ When this equation is solved, the result is −3 with no corresponding solution 𝑦2 = −3.
▪ Since there is no solution to the curve equation for 𝑥 = 1, there is no point on the curve
on the 𝑥 axis at that location, as shown in the figure.
• Example 2
▪ To find a solution for 𝑥 = -1, we have the equation 𝑦2 = -1 + 4 = 3.
▪ This equation has two solutions (𝑦 = √3, 𝑦 = – √3), the square root of 3 and its negative value.
▪ Since squaring always yields a positive number, 𝑦2 = (– 𝑦)2 holds for all real numbers 𝑦.
▪ The curve in the figure is symmetric about the 𝑥 axis for all points that solve this
equation (as are all elliptic curves of the form 𝑦2 = 𝑥3 + 𝑎𝑥 + 𝑏 ).
In ECC, it is important to distinguish between points on the curve and points off the curve. Points
on the curve are used for secure operations from a security perspective, while points off the
curve can pose a security threat.
Elliptic curve principle

## Page 200

200
ECC
⚫ Geometricallyunderstandingthe locationof 𝑅 = 𝑃 + 𝑄 relativeto points 𝑃 and 𝑄 on the curve
- Suppose you want to add two points, 𝑃 and 𝑄, on an elliptic curve to get a new point, 𝑅.
- Draw a line connecting 𝑃 and 𝑄 that is determined by geometric rules.
- Find the intersection of that line with the curve, and at that intersection, find a point that is
symmetric about the 𝑥 axis, which is 𝑅 = 𝑃 + 𝑄.
• In the figure, the line connecting 𝑃 and 𝑄
intersects a point between 𝑃 and 𝑄.
• Point 𝑅 is the point that is symmetric about
the intersection and the 𝑥 axis, with the same
𝑥 component of the coordinates and opposite
signs of the 𝑦component.
We have seen that the points on an elliptic curve are all coordinates (𝑥, 𝑦) that satisfy the
equation of the curve such as 𝑦² = 𝑥³ + 𝑎𝑥 + 𝑏. We will review the "rule of addition," which is
how we add points on an elliptic curve.
Add two points

## Page 201

201
ECC
⚫ Geometricallyunderstandingthe locationof 𝑅 = 𝑃 + 𝑄 relativeto points 𝑃 and 𝑄 on the curve
- To calculate the coordinates (𝑥𝑅, 𝑦𝑅) of point 𝑅, use the coordinates of point 𝑃 (𝑥𝑝, 𝑦𝑝) and the
coordinates of point 𝑄 (𝑥𝑄, 𝑦𝑄), using the following formula
• 𝑥𝑅 = 𝑚2 − 𝑥𝑝 − 𝑥𝑄
• 𝑦𝑅 = 𝑚(𝑥𝑝 − 𝑥𝑅) – 𝑦𝑝
- Here, 𝑚 is the slope of the straight line
connecting 𝑃 and 𝑄,
𝑚 = (𝑦𝑄 − 𝑦𝑝) / (𝑥𝑄 − 𝑥𝑝).
We have seen that the points on an elliptic curve are all coordinates (𝑥, 𝑦) that satisfy the
equation of the curve such as 𝑦² = 𝑥³ + 𝑎𝑥 + 𝑏. We will review the "rule of addition," which is
how we add points on an elliptic curve.
Add two points

## Page 202

202
ECC
⚫ Diffie-Hellman key exchange scheme using ECC
- Premise
• All should agree to use the 6-element tuple from (𝑝, 𝑎, 𝑏, 𝑔, 𝑛, ℎ) as a specific definition
domain parameter
• In some cases, you can also write a 7-element tuple with 𝑝 = {𝑚, 𝑓(𝑥)}.
• Each party must have the appropriate key pair (𝑑𝑥, 𝑄𝑥) on the ECC.
▪ 𝑑 is a randomly chosen integer between 1 and 𝑛 − 1 that is the private key.
▪ The public key 𝑄 is an integer satisfying 𝑄 = 𝑑𝑔.
Elliptic Curve Diffie-Hellman (ECDH) allows two people who wish to communicate cryptographically
to share a secret key, andenables symmetric-key cryptographic communication.
Elliptic Curve Diffie-Hellman (ECDH)

## Page 203

203
ECC
⚫ Diffie-Hellman key exchange scheme using ECC
- Procedure
• Alice has a key pair (𝑑𝐴, 𝑄𝐴) and Bob has a key pair (𝑑𝐵, 𝑄𝐵), and they know each other's
public keys by exchanging them.
• Alice computes the point (𝑥𝐴, 𝑦𝐴) = 𝑑𝐴𝑄𝐵, and Bob computes the point (𝑥𝐵, 𝑦𝐵) = 𝑑𝐵𝑄𝐴.
▪ 𝑑𝐴𝑄𝐵 = 𝑑𝐴𝑑𝐵 ∗ 𝑔 = 𝑑𝐵𝑑𝐴 ∗ 𝑔 = 𝑑𝐵𝑄𝐴
• The shared secret value is 𝑥𝑘.
▪ Many modern Elliptic Curve Diffie-Hellman (ECDH)-based ciphers hash the shared secret
value to generate a symmetric key.
- It is ECDH when the public key is permanent (static) and ECDH Ephemeral(ECDHE) when it is
ephemeral.
Elliptic Curve Diffie-Hellman (ECDH)
Elliptic Curve Diffie-Hellman (ECDH) allows two people who wish to communicate cryptographically
to share a secret key, andenables symmetric-key cryptographic communication.

## Page 204

204
ECC
⚫ E-signatures via elliptic curves
- A verification algorithm in which a signer uses their private key to create a signature, and a
verifier uses the signer's public key to check the accuracy of the signature.
• The signer holds the number 𝑑 as a private key, and the verifier holds 𝑃 = 𝑑𝐺 as a public
key.
• Both parties know in advance which elliptic curve to use, the order of the curve (𝑛, the
number of points on the curve), and the coordinates of the base point 𝐺 in advance.
The standard algorithm for signatures using ECC is the Elliptic Curve Digital Signature Algorithm
(ECDSA). It has replaced RSA and DSA signatures in many applications, is the only signature
algorithm used in Bitcoin, and is supported by many TLS and SSH implementations.
Elliptic Curve Digital Signature Algorithm (ECDSA)

## Page 205

205
ECC
⚫ Signature generation
- The signer uses their private key to create a signature for the message.
• The signer first uses a hash function, such as SHA-256 or BLAKE2, to generate the
message's hash value ℎ.
• The signer chooses a random number 𝑘 between 1 and 𝑛 − 1, and computes a point with
coordinates (𝑥, 𝑦), called 𝑘𝐺.
• Set 𝑟 = 𝑥 𝑚𝑜𝑑𝑛, compute 𝑠 = (ℎ + 𝑟𝑑) / 𝑘 𝑚𝑜𝑑𝑛, and use these values as the signature
(𝑟, 𝑠).
• The length of the signature depends on the length of the coordinates used.
• E.g., If you use a curve whose coordinates are 256-bit numbers, 𝑟 and 𝑠 are each 256 bits
long, resulting in a 512-bit signature.
The standard algorithm for signatures using ECC is the Elliptic Curve Digital Signature Algorithm
(ECDSA). It has replaced RSA and DSA signatures in many applications, is the only signature
algorithm used in Bitcoin, and is supported by many TLS and SSH implementations.
Elliptic Curve Digital Signature Algorithm (ECDSA)

## Page 206

206
ECC
⚫ Signature verification
- The process of validating a signed message using a public key to verify its accuracy.
1. The verifier computes the inverse of 𝑠 of the signature.
▪ The inverse of 𝑠 is denoted by 𝑤 = 1 / 𝑠, where 𝑠 is defined as 𝑠 = (ℎ + 𝑟𝑑) / 𝑘, so 𝑤 is
equal to 𝑘 / (ℎ + 𝑟𝑑) 𝑚𝑜𝑑𝑛.
2. The verifier calculates 𝑢 by multiplying 𝑤 and ℎ.
▪ 𝑤ℎ = ℎ𝑘 (ℎ + 𝑟𝑑) = 𝑢
3. The verifier calculates 𝑣 by multiplying 𝑤 and 𝑟.
▪ 𝑤𝑟 = 𝑟𝑘(ℎ + 𝑟𝑑) = 𝑣
4. Now, the verifier uses the following formula to calculate the point 𝑄.
▪ 𝑄 = 𝑢𝐺 + 𝑣𝑃
Where 𝑃 is the signer's public key, defined as 𝑃 = 𝑑𝐺. To accept the signature as valid,
the verifier checks that the coordinate 𝑥 of 𝑄 is equal to the value 𝑟 in the signature.
The standard algorithm for signatures using ECC is the Elliptic Curve Digital Signature Algorithm
(ECDSA). It has replaced RSA and DSA signatures in many applications, is the only signature
algorithm used in Bitcoin, and is supported by many TLS and SSH implementations.
Elliptic Curve Digital Signature Algorithm (ECDSA)

## Page 207

207
ECC
⚫ Signature verification
- The process of validating a signed message using a public key to verify its accuracy.
5. Replace the public key 𝑃 with the actual value 𝑑𝐺 to compute the point 𝑄.
▪ 𝑢𝐺 + 𝑣𝑑𝐺 = (𝑢 + 𝑣𝑑)𝐺
6. Replace 𝑢 and 𝑣 with their actual values.
▪ 𝑢 + 𝑣𝑑 = ℎ𝑘 (ℎ + 𝑟𝑑) + 𝑑𝑟𝑘/ (ℎ + 𝑟𝑑) = (ℎ𝑘 + 𝑑𝑟𝑘) / (ℎ + 𝑟𝑑) = 𝑘 (ℎ + 𝑑𝑟) / (ℎ + 𝑟𝑑) = 𝑘
The standard algorithm for signatures using ECC is the Elliptic Curve Digital Signature Algorithm
(ECDSA). It has replaced RSA and DSA signatures in many applications, is the only signature
algorithm used in Bitcoin, and is supported by many TLS and SSH implementations.
Elliptic Curve Digital Signature Algorithm (ECDSA)
This shows that (𝑢 +  𝑣𝑑) is equal to the value of 𝑘 chosen during signature
generation, and that the point 𝑘𝐺 is equal to 𝑢𝐺 +  𝑣𝑑𝐺. The verification algorithm
succeeds in computing the same point 𝑘𝐺 that was computed during signature
generation. The verifier checks for validity by verifying that the 𝑥 coordinate of 𝑘𝐺
is the same as the received 𝑟 value, otherwise the signature is rejected as invalid.

## Page 208

Integrity
04
• Hash function overview
• MD5
• SHA-1, SHA-2, SHA-3

## Page 209

209
Hash function overview
⚫ A cryptographichashfunctiontakesina randommessageandoutputsa fixed-lengthmessagedigest.
- The valueobtainedby a hash functionis calleda hash value, hash code, hash checksum,or hash.
⚫ Used in computer software for very fast data retrieval
⚫ Can speed up database searches and table searches
⚫ Used to verify the integrity of transmitted data and as an HMAC block to prove the sender
⚫ The hash function quality is determinedby the probabilityof hash collisionsin the input domain.
- The higher the probability of collisions, the harder it is to distinguish between different data,
and the more expensive it is to search.
⚫ Distinction between cryptographic and non-cryptographic hash functions
- Cryptographic hash functions : MD5, SHA series functions
• Must be secure against reverse and secondary phases, and collision pairs; used for
authentication
- Non-cryptographic hash functions : CRC32
The concept of hash functions originated in the 1950s, but even before the term "hash" was
coined, the same functions were developed to transform and compress data for efficient storage
and retrieval.
Hash function history

## Page 210

210
Hash function overview
⚫ Iterative hash functions
- General structure
• Framework for cryptographic hash function structures
• Takes in bits and outputs bits
• 𝑓: 0,1 𝑚 × 0,1 𝑛 = 0,1 𝑚
• However, this 𝑓 should be such that it is difficult to get the two inputs from the output and
to know the different 𝑚1, 𝑚2 that satisfy 𝑓 𝑚1 = 𝑓 𝑚2 .
The concept of hash functions originated in the 1950s, but even before the term "hash" was
coined, the same functions were developed to transform and compress data for efficient storage
and retrieval.
Merkle-Damgard construction
Message
block 1
Message
block 1
𝑓IV
Message
block 2
Message
block 2
𝑓
Message
block n
Message
block n
𝑓
Length
Padding
𝑓 𝐹𝑖𝑛𝑎𝑙𝑖𝑠𝑎𝑡𝑖𝑜𝑛 𝐻𝑎𝑠ℎ

## Page 211

211
Hash function overview
⚫ Iterative hash functions
- Wide pipe structure
• Structural weaknesses and multiple collision attacks in the basic structure led to the
development of the wide pipe hash structure.
• Similar to the Merkle-Damgard configuration, but with a larger internal state.
▪ This means that the bit length used internally is much larger than the output bits.
▪ If 𝑛 bits of hash are needed, 𝑓 compresses 2𝑛 bits of concatenated values and 𝑚 bits of
messages into a 2𝑛-bit output.
▪ In the last step, the second compression compresses the internal hash value (2𝑛 bits)
into a final hash value (𝑛 bits).
The concept of hash functions originated in the 1950s, but even before the term "hash" was
coined, the same functions were developed to transform and compress data for efficient storage
and retrieval.
Merkle-Damgard construction
Message
block 1
IV1
IV2
Message
block 2
Message
Message
block 3
Message
block 4
𝐻𝑎𝑠ℎ𝑓 𝑓 𝑓 𝑓𝑖𝑛𝑎𝑙
Padding(MESSAGE)

## Page 212

212
Hash function overview
⚫ Iterative hash functions
- Quick wide pipe structure
• Algorithm that roughly doubles the speed of wide-pipe hash functions
• Half goes into the subsequent compression function, and the other half goes into the next
compression function.
• Combine with the output of the corresponding compression function
• XORhalfofthepreviousconcatenationvalueandpassitastheoutputofthecompressionfunction
• Use longer message blocks for each iteration
The concept of hash functions originated in the 1950s, but even before the term "hash" was
coined, the same functions were developed to transform and compress data for efficient storage
and retrieval.
Merkle–Damgård construction
Message
block 1
IV1
IV2
Message
block 2
Message
Message
block 3
Message
block 4
𝐻𝑎𝑠ℎ𝑓 𝑓 𝑓𝑖𝑛𝑎𝑙
Padding(MESSAGE)
𝑓

## Page 213

213
MD5
⚫ Take in a random-length message and output a 128-bit-length value
- Input messages are split into 512-bit blocks
- Pad messages first and divide by 512 so they fall apart
- Add the first single bit, 1, to the end of the message
- Fill with zeros up to 64 bits less than the length of a multiple of 512
- Filltheremaining64bitswithanintegerequaltotheoriginalmessagelength.
- A single message block is processed in four steps
• Each step is called a round
• Nonlinear function 𝑓, modulo addition, and left rotation
• There are four F-functions, and a different F is used for each round.
▪ 𝐹 𝑋, 𝑌, 𝑍 = 𝑋 ∧ 𝑌 ∨ ¬𝑋 ∧ 𝑧 𝐺 𝑋, 𝑌, 𝑍 = (𝑋 ∧ 𝑍) ∨ (𝑌 ∧ ¬𝑍)
▪ 𝐻 𝑋, 𝑌, 𝑍 = 𝑋 ⊕ 𝑌⨁𝑍 𝐼 𝑋, 𝑌, 𝑍 = 𝑌⨁(𝑋 ∨ ¬𝑍)
MD5 is a 128-bit cryptographic hash function specified as RFC1321 and used for integrity checks, such as
verifying that a program or file is original. A design flaw was discovered in 1996, and a hash collision was
discovered in 2006 using the computing power of a single laptop in less than a minute, making it an obsolete
hash algorithm today.
Overview
⨁ : XOR
∧ : logical conjunction
∨ : logical disjunction
¬ : NOT
⊞ : modulo 232

## Page 214

214
SHA-1, SHA-2, SHA-3
⚫ Recognizing that SHA-1's strong collision resistance was broken in 2005, NIST began the
process of selecting a new one-way hash function in 2007.
- Competitive bidding process, such as in the AES selection process.
- In 2012, the selection was finalized and an algorithm
called Keccack was chosen as the final standard.
• This is the current SHA-3.
- Why NIST selected Keccack as SHA-3
• Totally different structure than SHA-2
• Transparent design and easy to analyze
• Work wellon a varietyof devicesand in any combination
• High performance when embedded in hardware
• Better security than the last competing algorithm
The Secure Hash Algorithm (SHA) is a standard developed by NIST based on MD5 and published
as FIP 180. It was revised as FIP 180-1, which included SHA-1, and revised again as FIP 180-2,
which included versions of SHA-224, SHA-256, SHA-384, and SHA-512.
SHA

## Page 215

215
SHA-1, SHA-2, SHA-3
⚫ NIST first published FIPS 180 as the secure hash standard, SHA, which is referred to as SHA-0
to distinguish it from other functions.
⚫ After some time, FIPS 180 was abolished and FIPS 180-1 (SHA-1) was published
- Add a one-bit rotation operation to the compression function of SHA-0
- Address issues in the original algorithm that reduced cryptographic security
• However, it did not disclose what the problem actually was.
- SHA-1 is generally known to be more difficult to attack cryptographically than SHA-0.
- SHA-0 and SHA-1 generate a 160-bit hash value from a message of up to 264 bits.
• Based on methods similar to those used in the MD4 and MD6 hash functions
The Secure Hash Algorithm (SHA) is a standard developed by NIST based on MD5 and published
as FIP 180. It was revised as FIP 180-1, which included SHA-1, and revised again as FIP 180-2,
which included versions of SHA-224, SHA-256, SHA-384, and SHA-512.
SHA

## Page 216

216
SHA-1, SHA-2, SHA-3
⚫ NIST later published four variants with longer hash values (collectively referred to as SHA-2)
- SHA-256, SHA-384, and SHA-512 first published as drafts in 2001
- Designated as a formal standard along with SHA-1 in 2002 (FIPS 180-2)
- Addedto the SHA-224 standardin 2004 to matchthe hash lengthto the key lengthof tripleDES.
- SHA-256 and SHA-512 are hash functions that use 32-byte and 64-byte words, respectively.
• Some constants are different, but the structure is exactly the same except for the number
of rounds
- SHA-224, SHA-384 are SHA-256 and SHA-512 hash values computed with different initial
values and truncated to fit the final hash value length.
⚫ Collision resistance of hashes
- Weak collision resistance : for a given 𝑥, collision resistance is weak when it is difficult to find
𝑦 ≠ 𝑥 such that 𝐻 𝑥 = 𝐻 𝑦 .
- Strong collision resistance : if 𝑥 and 𝑦 are found to have the same hash output value, such
that 𝐻(𝑥)=𝐻(𝑦).
The Secure Hash Algorithm (SHA) is a standard developed by NIST based on MD5 and published
as FIP 180. It was revised as FIP 180-1, which included SHA-1, and revised again as FIP 180-2,
which included versions of SHA-224, SHA-256, SHA-384, and SHA-512.
SHA

## Page 217

217
SHA-1, SHA-2, SHA-3
SHA
Algorithm Size Internal size Block size No. of
courses
List of operations
used
Security
strength Crash
MD5 128 128 (4*32) 512 64 +, and, xor, rot, add,
or <64 Found
SHA-0 160 160 (5*32) 512 80 +, and, or, xor, rotl <80 Found
SHA-1 160 160 (5*32) 512 80 +, and, or, xor, rotl <63 Found
SHA-2
SHA-224 224
256 (8*32)
512
64 +, and, or, xor, shr,
rotr
112
SHA-256 256 512 128
SHA-384 384
512 (8*64) 1024 80 +, and, or, xor, shr,
rotl
192
SHA-512 512 256
SHA-
512/224 224 112
SHA-
512/226 256 128
SHA-3
SHA3-224 224
1600 (5*5*64)
1152
24 +, and, xor, rot, not
112
SHA3-256 256 1088 128
SHA3-384 384 832 192
SHA3-512 512 576 256
SHAKE128 d(variable) 1344 min(d|2,128)
SHAKE256 d(variable) 1088 min(d|2,256)

## Page 218

Lab
05
• Break Caesar cipher
• Break DES
• Break hash with Hashcat

## Page 219

219
Break Caesar cipher
⚫ Exhaustive search attack
- Decrypt the ciphertext "P svcl Jyfwavnyhwof“ when Eve intercepted it.
- “I love Cryptography” was obtained when running an exhaustive search attack.
The Caesar cipher is a relatively easy ciphertext to crack. There are two main ways to break this
ciphertext.
Decrypting Caesar
K
1
2
3
4
5
6
7
O rubk Ixevzumxgvne
N qtaj Hwduytlwfumd
M pszi Gvctxskvetlc
L oryh Fubswrjudskb
K nqxg Etarvqitcrja
J mpwf Dszquphsbqiz
I love Cryptography

## Page 220

220
Break Caesar cipher
⚫ Statistical attack
- In English, the alphabet is used in the following order of frequency : E (12.7%), T (9.1%),
A (8.2%), O (7.5%), and N (7.0%).
- Characters that occur frequently in ciphertext are more likely to be E, T, A, O, and N in
plaintext.
• Analyze frequency to infer plaintext counterparts to ciphertext.
• It's a probability, so it's possible that it’s not.
- Frequency of common plaintext
• 2-character frequency : TH, HE, and IN are the most common.
• 3-character frequency : THE, and ING are the most common.
The Caesar cipher is a relatively easy ciphertext to crack. There are two main ways to break this
ciphertext.
Decrypting Caesar

## Page 221

221
Break Caesar cipher
⚫ Statistical attack
- Ciphertext
• juhhwlqj hyhubrqh zhofrph wr dfv lqirupdwlrq vhfxulwb zruog
• Frequency of occurrence of characters in the given ciphertext
▪ h = 8
▪ r = 6
▪ w = 4
▪ Substitutingthe most frequentcharacterh for e in the plaintextindicatesthat the key is 3.
• Decrypted plaintext
▪ greeting everyone welcome to acs information security world
The Caesar cipher is a relatively easy ciphertext to crack. There are two main ways to break this
ciphertext.
Decrypting Caesar

## Page 222

222
⚫ OpenSSL
- Open source implementations of TLS and SSL, used for communicating data over networks.
• The core library is written in C.
▪ Implement basic encryption and various utility functions
• Supported encryption algorithms
▪ AES
▪ Blowfish
▪ DES/T-DES
▪ IDEA
▪ RC4
• Supported hash functions
▪ MD5
▪ SHA-1
▪ MDC-2
Break DES
Encryption lab using openSSL

## Page 223

223
⚫ OpenSSL
- Installed by default on Linux/Mac, but requires installation on Windows
- Access via the following link.
• https://slproweb.com/products/Win32OpenSSL.html
• Download "Win64 OpenSSL v3.2.0"-exe among several other versions.
- Access the below path from the C drive
after installation.
• C:\Program Files\OpenSSL-Win64\bin
• Right click to open in Terminal.
Break DES
Encryption lab using openSSL

## Page 224

224
⚫ OpenSSL-DES encryption/decryption
- Write and save text in Notepad (save as plain.txt).
• Type “It is Plaintext!”
- Type commands in Terminal.
Break DES
Encryption lab using openSSL
PS C:\> .\openssl enc -des3 -in D:\plain.txt -out D:\plain_enc.txt
Enter ACS
Enter ACS

## Page 225

225
⚫ OpenSSL-DES encryption/decryption
- Decrypt the encrypted Notepad file.
Break DES
Encryption lab using openSSL
PS C:\> .\openssl enc -des3 -d -in D:\plain_enc.txt -out D:\plain_dec.txt
Enter ACS

## Page 226

226
Break DES
⚫ Cryptool
- Offer e-learning program for visualization of cryptography and cryptanalysis
- Cryptool implements more than 400 cryptographic algorithms
- Provide contemporary symmetric and asymmetric ciphers, including RSA, ECC, digital
signatures, and hybrid encryption, as well as classical ciphers
- Classical ciphers include solvers (analyzers) in addition to algorithms.
- Download link : https://www.cryptool.org/en/ct2/
Cryptool is an open source, free e-learning software for learning cryptography and cryptanalysis
concepts. According to the IT security magazine Hakin9, Cryptool is a globally popular software
in the field of cryptography.
Cryptool2

## Page 227

227
Break DES
Cryptool2
DES String Decoder
Data Input
Key Input
Data Output

## Page 228

228
⚫ Weak keys in DES
- The vulnerability is that the operation after parity stripping is either all 0s, all 1s, or half 0s
and half 1s.
- If you encrypt a block with a weak key and encrypt the result with the same weak key,
• You get the original block.
• You get the same result even when the block is decrypted twice.
Break DES
DES weak-key encryption
𝑲𝒆𝒚𝒔 𝒃𝒆𝒇𝒐𝒓𝒆 𝒑𝒂𝒓𝒊𝒕𝒊𝒆𝒔 𝒅𝒓𝒐𝒑 (𝟔𝟒 𝒃𝒊𝒕𝒔) 𝑨𝒄𝒕𝒖𝒂𝒍 𝑲𝒆𝒚 (𝟓𝟔 𝒃𝒊𝒕𝒔)
0101 0101 0101 0101 0000000 0000000
1F1F 1F1F 1F1F 1F1F 0000000 FFFFFFF
E0E0 E0E0 E1E1 E1E1 FFFFFFF 0000000
FEFE FEFE FEFE FEFE FFFFFFF FFFFFFF

## Page 229

229
⚫ Create a ciphertext using the DES you created in the previous section.
- Weak key encryption test
• Data : 12 34 56 87 65 43 21
• Key : 01 01 01 01 01 01 01 01
• Ciphertext : 81 4F E9 38 58 91 54 F7
- Paste the encryption result from here back into the input of the Encrypt command.
• Data : 81 4F E9 38 58 91 54 F7
• Key : 01 01 01 01 01 01 01 01
• Ciphertext : 12 34 56 78 87 65 43 21
- Using the weak key, we can see that the original message is output with only two
encryptions.
Break DES
DES weak-key encryption

## Page 230

230
Break DES
DES weak-key encryption
First encryption
Data Input
Weak Keys
Input
Ciphertext
Second encryption
Data Input
Weak Keys
Input
Ciphertext

## Page 231

231
⚫ Semi-weak keys in DES
- Six key pairs called semi-weak keys
- Semi-weak keys generate only two forms of the round key, each repeated eight times.
- Two semi-weak keys paired as one produce the same round key, just in a different order.
Break DES
DES semi-weak-key encryption
𝑭𝒊𝒓𝒔𝒕 𝒌𝒆𝒚 𝒊𝒏 𝒕𝒉𝒆 𝒑𝒂𝒊𝒓 𝑺𝒆𝒄𝒐𝒏𝒅 𝒌𝒆𝒚 𝒊𝒏 𝒕𝒉𝒆 𝒑𝒂𝒊𝒓
01FE 01FE 01FE 01FE FE01 FE01 FE01 FE01
1FE0 1FE0 1FE0 1FE0 E01F E01F E01F E01F
01E0 01E0 01E0 01E0 E001 E001 E001 E001
1FFE 1FFE 1FFE 1FFE FE1F FE1F FE1F FE1F
011F 011F 011F 011F 1F01 1F01 1F01 1F01
E0FE E0FE E0FE E0FE FEE0 FEE0 FEE0 FEE0

## Page 232

232
⚫ Create a ciphertext using the DES created in the previous section.
- Perform an encryption test with semi-weak keys
• Data : 12 34 56 87 65 43 21
• Key : 01 FE 01 FE 01 FE 01 FE
• Ciphertext : 07 E0 34 71 5D 41 EF DD
- Put the result of this encryption back as input and encrypt it again with the semi-weak key
pair.
• Data : 07 E0 34 71 5D 41 EF DD
• Key : FE 01 FE 01 FE 01 FE 01
• Ciphertext : 12 34 56 78 87 65 43 21
- See the source message printed when performing encryption using different keys instead of
the same key.
Break DES
DES semi-weak-key encryption

## Page 233

233
Break DES
DES semi-weak-key encryption
Data Input
Semi-Weak Keys
Input
Ciphertext
Data Input
Ciphertext
First encryption Second encryption
Semi-Weak Keys
Input

## Page 234

234
Break hash with Hashcat
⚫ Hashcat is a CPU-based password recovery tool
- GPU-enabled variants of oclHashcat/cudaHashcat also exist
- Based on flaws in other software discovered by Hashcat's creators
- Many algorithms supported by legacy Hashcat can be cracked in a fraction of the time with
GPU-based Hashcat.
- Not all algorithms are GPU accelerated.
• Bcrypt : not available due to factors such as data-dependent branching, serialization, and
memory.
Hashcat is a password recovery tool and open source software. Algorithms that can be cracked
with Hashcat include LM hash, MD4, MD5, and the SHA family.
Hashcat

## Page 235

235
Break hash with Hashcat
⚫ Types of attacks supported by Hashcat
- Brute force/dictionary attack
- Combinator attack
- Fingerprint attack
- Hybrid attack
- Mask attack
- Permutation attack
- Rule-based attack
- Table-lookup attack (CPU only)
- Toggle-case attack
- PRINCE attack (in CPU version 0.48 or later only)
Hashcat is a password recovery tool and open source software. Algorithms that can be cracked
with Hashcat include LM hash, MD4, MD5, and the SHA family.
Hashcat

## Page 236

236
⚫ How to crack with Hashcat
- Download a cracking tool, Hashcat.
• Virtual machine (X)
▪ Not used because GPUs are hard to use in virtual machines
- Copy the created dictionary file you created (wordlist.txt) and the extracted WordPress
password (passwd.txt).
Break hash with Hashcat
Hashcat

## Page 237

237
⚫ How to crack with Hashcat
- Start cracking as follows :
- Crack command can be found at https://hashcat.net/wiki/doku.php?id=hashcat
Break hash with Hashcat
Hashcat
hashcat.exe -a 3 -m 0 -d 2 test.txt -o testcrack.txt

## Page 238

238
⚫ How to crack with Hashcat
- When the crack is complete, a crack.txt is generated that stores the hash and password.
- Alternatively, you can use the following command to check.
Break hash with Hashcat
Hashcat
hashcat.exe -a 3 -m 0 -d 2 test.txt --show

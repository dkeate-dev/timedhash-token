# py-time-stamp

py-time-stamp is a proof of stake blockchain verification system for storing time-stamped hashes of data. 

The intent of this project is to remove centralized authorities from the file signing and time stamping process. Organizations like the [FreeTSA](https://freetsa.org) have come a long way in increasing the accessibility of time stamping, it is still an authority based system that requires an inherent trust in the service provider.

py-time-stamp aims to remove authority requirements and hold it in the public trust using the inherent verfiability of a consensus-based blockchain.

Why is this in python? Who knows&#x203D;

## Contributing

Created by [Dustin Keate](https://dkeate.dev)

I have no idea what I'm doing.

# Roadmap

## Basic Implementation

* &#x2610; Figure out where to put signature data
* &#x2611; Create hashable.py module
    * &#x2611; Hashes files and strings using SHA256
    * &#x2611; Create Hashable class
* &#x2610; Create block.py module
    * &#x2611; Create Block class
    * &#x2610; Add transaction tree and tree hash to Block
* &#x2610; Create transaction.py module
    * &#x2610; Create Transaction(Hashable) class
* &#x2611; Create wallet.py module
    * &#x2611; Create Wallet(Hashable) class
    * &#x2611; Validate signatures
* &#x2610; Create tree.py module
    * &#x2611; Create Node(Hashable) class
    * &#x2610; Create HeadNode(Node) class
    * &#x2610; Improve Tree functionality
* &#x2610; Create additional Transaction types
    * &#x2610; NewWallet
    * &#x2610; Transfer
    * &#x2610; Signature

## Long Term Ideas

* Save / export to flat file / db (import, too!)
    * SQLite
* Network
* Block Consensus
* Staking and Payment
* Time Consensus
* Create Request(Transaction) class
    * TimeRequest
    * ValidationRequest (if needed)
* Internal standards implementations
    * base58
    * SHA256
    * RSA

# License

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2023 Dustin Keate

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
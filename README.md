## CertiChain

CertiChain is a blockchain-based certificate verification system built with Python and Django.  
It aims to reduce certificate forgery by storing cryptographic hashes of certificates on a simple blockchain, enabling quick and reliable verification.

🚧 **Status: Under Construction**

This project is currently in active development. Core blockchain functionality such as block creation, mining, and certificate verification is implemented and being tested. Django backend integration is still in progress.

### 🔍 Core Idea
- Certificate data is converted into a unique SHA-256 hash
- Each hash is stored inside a blockchain block
- Verification checks whether a certificate hash exists on the blockchain

### ⚙️ Tech Stack
- Python
- Django
- SHA-256 Hashing
- Custom Blockchain (Proof of Work)

### 📌 Note
This project is still under construction.  
There is currently no public setup or usage guide available. Documentation and features will be added as development continues.

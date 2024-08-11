
# Vigenère and Vernam Cipher Encryption/Decryption Tool

This project is a Python implementation of two classical cryptography techniques: the Vigenère Cipher and the Vernam Cipher. It allows users to encrypt and decrypt messages using either cipher method through a simple command-line interface.

## Features

- **Vigenère Cipher**: 
  - Encrypt plaintext using a keyword.
  - Decrypt ciphertext using the same keyword.
  
- **Vernam Cipher**: 
  - Encrypt plaintext using a keyword of the same length.
  - Decrypt ciphertext using the same keyword.
  
## Prerequisites

- Python 3.x

## How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/thesaajii/Cryptography.git
   cd cipher-tool
   ```

2. **Run the Script:**

   ```bash
   python3 cipher.py
   ```

3. **Choose the Cipher Method:**

   - Select **1** for Vigenère Cipher.
   - Select **2** for Vernam Cipher.

4. **Choose the Operation:**

   - Select **1** for Encryption.
   - Select **2** for Decryption.

5. **Input the Required Data:**

   - For Vigenère Cipher: Input the plaintext/ciphertext and keyword.
   - For Vernam Cipher: Input the plaintext/ciphertext and a keyword of the same length.

6. **View the Result:**

   - The program will output the encrypted or decrypted text.

## Example

### Vigenère Cipher

- **Encrypting**:
  - Plaintext: `HELLO`
  - Keyword: `KEY`
  - Ciphertext: `RIJVS`

- **Decrypting**:
  - Ciphertext: `RIJVS`
  - Keyword: `KEY`
  - Plaintext: `HELLO`

### Vernam Cipher

- **Encrypting**:
  - Plaintext: `HELLO`
  - Keyword: `XMCKL`
  - Ciphertext: `EQNVZ`

- **Decrypting**:
  - Ciphertext: `EQNVZ`
  - Keyword: `XMCKL`
  - Plaintext: `HELLO`

## Notes

- The Vernam Cipher requires the keyword to be of the same length as the plaintext or ciphertext.
- The script only handles uppercase English letters (A-Z). Ensure your inputs are in uppercase.

## Contributing

Feel free to fork this repository, submit issues, and make pull requests. Contributions are always welcome!

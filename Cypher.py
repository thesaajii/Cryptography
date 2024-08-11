def vigenere_encrypt(plaintext, keyword):
    # Convert keyword to uppercase for consistency
    keyword = keyword.upper()
    key_length = len(keyword)

    # Extend the keyword to match the length of the plaintext
    keyword_sequence = (keyword * ((len(plaintext) // key_length) + 1))[:len(plaintext)]

    ciphertext = ""
    for p, k in zip(plaintext, keyword_sequence):
        p_idx = ord(p) - ord('A')
        k_idx = ord(k) - ord('A')
        c_idx = (p_idx + k_idx) % 26
        ciphertext += chr(c_idx + ord('A'))

    return ciphertext


def vigenere_decrypt(ciphertext, keyword):
    # Convert keyword to uppercase for consistency
    keyword = keyword.upper()
    key_length = len(keyword)

    # Extend the keyword to match the length of the ciphertext
    keyword_sequence = (keyword * ((len(ciphertext) // key_length) + 1))[:len(ciphertext)]

    plaintext = ""
    for c, k in zip(ciphertext, keyword_sequence):
        c_idx = ord(c) - ord('A')
        k_idx = ord(k) - ord('A')
        p_idx = (c_idx - k_idx + 26) % 26
        plaintext += chr(p_idx + ord('A'))

    return plaintext


def vernam_encrypt(plaintext, keyword):
    # Check if plaintext and keyword are of the same length
    if len(plaintext) != len(keyword):
        raise ValueError("For Vernam Cipher, the plaintext and keyword must be of the same length.")

    ciphertext = ""
    for p, k in zip(plaintext, keyword):
        p_idx = ord(p) - ord('A')
        k_idx = ord(k) - ord('A')
        c_idx = p_idx ^ k_idx
        ciphertext += chr(c_idx + ord('A'))

    return ciphertext


def vernam_decrypt(ciphertext, keyword):
    # Check if ciphertext and keyword are of the same length
    if len(ciphertext) != len(keyword):
        raise ValueError("For Vernam Cipher, the ciphertext and keyword must be of the same length.")

    plaintext = ""
    for c, k in zip(ciphertext, keyword):
        c_idx = ord(c) - ord('A')
        k_idx = ord(k) - ord('A')
        p_idx = c_idx ^ k_idx
        plaintext += chr(p_idx + ord('A'))

    return plaintext


def main():
    # Display cipher method choices
    print("Choose cipher method:")
    print("1. Vigenère Cipher")
    print("2. Vernam Cipher")
    cipher_choice = input("Enter your choice (1 or 2): ")

    if cipher_choice == '1':
        # Vigenère Cipher chosen
        print("\nFor Vigenère Cipher:")
        print("Choose operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        operation_choice = input("Enter your choice (1 or 2): ")

        if operation_choice == '1':
            # Encrypt with Vigenère Cipher
            plaintext = input("Enter plaintext: ").upper()
            keyword = input("Enter keyword: ").upper()
            ciphertext = vigenere_encrypt(plaintext, keyword)
            print("Ciphertext:", ciphertext)
        elif operation_choice == '2':
            # Decrypt with Vigenère Cipher
            ciphertext = input("Enter ciphertext: ").upper()
            keyword = input("Enter keyword: ").upper()
            plaintext = vigenere_decrypt(ciphertext, keyword)
            print("Plaintext:", plaintext)
        else:
            print("Invalid operation choice")

    elif cipher_choice == '2':
        # Vernam Cipher chosen
        print("\nFor Vernam Cipher:")
        print("Choose operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        operation_choice = input("Enter your choice (1 or 2): ")

        if operation_choice == '1':
            # Encrypt with Vernam Cipher
            plaintext = input("Enter plaintext: ").upper()
            keyword = input("Enter keyword: ").upper()
            if len(plaintext) != len(keyword):
                print("Error: For Vernam Cipher, the plaintext and keyword must be of the same length.")
            else:
                ciphertext = vernam_encrypt(plaintext, keyword)
                print("Ciphertext:", ciphertext)
        elif operation_choice == '2':
            # Decrypt with Vernam Cipher
            ciphertext = input("Enter ciphertext: ").upper()
            keyword = input("Enter keyword: ").upper()
            if len(ciphertext) != len(keyword):
                print("Error: For Vernam Cipher, the ciphertext and keyword must be of the same length.")
            else:
                plaintext = vernam_decrypt(ciphertext, keyword)
                print("Plaintext:", plaintext)
        else:
            print("Invalid operation choice")
    else:
        print("Invalid cipher method choice")


if __name__ == "__main__":
    main()

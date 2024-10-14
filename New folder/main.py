from substitution_cipher import (
    shift_cipher_encrypt,
    shift_cipher_decrypt,
    permutation_cipher_encrypt,
    permutation_cipher_decrypt
)

from transposition_cipher import (
    simple_transposition_cipher,
    double_transposition_cipher_encrypt,
    double_transposition_cipher_decrypt
)

from vigènere_cipher import (
    vigenere_cipher_encrypt,
    vigenere_cipher_decrypt
)

from additional_cipher import (
    aes_encrypt,
    aes_decrypt,
    des_encrypt,
    des_decrypt,
    des3_encrypt,
    des3_decrypt
)

from additional_cipher_modes import (
    ecb_encrypt,
    ecb_decrypt,
    cbc_encrypt,
    cbc_decrypt,
    cfb_encrypt,
    cfb_decrypt
)

# Maximum block sizes for different algorithms
BLOCK_SIZE_LIMITS = {
    'AES': 16,  # 128 bits
    'DES': 8,  # 64 bits
    '3DES': 16,  # 128 bits
}

def is_valid_text(text):
    return text.isalpha()  # Check if the text contains only alphabets

def get_aes_key(dec_flag = 0, enc=""):
    while True:
        if dec_flag == 1:
            key = input("Enter the decryption key (16 characters long) for AES-128 encryption (leave blank to use the same key as encryption): ") or enc
        else:
            key = input("Enter a key for AES-128 encryption (16 characters long): ")
        if len(key) == 16:  # Check if the key is exactly 16 characters
            return key.encode('utf-8')  # Convert to bytes
        else:
            print("Invalid key length. Please enter exactly 16 characters.")

def get_des_key(dec_flag = 0, enc="", enc_type=""):
    while True:
        if dec_flag == 1:
            key = input(f"Enter the decryption key (8 characters long) for {enc_type} encryption (leave blank to use the same key as encryption): ") or enc
        else:
            key = input(f"Enter a key for {enc_type} encryption (8 characters long): ")
        if len(key) == 8:  # Check if the key is exactly 8 characters
            return key.encode('utf-8')  # Convert to bytes
        else:
            print("Invalid key length. Please enter exactly 8 characters.")

def get_des3_key(dec_flag = 0, enc=""):
    while True:
        if dec_flag == 1:
            key = input("Enter the decryption key (16 characters long) for AES-128 encryption (leave blank to use the same key as encryption): ") or enc
        else:
            key = input("Enter a key for 3DES encryption (16 or 24 characters long): ")
        if len(key) == 16 or len(key) == 24:  # Check if the key is exactly 16, or 24 characters
            return key.encode('utf-8')  # Convert to bytes
        else:
            print("Invalid key length. Please enter exactly 16 or 24 characters.")

def main():
    while True:
        print("\nChoose an encryption technique:")
        print("1. Substitution Cipher")
        print("   1.1 Shift Cipher")
        print("   1.2 Permutation Cipher")
        print("2. Transposition Ciphers")
        print("   2.1 Simple Transposition")
        print("   2.2 Double Transposition")
        print("3. Vigenère Cipher")
        print("4. AES-128")
        print("5. DES")
        print("6. 3DES")
        print("7. ECB Mode")
        print("8. CBC Mode")
        print("9. CFB Mode")
        print("10. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '10':
            print("Exiting...")
            break

        text = input("Enter the message (plaintext): ")
        text = text.upper()
        if not is_valid_text(text):
            print("Invalid input. Please enter a text that contains only alphabets.")
            continue

        # Check message size limit based on the selected algorithm
        if choice in ['4', '5', '6'] and len(text) <= BLOCK_SIZE_LIMITS['AES']:
            print("Message size must be greater than the block size of the algorithm. Please try again.")
            continue

        if choice == '1.1':  # Shift Cipher
            encryption_key = input("Enter the encryption key (leave blank for default value = 3): ") or 3
            encrypted_text = shift_cipher_encrypt(text, encryption_key)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_key = input("Enter the decryption key (leave blank to use the same key as encryption): ") or encryption_key
                decrypted_text = shift_cipher_decrypt(encrypted_text, decryption_key)
                print("Decrypted Text:", decrypted_text)
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        elif choice == '1.2':  # Permutation Cipher
            permutation_input = input("Enter the permutation as space-separated indices (e.g., '2 0 1') : ")
            permutation = list(map(int, permutation_input.split()))
            encrypted_text = permutation_cipher_encrypt(text, permutation)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_permutation_input = input("Enter the decryption permutation (leave blank to use the same key as encryption): ") or permutation_input
                decryption_permutation = list(map(int, decryption_permutation_input.split()))
                decrypted_text = permutation_cipher_decrypt(encrypted_text, decryption_permutation)
                print("Decrypted Text:", decrypted_text)
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        elif choice == '2.1':  # Simple Transposition
            encryption_key = int(input("Enter the encryption key (leave blank for default value = 3): ") or 3)
            while len(text) >= (encryption_key * encryption_key):
                print("The message length must be less than the square of the key length.")
                encryption_key = int(input("Enter the encryption key (leave blank for default value = 3): ") or 3)
            encrypted_text = simple_transposition_cipher(text, encryption_key)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_key = input("Enter the decryption key (leave blank to use the same key as encryption): ") or encryption_key
                decrypted_text = simple_transposition_cipher(encrypted_text, decryption_key)
                print("Decrypted Text:", decrypted_text)
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        elif choice == '2.2':  # Double Transposition
            # Input for the first key (row permutation)
            key1_input = input("Enter the first transposition key (row permutation) as space-separated indices: ")
            key1 = list(map(int, key1_input.split()))
            # Input for the second key (column permutation)
            key2_input = input("Enter the second transposition key (column permutation) as space-separated indices: ")
            key2 = list(map(int, key2_input.split()))
            while len(text) > (len(key1) * len(key2)):
                print("The message length must be less than the product of lengths of row and column permutation key, otherwise loss of message may occur.")
                key1_input = input("Enter the first transposition key (row permutation) as space-separated indices: ")
                key1 = list(map(int, key1_input.split()))
                key2_input = input("Enter the second transposition key (column permutation) as space-separated indices: ")
            # Perform the encryption
            encrypted_text = double_transposition_cipher_encrypt(text, key1, key2)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_key1_input = input("Enter the first transposition key (row permutation) for decryption as space-separated indices (leave blank to use the same key as encryption): ") or key1_input
                decrypted_key1 = list(map(int, decryption_key1_input.split()))
                decryption_key2_input = input("Enter the second transposition key (column permutation) for decryption as space-separated indices (leave blank to use the same key as encryption): ") or key2_input
                decrypted_key2 = list(map(int, decryption_key2_input.split()))
                decrypted_text = double_transposition_cipher_decrypt(encrypted_text, decrypted_key1, decrypted_key2)
                print("Decrypted Text:", decrypted_text)
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        elif choice == '3':  # Vigenère Cipher
            encryption_key = input("Enter the encryption key (leave blank for default value = VIG): ") or "VIG"
            encryption_key = encryption_key.upper()
            encrypted_text = vigenere_cipher_encrypt(text, encryption_key)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_key = input("Enter the decryption key (leave blank to use the same key as encryption): ") or encryption_key
                decrypted_text = vigenere_cipher_decrypt(encrypted_text, decryption_key)
                print("Decrypted Text:", decrypted_text)
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        elif choice == '4':  # AES
            encryption_key = get_aes_key()
            plaintext_bytes = text.encode('utf-8')
            encrypted_text, iv = aes_encrypt(plaintext_bytes, encryption_key)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_key = get_aes_key(1, encryption_key.decode('utf-8'))
                decrypted_text = aes_decrypt(encrypted_text, decryption_key, iv)
                print("Decrypted Text:", decrypted_text.decode('utf-8'))
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        elif choice == '5':  # DES
            encryption_key = get_des_key(enc_type='DES')
            plaintext_bytes = text.encode('utf-8')
            encrypted_text, iv = des_encrypt(plaintext_bytes, encryption_key)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_key = get_des_key(1, encryption_key.decode('utf-8'), 'DES')
                decrypted_text = des_decrypt(encrypted_text, decryption_key, iv)
                print("Decrypted Text:", decrypted_text.decode('utf-8'))
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        elif choice == '6':  # 3DES
            encryption_key = get_des3_key()
            plaintext_bytes = text.encode('utf-8')
            encrypted_text, iv = des3_encrypt(plaintext_bytes, encryption_key)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_key = get_des3_key(1, encryption_key.decode('utf-8'))
                decrypted_text = des3_decrypt(encrypted_text, decryption_key, iv)
                print("Decrypted Text:", decrypted_text.decode('utf-8'))
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        elif choice == '7':  # ECB Mode
            encryption_key = get_des_key(enc_type='ECB')
            plaintext_bytes = text.encode('utf-8')
            encrypted_text = ecb_encrypt(plaintext_bytes, encryption_key)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_key = get_des_key(1, encryption_key.decode('utf-8'), "ECB")
                decrypted_text = ecb_decrypt(encrypted_text, decryption_key)
                print("Decrypted Text:", decrypted_text.decode('utf-8'))
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        elif choice == '8':  # CBC Mode
            encryption_key = get_des_key(enc_type='CBC')
            plaintext_bytes = text.encode('utf-8')
            encrypted_text, iv = cbc_encrypt(plaintext_bytes, encryption_key)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_key = get_des_key(1, encryption_key.decode('utf-8'), "CBC")
                decrypted_text = cbc_decrypt(encrypted_text, decryption_key, iv)
                print("Decrypted Text:", decrypted_text.decode('utf-8'))
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        elif choice == '9':  # CFB Mode
            encryption_key = get_des_key(enc_type='CFB')
            plaintext_bytes = text.encode('utf-8')
            encrypted_text, iv = cfb_encrypt(plaintext_bytes, encryption_key)
            print("Encrypted Text:", encrypted_text)

            # Ask if the user wants to decrypt the encrypted text
            decrypt_flag = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
            if decrypt_flag == 'yes':
                decryption_key = get_des_key(1, encryption_key.decode('utf-8'), "CFB")
                decrypted_text = cfb_decrypt(encrypted_text, decryption_key, iv)
                print("Decrypted Text:", decrypted_text.decode('utf-8'))
            elif decrypt_flag == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
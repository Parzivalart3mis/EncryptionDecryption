def create_vigenere_table():
    # Create the Vigenère cipher table
    table = []
    for i in range(26):
        # Generate a row with shifted letters
        row = [(chr((i + j) % 26 + ord('A'))) for j in range(26)]
        table.append(row)

    return table

def extend_key(plaintext, key):
    # Extend the key to match the length of the plaintext
    extended_key = []
    key_length = len(key)

    for i in range(len(plaintext)):
        extended_key.append(key[i % key_length])

    return ''.join(extended_key)

def char_to_index(char):
    return ord(char) - ord('A')

def index_to_char(index):
    return chr(index + ord('A'))

def vigenere_cipher_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ""
    vigenere_table = create_vigenere_table()
    extended_key = extend_key(plaintext, key)
    for i in range(len(plaintext)):
        char = plaintext[i]
        char_index = char_to_index(char)
        key_char = extended_key[i]
        key_char_index = char_to_index(key_char)
        ciphertext = ciphertext + vigenere_table[key_char_index][char_index]

    return ciphertext

def vigenere_cipher_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    plaintext = ""
    vigenere_table = create_vigenere_table()
    extended_key = extend_key(ciphertext, key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        char_index = char_to_index(char)
        key_char = extended_key[i]
        key_char_index = char_to_index(key_char)
        key_row = vigenere_table[key_char_index]
        for i in range(len(key_row)):
            key_row_char = key_row[i]
            if key_row_char == char:
                char_index = i
                plain_text_char = index_to_char(char_index)
                plaintext = plaintext + plain_text_char

    return plaintext

# # # Example usage
# plaintext = "THEBOYHASTHEBALL"
# key = "VIG"
# ciphertext = vigenere_cipher_encrypt(plaintext, key)
# print(ciphertext)
#
# decryptedtext = vigenere_cipher_decrypt(ciphertext, key)
# print(decryptedtext)
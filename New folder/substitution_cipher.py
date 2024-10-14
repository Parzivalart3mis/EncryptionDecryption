def shift_cipher_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ""
    for char in plaintext:
        shifted_char = (ord(char) - ord('A') + int(key)) % 26 + ord('A')
        ciphertext = ciphertext + chr(shifted_char)
    return ciphertext

def shift_cipher_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    plaintext = ""
    for char in ciphertext:
        shifted_char = (ord(char) - ord('A') - int(key)) % 26 + ord('A')
        plaintext = plaintext + chr(shifted_char)
    return plaintext

def permutation_cipher_encrypt(plaintext, permutation):
    permutation = [p - 1 for p in permutation]
    # Ensure plaintext length matches permutation length
    if len(plaintext) % len(permutation) != 0:
        # Padding plaintext to fit permutation
        padding_length = len(permutation) - (len(plaintext) % len(permutation))
        plaintext += 'X' * padding_length  # Padding with 'X' or any character

    ciphertext = []
    # Encrypting by applying the permutation
    for i in range(0, len(plaintext), len(permutation)):
        block = plaintext[i:i + len(permutation)]
        encrypted_block = [''] * len(permutation)
        for j in range(len(permutation)):
            encrypted_block[permutation[j]] = block[j]
        ciphertext.append(''.join(encrypted_block))

    return ''.join(ciphertext)

def permutation_cipher_decrypt(ciphertext, permutation):
    permutation = [p - 1 for p in permutation]
    # Creating the inverse permutation
    inverse_permutation = [0] * len(permutation)
    for index, value in enumerate(permutation):
        inverse_permutation[value] = index

    plaintext = []
    # Decrypting by applying the inverse permutation
    for i in range(0, len(ciphertext), len(permutation)):
        block = ciphertext[i:i + len(permutation)]
        decrypted_block = [''] * len(permutation)
        for j in range(len(permutation)):
            decrypted_block[inverse_permutation[j]] = block[j]
        plaintext.append(''.join(decrypted_block))

    return ''.join(plaintext).rstrip('X')  # Removing padding
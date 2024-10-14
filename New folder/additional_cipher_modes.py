from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Function to encrypt data using ECB mode
def ecb_encrypt(data, key):
    # Ensure key is 8 bytes long for DES
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long for DES.")

    # Create a DES cipher object in ECB mode
    cipher = DES.new(key, DES.MODE_ECB)

    # Encrypt the data after padding it to the block size
    ciphertext = cipher.encrypt(pad(data, DES.block_size))

    return ciphertext

# Function to decrypt data using ECB mode
def ecb_decrypt(ciphertext, key):
    # Ensure key is 8 bytes long for DES
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long for DES.")

    # Create a DES cipher object for decryption in ECB mode
    cipher = DES.new(key, DES.MODE_ECB)

    # Decrypt and unpad the data
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)

    return plaintext

# Function to encrypt data using CBC mode
def cbc_encrypt(data, key):
    # Ensure the key is 8 bytes long for DES
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long for DES.")

    # Create a DES cipher object in CBC mode
    cipher = DES.new(key, DES.MODE_CBC)
    iv = cipher.iv  # Save the IV for decryption

    # Encrypt the data after padding it to the block size
    ciphertext = cipher.encrypt(pad(data, DES.block_size))

    return ciphertext, iv

# Function to decrypt data using CBC mode
def cbc_decrypt(ciphertext, key, iv):
    # Ensure the key is 8 bytes long for DES
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long for DES.")

    # Create a DES cipher object for decryption in CBC mode
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)

    # Decrypt and unpad the data
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)

    return plaintext

# Function to encrypt data using CFB mode
def cfb_encrypt(data, key):
    # Ensure the key is 8 bytes long for DES
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long for DES.")

    # Create a DES cipher object in CFB mode
    cipher = DES.new(key, DES.MODE_CFB)
    iv = cipher.iv  # Save the IV for decryption

    # Encrypt the data
    ciphertext = cipher.encrypt(data)

    return ciphertext, iv


# Function to decrypt data using CFB mode
def cfb_decrypt(ciphertext, key, iv):
    # Ensure the key is 8 bytes long for DES
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long for DES.")

    # Create a DES cipher object for decryption in CFB mode
    cipher = DES.new(key, DES.MODE_CFB, iv=iv)

    # Decrypt the data
    plaintext = cipher.decrypt(ciphertext)

    return plaintext
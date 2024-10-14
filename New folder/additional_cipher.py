from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

# Function to encrypt data
def aes_encrypt(data, key):
    # Ensure key is 16 bytes for AES-128
    if len(key) != 16:
        raise ValueError("Key must be 16 bytes long (AES-128).")

    # Create a cipher object using AES in CBC mode
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv  # Save the IV for decryption

    # Encrypt the data after padding it to the block size
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    # Return the ciphertext and the IV
    return ciphertext, iv


# Function to decrypt data
def aes_decrypt(ciphertext, key, iv):
    # Ensure key is 16 bytes for AES-128
    if len(key) != 16:
        raise ValueError("Key must be 16 bytes long (AES-128).")

    # Create a new cipher object for decryption using the same IV
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # Decrypt and unpad the data
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return plaintext

# Function to encrypt data
def des_encrypt(data, key):
    # Ensure key is 8 bytes long
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long for DES.")

    # Create a DES cipher object in CBC mode
    cipher = DES.new(key, DES.MODE_CBC)
    iv = cipher.iv  # Save the IV for decryption

    # Encrypt the data after padding it to the block size
    ciphertext = cipher.encrypt(pad(data, DES.block_size))

    # Return the ciphertext and the IV
    return ciphertext, iv


# Function to decrypt data
def des_decrypt(ciphertext, key, iv):
    # Ensure key is 8 bytes long
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long for DES.")

    # Create a new DES cipher object for decryption
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)

    # Decrypt and unpad the data
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)

    return plaintext

# Function to encrypt data using 3DES
def des3_encrypt(data, key):
    # Ensure the key is either 16 bytes (2-key 3DES) or 24 bytes (3-key 3DES)
    if len(key) not in {16, 24}:
        raise ValueError("Key must be 16 or 24 bytes long for 3DES.")

    # Create a 3DES cipher object in CBC mode
    cipher = DES3.new(key, DES3.MODE_CBC)
    iv = cipher.iv  # Save the IV for decryption

    # Encrypt the data after padding it to the block size
    ciphertext = cipher.encrypt(pad(data, DES3.block_size))

    # Return the ciphertext and the IV
    return ciphertext, iv

# Function to decrypt data using 3DES
def des3_decrypt(ciphertext, key, iv):
    # Ensure the key is either 16 bytes (2-key 3DES) or 24 bytes (3-key 3DES)
    if len(key) not in {16, 24}:
        raise ValueError("Key must be 16 or 24 bytes long for 3DES.")

    # Create a new 3DES cipher object for decryption
    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)

    # Decrypt and unpad the data
    plaintext = unpad(cipher.decrypt(ciphertext), DES3.block_size)

    return plaintext
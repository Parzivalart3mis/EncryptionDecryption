def create_decryption_position_array(permutation):
    # Initialize an array with the same length as col_permutation
    decryption_position = [0] * len(permutation)

    # Fill the decryption position array
    for original_index, new_index in enumerate(permutation):
        decryption_position[new_index - 1] = original_index + 1  # Adjust for 1-based to 0-based index

    return decryption_position

def simple_transposition_cipher(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ""
    cipher_matrix = [['x' for _ in range(key)] for _ in range(key)]  # Use 'x' as padding
    # Fill the matrix row by row
    index = 0
    for row in range(key):
        for col in range(key):
            if index < len(plaintext):
                # Replace spaces with 'X'
                if plaintext[index] == ' ':
                    cipher_matrix[row][col] = 'X'
                else:
                    cipher_matrix[row][col] = plaintext[index]
                index += 1
            else:
                cipher_matrix[row][col] = 'X'  # Fill with 'x' if plaintext ends

    for row in range(key):
        for col in range(key):
            ciphertext += cipher_matrix[col][row]

    return ciphertext

def double_transposition_cipher_encrypt(plaintext, row_permutation, col_permutation):
    plaintext = plaintext.upper()
    ciphertext = ""
    rows = len(row_permutation)
    cols = len(col_permutation)

    # Initialize the matrix for plaintext
    plain_matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0

    # Fill the plain_matrix row by row
    for row in range(rows):
        for col in range(cols):
            if index < len(plaintext):
                # Replace spaces with 'X'
                if plaintext[index] == ' ':
                    plain_matrix[row][col] = 'X'
                else:
                    plain_matrix[row][col] = plaintext[index]
                index += 1
            else:
                plain_matrix[row][col] = 'X'  # Fill with 'x' if plaintext ends

    # Apply row permutation
    temp_plain_matrix = [['' for _ in range(cols)] for _ in range(rows)]
    for i, row in enumerate(row_permutation):
        temp_plain_matrix[i] = plain_matrix[row - 1]  # 1-based to 0-based index

    # Apply column permutation
    final_matrix = [['' for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for i, col in enumerate(col_permutation):
            final_matrix[row][i] = temp_plain_matrix[row][col - 1]  # 1-based to 0-based index

    # Generate the ciphertext
    for row in range(rows):
        for col in range(cols):
            ciphertext += final_matrix[row][col]

    return ciphertext

def double_transposition_cipher_decrypt(ciphertext, row_permutation, col_permutation):
    ciphertext = ciphertext.upper()
    row_permutation = create_decryption_position_array(row_permutation)
    col_permutation = create_decryption_position_array(col_permutation)
    plaintext = ""
    rows = len(row_permutation)
    cols = len(col_permutation)

    # Initialize the matrix for ciphertext
    cipher_matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0

    # Fill the cipher_matrix row by row
    for row in range(rows):
        for col in range(cols):
            if index < len(ciphertext):
                # Replace spaces with 'X'
                if ciphertext[index] == ' ':
                    cipher_matrix[row][col] = 'X'
                else:
                    cipher_matrix[row][col] = ciphertext[index]
                index += 1
            else:
                cipher_matrix[row][col] = 'X'  # Fill with 'x' if ciphertext ends

    # Apply column permutation
    temp_cipher_matrix = [['' for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for i, col in enumerate(col_permutation):
            temp_cipher_matrix[row][i] = cipher_matrix[row][col - 1]  # 1-based to 0-based index

    # Apply row permutation
    final_matrix = [['' for _ in range(cols)] for _ in range(rows)]
    for i, row in enumerate(row_permutation):
        final_matrix[i] = temp_cipher_matrix[row - 1]  # 1-based to 0-based index

    # Generate the plaintext
    for row in range(rows):
        for col in range(cols):
            plaintext += final_matrix[row][col]

    return plaintext
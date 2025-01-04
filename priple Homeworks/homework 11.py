def vigenere(plaintext, key, direction=1):
    try:
        # Check if the inputs are valid
        if not isinstance(plaintext, str) or not isinstance(key, str):
            raise TypeError("Both 'plaintext' and 'key' must be strings.")
        if len(key) == 0:
            raise ValueError("The key cannot be an empty string.")
        if direction not in [-1, 1]:
            raise ValueError("Direction must be either 1 (encrypt) or -1 (decrypt).")
        
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = ''
        
        for i, letter in enumerate(plaintext.upper()):
            if letter in alphabet:
                shift = alphabet.index(key[i % len(key)].upper()) * direction
                new_letter = alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
                ciphertext += new_letter
            else:
                # Add non-alphabet characters without modification
                ciphertext += letter
        
        return ciphertext
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Function execution complete.")

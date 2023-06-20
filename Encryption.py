def vigenere_encrypt(message, key):
    ciphertext = ""
    for i, letter in enumerate(message):
        ciphertext += chr((ord(letter) + ord(key[i % len(key)]) - 97) % 26 + 97)
    return ciphertext

def main():
    message = input("Enter the message to encrypt:")
    key = input("Enter the key:")
    print("The encrypted message is:", vigenere_encrypt(message, key))
    
if __name__ == "__main__":
    main()
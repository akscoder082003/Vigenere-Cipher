def encrypt_vigenere(plaintext, keyword):
    encrypted_text = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    plaintext = plaintext.upper()
    
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            keyword_index = i % keyword_length
            shift = ord(keyword[keyword_index]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

plaintext = input("Enter plaintext: ")
keyword = input("Enter keyword: ")
print("Encrypted text:", encrypt_vigenere(plaintext, keyword))
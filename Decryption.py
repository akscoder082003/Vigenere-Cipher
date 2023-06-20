def decrypt_vigenere(ciphertext, keyword):
    decrypted_text = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    ciphertext = ciphertext.upper()
    
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            keyword_index = i % keyword_length
            shift = ord(keyword[keyword_index]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

ciphertext = input("Enter ciphertext: ")
keyword = input("Enter keyword: ")
print("Decrypted text:", decrypt_vigenere(ciphertext, keyword))
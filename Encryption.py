
# Encrypts plaintext using Vigenere cipher with keyword

def encrypt_vigenere(plaintext, keyword): 
    encrypted_text = "" #create empty string for encrypted text
    keyword = keyword.upper() #make keyword uppercase 
    keyword_length = len(keyword) #get length of keyword
    plaintext = plaintext.upper() #make plaintext uppercase
    
    for i in range(len(plaintext)): #loop through plaintext
        char = plaintext[i] #get character at index i
        if char.isalpha(): #check if character is a letter
            keyword_index = i % keyword_length #get index of keyword
            shift = ord(keyword[keyword_index]) - ord('A') #get shift value
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A')) #get encrypted character
            encrypted_text += encrypted_char #add encrypted character to encrypted text
        else: #if character is not a letter
            encrypted_text += char #add character to encrypted text
    
    return encrypted_text #return encrypted text

plaintext = input("Enter plaintext: ") 
keyword = input("Enter keyword: ")
print("Encrypted text:", encrypt_vigenere(plaintext, keyword))
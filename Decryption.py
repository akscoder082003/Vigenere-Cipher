
#decrypts a ciphertext using a keyword and the Vigenere cipher 

def decrypt_vigenere(ciphertext, keyword):  
    decrypted_text = "" #create empty string for decrypted text
    keyword = keyword.upper() #make keyword uppercase 
    keyword_length = len(keyword) #get length of keyword
    ciphertext = ciphertext.upper() #make ciphertext uppercase
    
    for i in range(len(ciphertext)): #loop through ciphertext
        char = ciphertext[i] #get character at index i  
        if char.isalpha():  #check if character is a letter
            keyword_index = i % keyword_length #get index of keyword
            shift = ord(keyword[keyword_index]) - ord('A')  #get shift value 
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A')) #get decrypted character
            decrypted_text += decrypted_char #add decrypted character to decrypted text
        else:  #if character is not a letter
            decrypted_text += char #add character to decrypted text
    
    return decrypted_text #return decrypted text

ciphertext = input("Enter ciphertext: ") 
keyword = input("Enter keyword: ") 
print("Decrypted text:", decrypt_vigenere(ciphertext, keyword)) 
import string

class Vigenere:
    def __init__(self, key):
        """Initialize the Vigenere cipher with a given Key."""
        self.key = key.lower()
        self.alphabet = string.ascii_lowercase

    def encryption(self, plaintext):
        """Encrypt the plaintext by using Vigenere"""
        self.store_space(plaintext)
        ciphertext = ""
        plaintext = plaintext.replace(" ", "").lower()
        self.ready_encryption_key(plaintext)
        for i in range(len(self.key)):
            index = (self.alphabet.index(self.key[i])+self.alphabet.index(plaintext[i])) %26
            ciphertext+=self.alphabet[index]
        for i in self.storeList:  
            ciphertext = ciphertext[:i] + " " + ciphertext[i:]  
        return ciphertext

    def store_space(self,text):
        """Store Space in the text"""
        self.storeList = []
        for i in range(len(text)):
            if text[i] == " ":
                self.storeList.append(i)
        

    def ready_encryption_key(self, plaintext):
        """Ready for size of the key"""
        if len(self.key) < len(plaintext):
            self.key += plaintext[:len(plaintext) - len(self.key)] 
        elif len(self.key) > len(plaintext):
            self.key = self.key[:len(plaintext)]

    def decryption(self,ciphertext):
        """Decrypt the ciphertext by using Vigenere"""
        self.store_space(ciphertext)
        ciphertext = ciphertext.replace(" ","").lower()
        plaintext = ""
        if len(self.key) < len(ciphertext):
            plaintext = self.ready_decryption_key(ciphertext)
        else:
            for i in range(len(ciphertext)):
                index = (self.alphabet.index(ciphertext[i])-self.alphabet.index(self.key[i])) %26
                plaintext+=self.alphabet[index]
        for i in self.storeList:  
            plaintext = plaintext[:i] + " " + plaintext[i:]  
        return plaintext


    def ready_decryption_key(self,ciphertext):
        """Ready to convert ciphertext to plaintext"""
        plaintext = ""
        std = self.key
        tmp = ciphertext[len(plaintext):]
        while True:
            ptr = ""
            for i in range(len(std)):
                index = (self.alphabet.index(tmp[i])-self.alphabet.index(std[i])) %26
                ptr+=self.alphabet[index]
            plaintext += ptr
            tmp = ciphertext[len(plaintext):]
            if(len(tmp)<len(ptr)):
                ptr = ptr[:len(tmp)]
            self.key+=ptr
            std = ptr
            if(tmp == ""):
                break
        return plaintext    



#Run the code
key = input("Please enter key: ")
V = Vigenere(key)
choose = input("Enter 1 for encryption or 2 for decryption: ")
while choose not in ['1', '2']:
    print("Please enter either 1 or 2.")
    choose = input("Enter 1 for encryption or 2 for decryption: ")

text = input("Please enter the text: ")


if choose == '1':
    print("Encrypted text:", V.encryption(text))
else:
    print("Decrypted text:", V.decryption(text))
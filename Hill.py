import numpy as np
import string

class Hill:
    def __init__(self, number):
        """Initialize the Hill cipher with a given number and fill the matrix with user input."""
        self.number = number
        self.alphabet = string.ascii_lowercase
        self.matrixKey = [["" for _ in range(self.number)] for _ in range(self.number)]
        for i in range(self.number):
            for ii in range(self.number):
                self.matrixKey[i][ii] = int(input("Fill the matrix: ")) % 26

        self.matrixKey = np.array(self.matrixKey)
                
       
                
    def ready(self, text):
        """Split the text into pairs based on the matrix size."""
        text = text.lower()
        pairs = []
        i = 0
        while i < len(text):
            pair = text[i:i + self.number]
            if len(pair) < self.number: 
                size = len(pair)
                while(size != self.number):
                    pair += self.alphabet[26-(self.number-size)]
                    size+=1
            pairs.append([self.alphabet.index(letter) for letter in pair if letter in self.alphabet])
            i += self.number
        return pairs
    
    def encryption_pair(self, pair):
        """Encrypt a pair using the Hill cipher."""
        array2 = np.array([pair])  
        result = np.dot(array2, self.matrixKey)
        return [self.alphabet[index % 26] for index in result[0]]
    
    def encryption(self,plaintext):
        """Encrypt the plaintext to be ciphertext using hill cipher"""
        self.store_space(plaintext)
        plaintext = plaintext.replace(" ","")
        plaintext_pairs = self.ready(plaintext)
        ciphertext = ""
        for pair in plaintext_pairs:
            pair = self.encryption_pair(pair)
            for letter in pair :
                ciphertext+=letter
        for i in self.storeList:  
            ciphertext = ciphertext[:i] + " " + ciphertext[i:]  
        return ciphertext
    
    def decryption_pair(self, pair):
        """Decrypt a pair using the Hill cipher."""
        array1 = self.reverseKey()
        array2 = np.array([pair]) 
        result = np.dot(array2, array1) % 26
        return [self.alphabet[index] for index in result[0]]
    
    def decryption(self,ciphertext):
        """Decrypt the ciphertext  to be plaintext using hill cipher"""
        ciphertext = ciphertext.replace(" ","")
        ciphertext_pairs = self.ready(ciphertext)
        plaintext = ""
        for pair in ciphertext_pairs:
            pair = self.decryption_pair(pair)
            for letter in pair:
                plaintext+=letter
        return plaintext

    def reverseKey(self):
        """Ready for Reverse Matrix"""
        self.det_rev = np.linalg.det(self.matrixKey)
        self.det_rev %= 26
        self.det_rev = round(self.det_rev)
        self.det_rev = self.MIVdet()
        matrix = self.adjoint()
        matrix = self.det_rev * matrix  
        matrix = matrix % 26
        return matrix  
        

    def can_be_decryption(self):
        """Can be decryption or not"""
        self.det_rev = np.linalg.det(self.matrixKey)
        self.det_rev %= 26
        self.det_rev = round(self.det_rev)
        if(self.det_rev%2!=0):
            return True
        return False

    def store_space(self,text):
        """Store Space in the text"""
        self.storeList = []
        for i in range(len(text)):
            if text[i] == " ":
                self.storeList.append(i)

    def MIVdet(self):
        """Get the MIV for the det in the matrix"""
        for i in range(26):
            if (i*self.det_rev) %26 == 1:
                return i
            
    def adjoint(self):
        """Getting the adjoint matrix by mod 26"""
        cofactors = []
        for r in range(len(self.matrixKey)):
            cofactor_row = []
            for c in range(len(self.matrixKey)):
                minor_matrix = np.delete(np.delete(self.matrixKey, r, axis=0), c, axis=1)
                minor_det = np.linalg.det(minor_matrix)
                cofactor = ((-1) ** (r + c)) * minor_det
                cofactor = round(cofactor)
                cofactor%=26
                cofactor_row.append(cofactor)
            cofactors.append(cofactor_row)
        
        adjoint_matrix = np.transpose(cofactors)
        
        return adjoint_matrix

#Run the code
number = int(input("Please enter the number : "))
h = Hill(number)
choose = input("Enter 1 for encryption or 2 for decryption: ")
while choose not in ['1', '2']:
    print("Please enter either 1 or 2.")
    choose = input("Enter 1 for encryption or 2 for decryption: ")

text = input("Please enter the text: ")

if choose == '1':
    print("Encrypted text:", h.encryption(text))
else:
    if(h.can_be_decryption()):
        print("Decrypted text:", h.decryption(text))
    else:
        print("The Matrix can not be invertable!!")
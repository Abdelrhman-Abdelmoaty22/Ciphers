class PLayFair:

    def __init__(self,key):
            self.key = self.remove_repeating_letters(key.lower())
            self.key = self.replace_j_with_i(self.key)
            self.KeywordList = [["" for j in range(5)] for i in range(5)]
            size = len(self.key)
            index = 0
            start = 'a'  #start from user key
            
            for i in range(5):
                for j in range(5):
                    if size != 0:
                        self.KeywordList[i][j] = self.key[index]
                        size -= 1
                        index += 1
                    else:
                        if start not in self.key:
                            self.KeywordList[i][j] = start
                            start = self.nextLetter(start)
                            if start == -1:
                                break
                        else:
                            while start in self.key:
                                start = self.nextLetter(start)
                            self.KeywordList[i][j] = start
                            start = self.nextLetter(start)
                            if start == -1:
                                break

    def Ready(self, plainText):
        """Give the word to be ready for process"""
        pairs = []
        i = 0
        while i < len(plainText) - 1:
            pair = plainText[i:i + 2]  # Extract the 
            if pair[0] == pair[1]:
                pair = pair[0] + 'x'
                pairs.append(pair)  
                i += 1  
            else:
                pairs.append(pair)  
                i += 2  
        if i == len(plainText) - 1:
            pairs.append(plainText[i] + 'x')
        return pairs


    def encrypt(self,text):
        """Encrypt a plaintext using the Playfair cipher."""
        self.store_space(text)
        text = text.replace(" ","")
        text = self.replace_j_with_i(text.lower())
        plaintext_pairs = self.Ready(text)
        ciphertext = ""
        for pair in plaintext_pairs:
            ciphertext += self.encrypt_pair(pair)
        for i in self.storeList:  
            ciphertext = ciphertext[:i] + " " + ciphertext[i:]  
        return ciphertext
    
    def encrypt_pair(self,pair):
        """Encrypt a digraph (pair of letters) using the Playfair plaintext."""
        a,b = pair
        
        row1 , col1 =self.find_value_2d(a)
        row2 , col2 =self.find_value_2d(b)
        if row2 == row1:
            enc_letter1 = self.KeywordList[row1][(col1+1)%5]
            enc_letter2 = self.KeywordList[row2][(col2+1)%5]
        
        elif col1 == col2:
            enc_letter1 = self.KeywordList[(row1+1)%5][col1]
            enc_letter2 = self.KeywordList[(row2+1)%5][col2]
        else:
            enc_letter1 = self.KeywordList[row1][col2]
            enc_letter2 = self.KeywordList[row2][col1]
        return enc_letter1 + enc_letter2
    
    def decrypt_pair(self, pair):
        """Decrypt a digraph (pair of letters) using the Playfair cipher."""
        letter1, letter2 = pair
        row1, col1 = self.find_value_2d(letter1)
        row2, col2 = self.find_value_2d(letter2)

        if row1 == row2:  # If the letters are in the same row
            decrypted_letter1 = self.KeywordList[row1][(col1 - 1) % 5]
            decrypted_letter2 = self.KeywordList[row2][(col2 - 1) % 5]
        elif col1 == col2:  # If the letters are in the same column
            decrypted_letter1 = self.KeywordList[(row1 - 1) % 5][col1]
            decrypted_letter2 = self.KeywordList[(row2 - 1) % 5][col2]
        else:  # If the letters form a rectangle
            decrypted_letter1 = self.KeywordList[row1][col2]
            decrypted_letter2 = self.KeywordList[row2][col1]

        return decrypted_letter1 + decrypted_letter2

    def decrypt(self, ciphertext):
        """Decrypt a ciphertext using the Playfair cipher."""
        self.store_space(ciphertext)
        ciphertext = ciphertext.replace(" ","")
        ciphertext = self.replace_j_with_i(ciphertext.lower())
        plaintext = ""
        ciphertext_pairs = self.Ready(ciphertext)
        for pair in ciphertext_pairs:
           plaintext += self.decrypt_pair(pair)
        for i in self.storeList:  
            plaintext = plaintext[:i] + " " + plaintext[i:]  
        return plaintext
    
    
    def remove_repeating_letters(self,word):
        """Remove repeating letters from a word."""
        unique_letters = set()     
        return ''.join(letter for letter in word if letter not in unique_letters and not unique_letters.add(letter))
    

    def nextLetter(self, letter):
        """Getting the next letter """
        if letter == 'z':
            return -1  # Signal for end of letters
        elif letter == 'i':
            return chr(ord(letter) + 2)
        else:
            return chr(ord(letter) + 1)
        
    def find_value_2d(self, value):
        """Getting location of the value in the matrix"""
        for i, row in enumerate(self.KeywordList):
            for j, element in enumerate(row):
                if element == value:
                    return (i, j)  
        return None
    
    def replace_j_with_i(self,word):
       return word.replace('j','i')
    
    def store_space(self,text):
        """Store Space in the text"""
        self.storeList = []
        for i in range(len(text)):
            if text[i] == " ":
                self.storeList.append(i)



#Run the code
key = input("please enter the keyword: ")
pl = PLayFair(str(key))

choose = input("1 for encryption \t 2 for decryption\n")
while(int(choose) != 1 and int(choose) != 2):
    print("please 1 or 2 not any another thing")
    choose = input("1 for encryption \t 2 for decryption\n")
    
if(int(choose) == 1):
    print(pl.encrypt(input("Plaese write the plaintext: ")))
else:
    print(pl.decrypt(input("Plaese write the ciphertext: "))) 
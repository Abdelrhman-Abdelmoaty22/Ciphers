class DES:
    def __init__(self, hexadecimal,key):
        """Initialize the Data Encryption Standard cipher with a given hexadecimal."""
        self.hexadecimal = hexadecimal
        self.key = key

        # Initial Permutation (IP) table
        self.IP = [58,50,42,34,26,18,10,2,
                   60,52,44,36,28,20,12,4,
                   62,54,46,38,30,22,14,6,
                   64,56,48,40,32,24,16,8,
                   57,49,41,33,25,17,9,1,
                   59,51,43,35,27,19,11,3,
                   61,53,45,37,29,21,13,5,
                   63,55,47,39,31,23,15,7]

        # Inverse Initial Permutation (IP-inverse) table
        self.IP_inverse = [40,8,48,16,56,24,64,32,
                           39,7,47,15,55,23,63,31,
                           38,6,46,14,54,22,62,30,
                           37,5,45,13,53,21,61,29,
                           36,4,44,12,52,20,60,28,
                           35,3,43,11,51,19,59,27,
                           34,2,42,10,50,18,58,26,
                           33,1,41,9,49,17,57,25]
        
        #Expansion Permutation table
        self.E = [32,1,2,3,4,5,
                  4,5,6,7,8,9,
                  8,9,10,11,12,13,
                  12,13,14,15,16,17,
                  16,17,18,19,20,21,
                  20,21,22,23,24,25,
                  24,25,26,27,28,29,
                  28,29,30,31,32,1]
        
        #Permutation Fuction table
        self.P = [16,7,20,21,29,12,28,17,
                  1,15,23,26,5,18,31,10,
                  2,8,24,14,32,27,3,9,
                  19,13,30,6,22,11,4,25]
        
        #Permution Choice one
        self.PC_1 = [57, 49, 41, 33, 25, 17, 9,
                    1, 58, 50, 42, 34, 26, 18,
                    10, 2, 59, 51, 43, 35, 27,
                    19, 11, 3, 60, 52, 44, 36,
                    63, 55, 47, 39, 31, 23, 15,
                    7, 62, 54, 46, 38, 30, 22,
                    14, 6, 61, 53, 45, 37, 29,
                    21, 13, 5, 28, 20, 12, 4]
        
        #Permution Choice two
        self.PC_2 = [14, 17, 11, 24, 1, 5,
                    3, 28, 15, 6, 21, 10,
                    23, 19, 12, 4, 26, 8,
                    16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55,
                    30, 40, 51, 45, 33, 48,
                    44, 49, 39, 56, 34, 53,
                    46, 42, 50, 36, 29, 32]
        
        self.sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

                    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

                    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

                    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

                    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

                    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

                    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

                    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
        
    def initial_permutation(self,type = "IP"):
        """Apply the Initial Permutation (IP) to the input hexadecimal."""
        pt = ""
        if(type == "IP"):
            binary = self.hex2bin(self.hexadecimal)
            for i in self.IP:
                pt += binary[i-1]
        else:
            binary = self.hex2bin(self.hexadecimal)
            for i in self.IP_inverse:
                pt += binary[i-1]
        return self.bin2hex(pt)
    
    def expansion_permuation(self,right_hand):
        """Expansion permuation of right hand 32-bit to 48-bit"""
        right_hand_bits = right_hand
        ep = ""
        for i in self.E:
            ep += right_hand_bits[i-1]
        return ep
    
    def key_rounds(self):
        """The 16 round key"""
        step_key = "" # the key with 56-bit
        key = self.hex2bin(self.key)
        for i in self.PC_1:
            step_key += key[i-1]
        keys = []
        for i in range(16):
            lh = step_key[:28]
            rh = step_key[28:]
            #Shift left
            lht,rht = "",""
            for ii in range(28):
                if i in [0,1,8,15]:
                    lht+=lh[(ii+1)%28]
                    rht+=rh[(ii+1)%28]
                else:
                    lht+=lh[(ii+2)%28]
                    rht+=rh[(ii+2)%28] 
            #Permutation chocie two
            step_key = lht+rht
            sub_key = ""
            for i in self.PC_2:
                sub_key+=step_key[i-1]
            keys.append(sub_key)
        return keys
            

    def xor(self,rk,ep):
        """Xor between bits"""        
        result = ""
        for i in range(len(rk)):
            result += str(int(rk[i])^int(ep[i]))
        return result.zfill(len(rk))
    
    def chose_permution(self,rh48):
        """chose right hand from 48 to 32 bits and Permution"""
        rh32=""
        for i in range(0,48,6):
            row_selection_bits = rh48[i] + rh48[i+5]
            col_selection_bits = rh48[i+1]+rh48[i+2]+rh48[i+3]+rh48[i+4]
            row_selection = self.bin2dec(row_selection_bits)
            col_selection = self.bin2dec(col_selection_bits)
            number = self.sbox[int(i/6)][row_selection][col_selection]
            rh32+=self.dec2bin(number)
        rh=""
        for i in self.P:
            rh += rh32[i-1]
        
        return rh            

    def rounds_encryption(self):
        """The 16 Round of DES cipher"""
        self.hexadecimal = self.initial_permutation()
        print("IP : ",self.hexadecimal)
        keys = self.key_rounds()
        binary_text = self.hex2bin(self.hexadecimal)
        for i in range(16):
            left_hand = binary_text[:32]
            right_hand = binary_text[32:]

            step_left = left_hand
            left_hand = right_hand
            ep_right_hand = self.expansion_permuation(right_hand)
            right_hand_48_bit = self.xor(keys[i],ep_right_hand)
            right_hand_32_bit = self.chose_permution(right_hand_48_bit)
            right_hand = self.xor(right_hand_32_bit,step_left)

            binary_text =  left_hand+right_hand
            if(i != 15):
                print("the round ",i+1," : ",self.bin2hex(binary_text))

        
        right_hand , left_hand = left_hand, right_hand
        binary_text = left_hand+right_hand
        print("the round ",i+1," : ",self.bin2hex(binary_text))
        self.hexadecimal = self.bin2hex(binary_text)

        self.hexadecimal = self.initial_permutation("IP_nverse")
        print("Encrypted text : ",self.hexadecimal)

    def rounds_decryption(self):
            """The 16 Round of DES cipher"""
            self.hexadecimal = self.initial_permutation()
            print("IP : ",self.hexadecimal)
            keys = self.key_rounds()
            binary_text = self.hex2bin(self.hexadecimal)
            for i in range(15,-1,-1):
                left_hand = binary_text[:32]
                right_hand = binary_text[32:]

                step_left = left_hand
                left_hand = right_hand
                ep_right_hand = self.expansion_permuation(right_hand)
                right_hand_48_bit = self.xor(keys[i],ep_right_hand)
                right_hand_32_bit = self.chose_permution(right_hand_48_bit)
                right_hand = self.xor(right_hand_32_bit,step_left)

                binary_text =  left_hand+right_hand
                if(i != 0):
                    print("the round ",i+1," : ",self.bin2hex(binary_text))

            
            right_hand , left_hand = left_hand, right_hand
            binary_text = left_hand+right_hand
            print("the round ",i+1," : ",self.bin2hex(binary_text))
            self.hexadecimal = self.bin2hex(binary_text)
            self.hexadecimal = self.initial_permutation("IP_nverse")  
            print("Decryption text : ",self.hexadecimal)

    def bin2dec(self,binary):
        """Convert binary number to decimal."""
        return int(binary,2)

    def dec2bin(self,decimal):
        """Convert decimal number to binary."""
        return bin(decimal)[2:].zfill(4)

    def bin2hex(self, binary):
        """Convert a binary string to a hexadecimal string."""
        decimal_integer = int(binary, 2)
        hexadecimal_string = format(decimal_integer, 'x')
        return hexadecimal_string.zfill(16) 

    def hex2bin(self, hexadecimal):
        """Convert a hexadecimal string to a binary string."""
        decimal_integer = int(hexadecimal, 16)
        binary_string = bin(decimal_integer)[2:]  
        binary_string = binary_string.zfill(4*len(hexadecimal))
        return binary_string

#Run the code

key = input("Please enter the key: ")
choose = input("Enter 1 for encryption or 2 for decryption: ")
while choose not in ['1', '2']:
    print("Please enter either 1 or 2.")
    choose = input("Enter 1 for encryption or 2 for decryption: ")

text = input("Please enter the text: ")
D = DES(text,key)
if choose == '1':
     D.rounds_encryption()
else:
     D.rounds_decryption()



#ab1f5cdf5a106786
#0F1571C947D9E859
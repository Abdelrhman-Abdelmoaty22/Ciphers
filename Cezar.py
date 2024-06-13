import string
class Cezar:
    def __init__(self, shift):
        """Initialize the Caesar cipher with a given shift."""
        self.shift = shift
        self.alphabet = string.ascii_lowercase

    def move(self, letter, direction='encrypt'):
        """Shift a letter by the specified shift amount."""
        if direction == 'encrypt':
            index = (self.alphabet.index(letter) + self.shift) % 26
        elif direction == 'decrypt':
            index = (self.alphabet.index(letter) - self.shift) % 26
        return self.alphabet[index]

    def transform_text(self, text, direction='encrypt'):
        """Transform a given text (plaintext or ciphertext)."""
        transformed_text = ""
        for char in text:
            if char.isalpha():
                transformed_text += self.move(char, direction)
            else:
                transformed_text += char
        return transformed_text

    def encrypt(self, plaintext):
        """Encrypt plaintext using the Caesar cipher."""
        plaintext = plaintext.lower()
        return self.transform_text(plaintext)

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using the Caesar cipher."""
        ciphertext = ciphertext.lower()
        return self.transform_text(ciphertext, direction='decrypt')


# Run the code
shift = int(input("Please enter the shift number: "))
cz = Cezar(shift)

choose = input("Enter 1 for encryption or 2 for decryption: ")
while choose not in ['1', '2']:
    print("Please enter either 1 or 2.")
    choose = input("Enter 1 for encryption or 2 for decryption: ")

text = input("Please enter the text: ")

if choose == '1':
    print("Encrypted text:", cz.encrypt(text))
else:
    print("Decrypted text:", cz.decrypt(text))

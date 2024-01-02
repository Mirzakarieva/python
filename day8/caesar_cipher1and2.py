alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction= input ("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input ("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(plain_text , shift_amount):
    cipher_text=""
    for letter in plain_text:      
        order=alphabet.index(letter)
        letter = alphabet[order+shift_amount]
        cipher_text+=letter
    print("Text:",cipher_text)


def decrypt(cipher_text , shift_amount):
    real_text=""
    for letter in cipher_text:      
        order=alphabet.index(letter)
        letter = alphabet[order-shift_amount]
        real_text+=letter
    print("Text:",real_text)


if direction=="encode":
    encrypt(text , shift)
else:
    decrypt(text , shift)


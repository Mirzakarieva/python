alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction= input ("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input ("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def caesar(type , input_text , shift_amount):

    final_text=""
    for letter in input_text:      
        order=alphabet.index(letter)
        if type=="encode":
            letter = alphabet[order+shift_amount]
        else:
            letter = alphabet[order-shift_amount] 

        final_text+=letter
    print(f"{type}d text:",final_text)

caesar(direction , text , shift)
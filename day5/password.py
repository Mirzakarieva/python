import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ["!", "#", '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input ("How many letters would you like in your password?\n"))
nr_symbols = int (input ("How many symbols would you like?\n"))
nr_numbers = int (input ("How many numbers would you like?\n"))

password = []
for letter in range(0, nr_letters):
    rand_index = random.randint(0, len(letters)-1)
    password.append(letters[rand_index])
# better version
# password.append(random.choice(letters))

for number in range(0, nr_numbers):
    rand_index = random.randint(0, len(numbers)-1)
    password.append(numbers[rand_index])
# better version
# password.append(random.choice(numbers))

for symbol in range(0, nr_symbols):
    rand_index = random.randint(0, len(symbols)-1)
    password.append(symbols[rand_index])
# better version
# password.append(random.choice(symbol))

random.shuffle(password)
final_password = ''.join(password)

print(f"The password is: {final_password}")
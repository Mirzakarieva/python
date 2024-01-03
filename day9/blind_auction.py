from art import image 
print(image)
bids ={}
print("Welcome to the secret auction program.")
game = True


while game:
    name = input("What is your name?: ")
    value = input("What's your bid?: $")
    duration = input("Are there any other bidders? Type 'yes'or 'no'")
    bids[name]=value
    if duration=="no":
        game = False
    else:
        print('\n'*20)





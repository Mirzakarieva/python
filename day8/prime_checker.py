n = int(input("Check this number: "))
def prime_checker(number):
    num_mod =0
    for i in range(1, number+1):
        if number%i==0:
            num_mod+=1
    if num_mod==2:
        print("It's a prime number")
    else:
        print("It's not a prime number")

prime_checker(number=n)

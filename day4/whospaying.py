import random
names_string = input ("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

end = len(names)-1
random_index = random.randint(0, end)
random_chel = names[random_index]
print(f"{random_chel} is going to buy the meal today!")
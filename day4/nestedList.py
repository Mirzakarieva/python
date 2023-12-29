row1 = ["*" , "*", "*"]
row2 = ["*" , "*", "*"]
row3 = ["*" , "*", "*"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

coordinate = int(input("Where do you want to put the treasure?"))
a = coordinate[0]-1
b = coordinate[1]-1
map[b][a] = "x"
print(f"{row1}\n{row2}\n{row3}")


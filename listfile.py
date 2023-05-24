numbers = []

# prompt the user to enter 5 numbers
for i in range(5):
    num = input("Enter a number: ")
    numbers.append(num)

# write the list to a file
with open("listdata.txt", "w") as file:
    for num in numbers:
        file.write(num + "\n")

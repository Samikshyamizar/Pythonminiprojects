# create a list of 5 numbers input from the user
lst = []
for i in range(5):
    num = int(input("Enter a number: "))
    lst.append(num)

# write the list to a file named "data.txt
with open("data.txt", "w") as f:
    for num in lst:
        f.write(str(num) + "\n")

# read the numbers from "data.txt" and write only the even numbers to "dest.txt"
with open("data.txt", "r") as f1, open("dest.txt", "w") as f2:
    for line in f1:
        num = int(line.strip())
        if num % 2 == 0:
            f2.write(str(num) + "\n")

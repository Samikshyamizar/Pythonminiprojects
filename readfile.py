with open("FILE.TXT", "r") as file:
    for line in file:
        if line.startswith("y"):
            print(line.strip())

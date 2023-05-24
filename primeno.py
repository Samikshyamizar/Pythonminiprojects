# function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# get the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# initialize count to 0
count = 0

# loop through the range and print/count the prime numbers
print("Prime numbers in the range", start, "to", end, "are:")
for i in range(start, end + 1):
    if is_prime(i):
        print(i)
        count += 1

# display the count of prime numbers
print("There are", count, "prime numbers in the range", start, "to", end)

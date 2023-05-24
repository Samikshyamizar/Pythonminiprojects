import random

# generate a two-digit lottery number
lottery = random.randint(10, 99)

# prompt the user to enter a two-digit number
guess = int(input("Enter your two-digit guess: "))

# check for exact match
if guess == lottery:
    print("Congratulations! You win $10,000!")
    
# check for all digits match
elif guess % 10 == lottery // 10 and guess // 10 == lottery % 10:
    print("Congratulations! You win $3,000!")
    
# check for one digit match
elif guess % 10 == lottery % 10 or guess // 10 == lottery // 10 or guess % 10 == lottery // 10 or guess // 10 == lottery % 10:
    print("Congratulations! You win $1,000!")
    
# no match
else:
    print("Sorry, you did not win. The lottery number was", lottery)

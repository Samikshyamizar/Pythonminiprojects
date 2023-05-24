# get weight and height input from user
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

# convert weight and height to kilograms and meters
weight_kg = weight * 0.45359237
height_m = height * 0.0254

# calculate BMI
bmi = weight_kg / height_m ** 2

# display the BMI
print("Your BMI is:", bmi)

# interpret the BMI based on categories provided
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi <= 24.9:
    print("You have a normal weight.")
elif 25.0 <= bmi <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

num_terms = int(input("Enter number of terms: "))
a=0
b=1
if num_terms <= 0:
    print("Please enter a positive integer")
elif num_terms == 1:
    print("Fibonacci sequence up to", num_terms, "term is:")
    print(a)
else:
    print("Fibonacci sequence up to", num_terms, "terms is:")
    print(a)
    print(b)
    for i in range(2, num_terms):
        c = a + b
        print(c)
        a = b
        b= c

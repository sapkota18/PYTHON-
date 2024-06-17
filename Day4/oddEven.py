x = float(input("Enter a Number To check even or odd: "))
if x.is_integer():  # Check if the float is a whole number
    x = int(x)  # Convert the float to an integer
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")
else:
    print("Input should be an integer")

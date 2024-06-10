x = input("Enter a Number To check even or odd: ")
if '.' in x:
    print("Input should be an integer")
else:
    x = int(x)
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")

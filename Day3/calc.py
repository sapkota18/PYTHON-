# a = input("Enter Number 1: ")
# b = input("Enter Number 2: ")
# x = input("Enter 1 for add and 2 for sub: ")
# x=int(x)
# a = int(a)
# b = int(b)
# if x == "1":
#     print("Sum Is:", a + b)
# elif x=="2": 
#     print("Difference Is:", a - b)   
# else :
#     print("Difference Is:", a - b)

a = int(input("Enter a Number 1: "))
b = int(input("Enter a Number 2: "))
choice = input("Enter a Choice (Add, Sub, Div, Mul, Average): ").lower()

if choice == "add":
    print("Add:", a + b)
elif choice == "sub":
    print("Sub:", a - b)
elif choice == "div":
    print("Div:", a / b)
elif choice == "mul":
    print("Mul:", a * b)
elif choice == "average":
    print("Average:", (a + b) / 2)
else:
    print("Invalid choice")
 
 

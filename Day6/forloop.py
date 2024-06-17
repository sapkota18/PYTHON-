# for x in "kera":
#     print(x ,end=",")

# for z in range(0,4):
#     print(z)

# fruits=["apple","mango","banana"]
# for x in fruits:
#     print(x)
#     if(x=="mango"):
#       break


# fruits=["apple","mango","banana"]
# for x in fruits:
#     if(x=="mango"):
#         break
#     print(x)


# fruits=["apple","mango","banana"]
# for x in fruits:
#     if(x=="mango"):
#         continue
#     print(x)


# choice=input("Enter a number:")
# choice=int(choice)
# for x in range(1,11): 
#     print(choice,"*",x,"=",choice*x)
# list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for list in list_of_lists:
#     for x in list:
#         print(x)

# #prints even numbers in the given range
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))
# print("Even numbers are: ")
# for x in range(start, end + 1):  # Include the end in the range
#     if x % 2 == 0:  # Check if the number is even
#         print(x)


#prints sum of even numbers upto given number
# n=int(input("Enter a number: "))
# sum=0
# for z in range(1,n+1):
#     if(z%2==0):
#         sum=sum+z
# print("Sum of even numbers:", sum)  


#prints number of Digits in Number
# number=int(input("Enter a number: "))
# count=0
# for x in str(number):
#     count=count+1
# print("Number digits in number :",count)

#Checks whether the given number is Armstrong or Not
# sum = 0
# number = int(input("Enter a number:"))
# num_digits = len(str(number))
# for digit in str(number):
#     digit = int(digit)  
#     sum += digit ** num_digits  
# if number == sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")


#Displays how many even or odd from given series of input numbers
# My_list = []
# even = 0
# odd = 0
# n = int(input("How many Numbers:"))
# for x in range(1, n + 1):
#     number = int(input("Enter a number:"))
#     My_list.append(number)
#     if number % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print("Numbers are:",My_list)
# print("Number of even:", even)
# print("Number of odd:", odd)

#Removing a prime numbers from the list 
# my_list = []
# start = int(input("Enter a starting range: "))
# end = int(input("Enter an ending range:"))
# for x in range(start, end + 1):
#     my_list.append(x)
# for x in my_list[:]:  
#     factor = 0
#     for i in range(1, x + 1):
#         if x % i == 0:/
#             factor += 1
#     if factor == 2:  
#         my_list.remove(x)
# print("List without prime numbers:", my_list)

# first = 0
# second = 1
# for _ in range(50):  # Looping 50 times to generate 50 Fibonacci numbers
#     n = first + second
#     print(first, end=" ")
#     first, second = second, n

    
    


    
    




# f = open("D:\PYTHON\Day7\demo.txt", "r")
# data = f.read(5)

# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)


# print(type(data))
# print(data)

# f.close()

# import os
# with open("demo.txt","a+") as f:
#   print(f.read())
#   f.write("abc")
#   f.close()
# os.remove("demo.txt")

# with open("practice.txt","r") as f:
#    data=f.read()

# new_data=data.replace("java","python")
# print(new_data)

# with open("practice.txt","w") as f:
#    f.write(new_data)

# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if data.find(word) != -1:
#             print("found")
#         else:
#             print("not found")

# check_for_word()

# def check_for_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#         return -1

# check_for_line()

count=0
with open("practice.txt",'r' ) as f:
    data=f.read()
    print(data)
    
    # num=""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #       print(int(num))
    #       num=""
    #     else:
    #         num+=data[i]
    
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
         count+=1
    print(count)

    
  

#Abstraction
# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.__acc_no = acc_no
#         self.__acc_pass = acc_pass
    
#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1=account("1234","Abcd")
# # print(acc1.__acc_pass)
# print(acc1.reset_pass())






#private
# class person:
#     __name="ramesh"
    
#     def __hello(self):
#         print("hello")

#     def welcome(self):
#         self.__hello()
        
# p1=person()
# print(p1.welcome())






#Iheritance
# class Car:
    
#     @staticmethod
#     def start():
#         print("Car is started")
        
#     @staticmethod
#     def stop():
#          print("Car is stopped")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type
    
# car1=Fortuner("disel")
# print(car1.start())
 
 
 
 
 
#Multiple inheritance
# class A:
#     var1="Welcome"

# class B:
#     var2="To"
    
# class C(A,B):
#     var3="Python"

# c1=C()
# print(c1.var1)
# print(c1.var2)
# print(c1.var3)





#super keyword
# class Car:
#     def __init__(self,type):
#         self.type=type
    
#     @staticmethod
#     def start():
#         print("Car is started")
        
#     @staticmethod
#     def stop():
#          print("Car is stopped")

# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()

# car1=ToyotaCar("pirus","electric" )
# print(car1.type )




#class methods
# class person:
#     name="Anonymous"
    
#     # def change_Name(self,name):
#     #     self.__class__.name="Rahul"
    
#     @classmethod
#     def change_Name(cls,name):
#         cls.name=name

# p1=person()
# p1.change_Name("Rahul")
# print(p1.name)
# print(person.name)






#property decorater
# class student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"
# s1=student(98,97,99)
# print(s1.percentage)
# s1.phy=86  
# print(s1.percentage)
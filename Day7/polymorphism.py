# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
    
#     def show_numbers(self):
#         print(self.real,"i +",self.img,"j")
    
#     #dunder function
#     def __add__(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal,newImg)
    
#     #dunder function
#     def __sub__(self,num2):
#         newReal=self.real-num2.real
#         newImg=self.img-num2.img
#         return Complex(newReal,newImg)
    
# num1=Complex(1,3)
# num1.show_numbers()

# num2=Complex(4,6)
# num2.show_numbers()

# num3=num1-num2
# num3.show_numbers()

# class Circle:
#      def __init__(self,radius):
#          self.radius=radius
         
         
#      def Area(self):
#          return ((22/7)*self.radius**2)
     
#      def perimeter(self):
#          return ((22/7)*2*self.radius)


# c=Circle(21)
# print("Area=",c.Area())
# print("Perimeter=",c.perimeter())

# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
        
#     def show_details(self):
#         return f"Employee role is {self.role}, department is {self.department}, salary is {self.salary}"

# class Engineer(Employee):
#     def __init__(self, role, department, salary, name, age):
#         super().__init__(role, department, salary)
#         self.name = name
#         self.age = age

#     def show_details(self):
#         base_details = super().show_details()
#         return f"{base_details}, name is {self.name}, age is {self.age}"

 
# e1 = Employee("manager", "management", 200000)
# print(e1.show_details())

# e2 = Engineer("engineer", "IT", 50000, "Elon Musk", 40)
# print(e2.show_details())



# class Order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
        
        
#     def __gt__(self,ord2):
#         return self.price>ord2.price

# ord1=Order('chips',20)
# ord2=Order('milk',60)

# print(ord1>ord2) #false

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    # Getter method
    def get_name(self):
        return self._name
    
    # Setter method
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative")
    
    # Getter method
    def get_age(self):
        return self._age

# Create an instance of Person
person = Person("Alice", 30)

# Use getter method
print(f"Name: {person.get_name()}")
print(f"Age: {person.get_age()}")

# Use setter method
person.set_age(25)
print(f"Updated age: {person.get_age()}")
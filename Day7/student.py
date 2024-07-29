class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    @staticmethod
    def college():
        return "ABC College"
        
    def average(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("HI",self.name,"Your average marks is:",sum/3)    
        
# s1=Student("Avisar",[99,80,89])
# s1.average()
# s1.college()

s2=Student("Anish",[100,95,87])
del s2.name
print(s2.name)

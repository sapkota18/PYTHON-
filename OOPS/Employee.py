# Base class Employee
class Employee:
    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def calculate_salary(self):
        """Method to calculate the monthly salary."""
        return self.salary

    def promote(self):
        """Promote the employee by a fixed percentage."""
        self.salary += self.salary * 0.10  
        print(f"{self.name} has been promoted. New salary: {self.salary}")

    def display_details(self):
        """Display employee details."""
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

class Manager(Employee):
    def __init__(self, employee_id, name, salary, department, team_size):
        super().__init__(employee_id, name, salary, department)
        self.team_size = team_size

    def calculate_salary(self):
        """Override method to calculate manager's salary with additional bonus."""
        base_salary = super().calculate_salary()
        bonus = 0.20 * base_salary  
        return base_salary + bonus

    def display_details(self):
        """Override method to display manager details."""
        super().display_details()
        print(f"Team Size: {self.team_size}")

class Developer(Employee):
    def __init__(self, employee_id, name, salary, department, programming_language):
        super().__init__(employee_id, name, salary, department)
        self.programming_language = programming_language

    def calculate_salary(self):
        """Override method to calculate developer's salary with a skill bonus."""
        base_salary = super().calculate_salary()
        skill_bonus = 0.15 * base_salary 
        return base_salary + skill_bonus

    def display_details(self):
        """Override method to display developer details."""
        super().display_details()
        print(f"Programming Language: {self.programming_language}")

def main():
   
    emp1 = Employee(101, "Ramesh Pawar", 5000, "HR")
    mgr1 = Manager(102, "Alice Khadka", 7000, "IT", 5)
    dev1 = Developer(103, "Bob Chaiwala ", 6000, "IT", "Python")

 
    print("Employee Details:")
    emp1.display_details()
    print(f"Monthly Salary: {emp1.calculate_salary()}\n")

    print("Manager Details:")
    mgr1.display_details()
    print(f"Monthly Salary: {mgr1.calculate_salary()}\n")

    print("Developer Details:")
    dev1.display_details()
    print(f"Monthly Salary: {dev1.calculate_salary()}\n")

 
    emp1.promote()
    mgr1.promote()
    dev1.promote()


if __name__ == "__main__":
    main()

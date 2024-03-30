'''
Define a employee class with attribute role,department & salary, This class also has a showDetails() method 
Create an engineer class that inherite properties from Employee and has additional attributes : name and age.
'''

class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDeails(self):
        print("The Role of the employee: ",self.role)
        print("The deparmenrt of the employee: ",self.department)
        print("The salary of the employee is: ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","50,000") 


Egr = Engineer("Utkarsh Harshe","22")  #Here we create the object of the Engineer
Egr.showDeails() #Here we call the showDetails method to display the detailss
        

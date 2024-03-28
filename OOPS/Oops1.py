# Create student class that takes name and marks of 3 subjects as argument in constructor.
# Then create a method to print average.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def cal_Avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your Avg marks is : ",sum/3)

s1 = Student("Utkarsh",[78,79,77])
s1.cal_Avg()

s1.name = "Gaurav"
s1.cal_Avg()


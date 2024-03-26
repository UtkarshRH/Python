""" WAP to enter the marks of three subjects from the user and store them in a dictionary. start with the empty dictionary and 
add one by one use subject name as key marks as value."""

marks = {}
x = int(input("enter phy : "))
marks.update({"Phy ": x})
x = int(input("enter math : "))
marks.update({"Math ": x})
x = int(input("enter Chem : "))
marks.update({"Chem ": x})
print(marks)
#WAP to find the greatest of two number entered by user
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))
if num1 > num2 :
    if num1 > num3:
        print("The Greatest number is : ",num1)
elif num2 > num3:
    print("The Greates number is : ",num2)
else:
    print("The Greatest number is : ",num3) 
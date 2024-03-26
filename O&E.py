#WAP to check if a number entered by user is odd or even

user  = int(input("Enter a number : "))
if user % 2 == 0:
    print("The number is even: ",user)
else:
    print("The Number is odd : ",user)

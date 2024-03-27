# Write a recursive function to calculate the sum of first n natural numbers

def first_Naturalnum(num):
    if(num == 0):
        return 0
    return first_Naturalnum(num - 1) + num

sum = first_Naturalnum(5)
print(sum)

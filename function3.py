#WAF to print the element of list in a single line (list is the parameter)
cities = ["Sakoli","Bhndara","Nagpur","Pune"]


def print_Ele(list):
    for item in list:
        print(item, end=" ")

# print_Ele(cities)


# WAF To find the factorial of n. (n is the parameter)

def fact_N(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    print(fact)

# fact_N(5)


#WAF to convert USD to INR

def convert_USD(USD):
    INR = USD * 83
    print(USD,"USD = ",INR,"INR") 

# convert_USD(2)
    

# WAF To print the number is even or odd
def fuc_Even_Odd(num):
    if num % 2 == 0:
        print("Even Number : ",num)
    else:
        print("Odd Number : ",num)

fuc_Even_Odd(2)
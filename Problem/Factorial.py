def compute_factorial(fact):
    num = 1
    if fact < 0:
        print("Sorry we con not find the fact of negative number")
    elif fact == 0:
        print("The factorial of the number zer is 1")
    for i in range(1, fact + 1):
        num *= i
    print(f"The factorial of the {fact} is {num}")



# compute_factorial(5)


# Now Here is the another method to solve this 
memo = {}
def compute_Fact(n):
    if n == 0:
        return 1 
    if n in memo:
        return memo[n]
    memo[n] = n * compute_Fact(n - 1)
    return memo[n]


print(compute_Fact(50))
print(memo)



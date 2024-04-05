def isPrime(nums):
    if nums <= 1:
        return False
    for i in range(2, int(nums ** 0.5) + 1):
        if nums % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if isPrime(int(num)):
    print(f"The Number: {num} is prime")
else:
    print(f"The Number: {num} is not a prime number")

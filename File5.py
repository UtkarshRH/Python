# From A file containing a number seperated by comma print the count of even number 
with open("File I/O/Practice.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(',')
    print(nums)
    count = 0
    for num in nums:
        if int(num) % 2 == 0 :
            count += 1
            print(num)
print("Their are ",count,"Even number in a file")


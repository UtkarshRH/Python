# Print the element of the following list using loop

ele = [1,4,9,16,25,36,49,64,81,100]

# for val in ele:
    # print(val)



# Search for a number x in this tuple using loop

tup = (1,4,9,16,25,36,49,64,81,100)
i = 0
x = 9

for t in tup :
    if t == x :
        print("Found",i)
        break
    i += 1
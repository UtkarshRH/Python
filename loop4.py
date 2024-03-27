# Search For a number x in this tuple using loop 
# (1,4,9,16,25,36,49,64,81,100)

tup = (1,4,9,16,25,36,49,64,81,100)
x = 1001

i = 0
while i <= len(tup)-1:
    if(tup[i]==x):
        print("Found")
    else:
        print("Not Found")
    i += 1
 
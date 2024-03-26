# WAP to check if a list contains a palindrom of elements (Hint: use copy() method) 

list = [1,2,1]
copyList = list.copy()
copyList.reverse()
if(list == copyList):
    print("The Give List is palimndrom")
else:
    print("The Give List is not palimndrom")

# Write a recursive function to print all element in a list 
# hint : List and idex as a parameter 
def print_List(list,idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print(list,idx+1)

fruit = ["banana","apple","orange","grapse"]
print_List(fruit,0)

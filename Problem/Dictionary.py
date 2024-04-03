my_Dict = {'a':1,'b':2} # Here we create the dictionary 
print("Here we create the dictionary        --> ",my_Dict)

my_Dict['c'] = 3 # Here we add the new key value pair
print("Added New Key value pair             --> ",my_Dict)

my_Dict['a'] = 5 #Here we change the value of the key 
print("Here we change the value of a        --> ",my_Dict)

del my_Dict['b'] #Here we remove the value of key 
print("Here we remove b from the dictionary --> ",my_Dict)

acc = my_Dict['a']

print("Modified Dictionary                  --> ",my_Dict)
print("The value of a :                     --> ",acc)




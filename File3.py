# Search If the word "lerning" exist in file or not 
word = "lerning"

with open('File I/O/Practice.txt','r') as f:
    data = f.read()
    if(data.find(word) != -1):
        print('Found')
    else:
        print('Not found')
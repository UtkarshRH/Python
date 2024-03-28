#WAF that replace all occurances of "Python" with "java"
with open('File I/O/Practice.txt','r') as f:
    data = f.read()

new_data = data.replace('Python','Java')
print(new_data)


with open('File I/O/Practice.txt','w')as f:
    f.write(new_data)
# WAF in which line of the file does the lerning occur first.
# Print -1 if word not found

def check_for_line():
    word = "lerasfning"
    data = True
    line_num = 1
    with open("File I/O/Practice.txt","r")as f:
        while data: 
            data = f.readline()
            if(word in data):
                print(line_num)
            line_num += 1
    return -1


print(check_for_line())
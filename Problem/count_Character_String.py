def count_Char(string):
    char_Count = {}
    for char in string:
        if char in char_Count:
            char_Count[char] += 1
        else:
            char_Count[char] = 1
    return char_Count


input_String = input("Enter a String : ")
print(count_Char(input_String))
my_char = input().upper()

valid_list = ["A","C","G","T","U"]

updated_str = ""

for i in my_char:

    if i not in valid_list:
        print("Invalid Input")
        exit()
    elif i == "G":
        updated_str += "C"
    elif i == "C":
        updated_str += "G"
    elif i == "T":
        updated_str += "A"
    elif i == "A":
        updated_str += "U"
    else:
        updated_str += i

print(updated_str)
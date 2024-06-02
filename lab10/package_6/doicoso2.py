def syntax_check(string):
    string_list = []
    for char in string:
        string_list.append(char)
        if char not in "0123456789ABCDEF":
            string_list.remove(char)
    return string_list

def base_number_check(base_number):
    for char in base_number:
        if char in 0 <= char <=9:
            print(base_number, "là hệ cơ số 10")
        elif char in 0 <= char <= 1:
            print(base_number, "là hệ cơ số 2")
        elif char in 0 <= char <=7:
            print(base_number, "là hệ cơ số 8")
        elif char in 0 <= char <= 9 and char in 'A' <= char <= 'F':
            print(base_number, "là hệ cơ số 16")
        else:
            print("Không hợp lệ")

def convert_binary_to_decimal(binary):
    binary = int(binary)
    decimal,i =0,0
    while binary >0:
        remainder = binary % 10
        exponential = remainder *(2**i)
        decimal = decimal + exponential
        binary = binary//10
        i += 1
    return binary

def convert_octal_to_decimal(octal):
    octal = int(octal)
    decimal,i =0,0
    while octal >0:
        remainder = octal % 10
        exponential = remainder *(8**i)
        decimal = decimal + exponential
        octal = octal //10
        i +=1
    return octal

def convert_hexadecimal_to_decimal(hexadecimal):
    convert_letters_to_numbers = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    position = len(hexadecimal) -1
    decimal = 0
    for i in hexadecimal:
        decimal += convert_letters_to_numbers[i] * pow(16,position)
        position -= 1
    return decimal
        


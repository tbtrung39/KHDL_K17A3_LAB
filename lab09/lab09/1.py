def find_max_number_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = find_max_number_recursive(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

def main():
    a = int(input('Nhập số thứ nhất: '))
    b = int(input('Nhập số thứ hai: '))
    c = int(input('Nhập số thứ ba: '))
    numbers = [a, b, c]
    print(f'Số lớn nhất trong 3 số được nhập là: {find_max_number_recursive(numbers)}')

main()

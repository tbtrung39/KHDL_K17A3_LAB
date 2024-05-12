def find_max_number(list):
    if len(list) ==1:
        return list[0]
    else:
        m = find_max_number(list[1:])
        return m if m > list[0] else list[0]
    
def main():
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    c = int(input("Nhập số thứ ba: "))
    list = [a,b,c]
    print("Số lớn nhất trong 3 số được nhập là: ", find_max_number(list))

main()
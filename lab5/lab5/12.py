a = input('Nhập chuỗi A: ')
b = input('Nhập chuỗi B: ')

found_solution = False

for i in range(1, len(a)):
    for j in range(1, len(b)):
        C, D, E, F = int(a[:i]), int(a[i:]), int(b[:j]), int(b[j:])
        if C + D == E + F:
            print(f'{C}+{D}={E}+{F}')
            found_solution = True
            break
    if found_solution:
        break

if not found_solution:
    print('Không tồn tại cách đặt!')
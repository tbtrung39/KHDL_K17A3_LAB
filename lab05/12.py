A = input("Nhập chuỗi ký tự A: ")
B = input("Nhập chuỗi ký tự B: ")

found_solution = False

for i in range(1, len(A)):
    for j in range(1, len(B)):
        C, D, E, F = int(A[:i]), int(A[i:]), int(B[:j]), int(B[j:])
        if C + D == E + F:
            print(f"{C}+{D}={E}+{F}")
            found_solution = True
            break
    if found_solution:
        break

if not found_solution:
    print("Không tồn tại cách đặt!")

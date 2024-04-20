def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Nhap mot so tu nhien n: "))

    A = {i for i in range(1, n+1) if n % i == 0 and la_so_nguyen_to(i)}
    B = {i for i in range(2, n) if la_so_nguyen_to(i) and n % i != 0}

    print("Tap hop A (cac so nguyen to la uoc cua n): ", A)
    print("Tap hop B (cac so nguyen to nho hon n va khong la uoc cua n): ", B)

if __name__ == "__main__":
    main()

def la_so_nguyen_to(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def tao_tap_hop(n):
    uoc_so_nguyen_to = [i for i in range(1, n + 1) if n % i == 0 and la_so_nguyen_to(i)]
    nguyen_to_nho_hon_n = [i for i in range(2, n) if la_so_nguyen_to(i) and n % i != 0]

    tap_hop_A = set(uoc_so_nguyen_to)
    tap_hop_B = set(nguyen_to_nho_hon_n)

    return tap_hop_A, tap_hop_B

def main():
    n = int(input("Nhập số nguyên dương n: "))
    tap_hop_A, tap_hop_B = tao_tap_hop(n)

    print("Tập hợp A:", tap_hop_A)
    print("Tập hợp B:", tap_hop_B)

if __name__ == "__main__":
    main()

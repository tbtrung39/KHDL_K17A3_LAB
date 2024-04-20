def tim_cap_chi_so(a):
    n = len(a)
    cap_chi_so = []
    for i in range(n):
        for j in range(i+1, n):
            if a[j] + 1 == a[i]:
                cap_chi_so.append((i, j))
    return cap_chi_so

if __name__ == '__main__':
    a = list(map(int, input("Nhập dãy số (các số cách nhau bởi dấu cách): ").split()))
    print(tim_cap_chi_so(a))

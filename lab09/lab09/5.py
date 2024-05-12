def hoan_vi(s):
    if len(s) == 1:
        return [s]
    
    result = []
    for i, c in enumerate(s):
        for perm in hoan_vi(s[:i] + s[i+1:]):
            result.append(c + perm)
    return result

def main():
    n = input('Nhập chuỗi: ')
    print(hoan_vi(n))

main()

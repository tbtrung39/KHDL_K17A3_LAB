def permutation(lst, start, end):
    if start == end:
        print(lst)
    else:
        for i in range(start, end + 1):
            lst[start], lst[i] = lst[i], lst[start]
            permutation(lst, start + 1, end)
            lst[start], lst[i] = lst[i], lst[start]

def main():
    n = int(input('Nhập số phần tử tự nhiên: '))
    elements = list(range(1, n + 1))
    permutation(elements, 0, n - 1)

main()

a = set()
end = 'ESC'
while True:
    n = input("Hãy nhập vào bàn phím: ")
    if n == end:
        break
    a.add(n)
print(a)
a = {n for n in a if not n.isdigit()}
print(a, "là set cuối cùng đã loại bỏ số")


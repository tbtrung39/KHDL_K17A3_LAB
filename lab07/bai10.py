m = set(str(input("nhập gtrị m: ")))
n = set(str(input("nhập gtrị n: ")))
result = 0
q = m & n
for i in q:
    if i.isdigit():
        result += int(i)
print("Tổng các chữ số chung: ", result)
n = int(input('Nhập vào số phần tử của dãy fibonacci:  '))
fibonacci = [0, 1]
[fibonacci.append(fibonacci[0] + fibonacci[1]) for i in range(n-2)]
print(','.join(map(str, fibonacci)))
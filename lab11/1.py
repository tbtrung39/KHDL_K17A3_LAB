with open('lab11/dayso.dat','r') as file:
    data = list(map(int,file.read().split()))
    tong = sum([i for i in data if i%2!=0])
    print('tổng các số lẻ trong dãy là:',tong)
Str = input('nhập chuỗi ký tự: ')
S1=''

for i in Str:
    if i.isnumeric():
        S1+=i

S2= int(S1)
tong=0

for i in range(1,S2):
    if S2 % i == 0:
        tong+=1

if tong == S2:
    print(S2, 'đây là số hoàn hảo')
else:
    print(S2, 'đây kp là số hoàn hảo')
    
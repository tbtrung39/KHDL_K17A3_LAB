a = [2,-4,1,9,-3,6,3,-2,6,8]
#
sum = 0
for i in a:
    sum +=1
print(f'Tổng các chữ số trong list là: {sum}')
#
a_duong = list(filter(lambda x:x>0, a))
print(f'Các phần tử dương trong list là: {a_duong}')
sum = 0
for i in a_duong:
    sum +=1
print(f'Tổng các phần tử dương trong list là: {sum}')
#
a_am = list(filter(lambda x:x<0, a))
print(f'Phần tử âm đầu tiên trong danh sách là: {a_am[0]}')
#
a_duong = list(filter(lambda x:x>0, a))
print(f'Phần tử dương cuối cùng trong danh sách là: {a_duong[-1]}')
#
vtln= len(a)-a[::-1].index(max(a))
print(f'phần tử lớn nhất của danh sách {a[vtln-1]} và vị trí lớn nhất cuối cùng là {vtln-1}')
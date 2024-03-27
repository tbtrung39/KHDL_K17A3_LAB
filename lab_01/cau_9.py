# viết chương trình xác suất khi tung n lần 3 xúc sắc có ít nhất,
# có 1 lần ra cả 3 và 6 (làm tròn đến số thập phân thứ 2)
n=float(input('Nhap so lan tung: '))
xac_xuat=(1-(5/6)**n)**3
print(f'Xac xuat la {xac_xuat:.2f}')
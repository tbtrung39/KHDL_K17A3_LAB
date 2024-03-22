a = float(input("nhập giá trị a :"))
b = float(input("nhập giá trị b :"))
c = float(input("nhập giá trị c :"))
d = float(input("nhập giá trị d :"))
r = float(input("nhập giá trị r :"))
do_dai_IM = ((c - a)**2 + (d - b)**2)**0.5
if do_dai_IM > r :
    print("điểm M nằm ngoài đường tròn.")
elif do_dai_IM == r :
    print("điểm M nằm trên đường tròn.")
else:
    print("điểm M nằm trong đường tròn.")        
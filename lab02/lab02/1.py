t=int(input("Nhập vào số tháng cần biết bao nhiêu ngày:"))
if t==2:
    a=input("Năm đó có nhuận hay không:      (y/n) ")
    if a=='y':
        print(f"Tháng {t} có 29 ngày")
    elif a=='n':
        print(f"Tháng {t} có 28 ngày") 
elif t == 1 or t == 3 or t == 5 or t == 7 or t == 8 or t == 10 or t == 12 :
    print(f"Tháng {t} có  31 ngày")
elif t == 4 or t == 6 or t == 9 or t == 11 :
    print(f"Tháng {t} có 30 ngày")
else:
    print("Nhập tháng sai rồi cu")
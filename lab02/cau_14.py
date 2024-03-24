# lý
I=float(input('nhập mức cường độ âm:'))
D=float(input('nhập khoảng cách:'))
if 20*pow(((pow(10,I/10)*pow(10,-12))/pow(10,-12)),0.5)>100:
    print("Người này có nghe thấy âm thanh.")
else:
    print("Người này không nghe thấy âm thanh.")
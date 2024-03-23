t=float(input("Nhập số điện tiêu thụ cần đổi sang tiền:"))
if 0<= t <=100:
    t0=t*2000
    print(f"{t} có số điện tiêu thụ là {t0} VND")
elif 101<= t and t <= 200:
    t1=(t-100)*2500 + 100*(2000+2500)
    print(f"{t} có số điện tiêu thụ là {t1} VND")
elif 201<= t and t <= 300:
    t2=(t-300)*3000 + 100*(2000+2500+3000)
    print(f"{t} có số điện tiêu thụ là {t2} VND")
elif t >= 300:
    t3=(t-600)*3000 + 100*(2000+2500+3000+5000)
    print(f"{t} có số điện tiêu thụ là {t3 } VND")
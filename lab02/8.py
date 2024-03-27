TNCT = int(input('nhập thâm niên công tác : '))
luongcanban = 1350000
if TNCT <12:
    luong = 2.34*luongcanban
elif TNCT>= 12 and TNCT <36:
    luong = 3.33*luongcanban
elif TNCT>=36 and TNCT<60:
    luong = 3.66*luongcanban
elif TNCT >60:
    luong = 3.99 *luongcanban
print(f'luong theo tham nien la {luong}')
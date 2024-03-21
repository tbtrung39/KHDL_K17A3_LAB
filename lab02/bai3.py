thu=int(input("nhap thu :"))
if thu <1 or thu>7:
    thu=(int(input("nhap thu :")))
if thu == 1:
    print("sunday")
elif thu == 2:
    print("Monday")
elif thu == 3:
    print("tuesday")
elif thu == 4:
    print("wednesday")
elif thu == 5:
    print("thursday")
elif thu == 6:
    print("friday")
else:
    print("saturday")
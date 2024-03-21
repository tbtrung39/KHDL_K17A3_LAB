a = int(input("Nhap vao mot so nguyen bat ki co 3 chu so: "))
a1 = a//100
a2 = (a//10)%10
a3 = a%10
if a1 == 1:
    a1 = "Mot Tram"
elif a1 == 2:
    a1 = "Hai Tram"
elif a1 == 3:
    a1 = "Ba Tram"
elif a1 == 4:
    a1 = "Bon Tram"
elif a1 == 5:
    a1 = "Nam Tram"
elif a1 == 6:
    a1 = "Sau Tram"
elif a1 == 7:
    a1 = "Bay Tram"
elif a1 == 8:
    a1 = "Tam Tram"
elif a1 == 9:
    a1 = "Chin Tram"
if a2 == 1:
    a2 = "Muoi"
elif a2 == 2:
    a2 = "Hai Muoi"
elif a2 == 3:
    a2 = "Ba Muoi"
elif a2 == 4:
    a2 = "Bon Muoi"
elif a2 == 5:
    a2 = "Nam Muoi"
elif a2 == 6:
    a2 = "Sau Muoi"
elif a2 == 7:
    a2 = "Bay Muoi"
elif a2 == 8:
    a2 = "Tam Muoi"
elif a2 == 9:
    a2 = "Chin Muoi"
elif a2 == 0 and a3!=0:
    a2 = "Linh"
if a3 ==1:
    a3 ="Mot"
if a3 ==2:
    a3 ="Hai"
if a3 ==3:
    a3 ="Ba"
if a3 ==4:
    a3 ="Bon"
if a3 ==5:
    a3 ="Nam"
if a3 ==6:
    a3 ="Sau"
if a3 ==7:
    a3 ="Bay"
if a3 ==8:
    a3 ="Tam"
if a3 ==9:
    a3 ="Chin"
if a3 ==0:
    a3 =""
print("Cach doc la:", a1,a2,a3)
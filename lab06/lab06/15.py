num_tuples = int(input("Nhap so luong tuples : "))
tuples= []
for i in range (num_tuples):
    name = input(f"Nhap ten nguoi thu{i+1}: ")
    age = int(input(f"Nhap tuoi cua {name}: "))
    score= int(input(f"Nhap diem  của {name}: "))
    tuples.append((name, age, score))
tuples.sort(key =lambda x: (x[0],x[1],x[2]))
print("danh sach tuple sau khi sap xep la :")
for t in tuples:
    print(t)
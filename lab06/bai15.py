num_tuples = int(input("Nhập số lượng tuples : "))
tuples= []
for i in range (num_tuples):
    name = input(f"Nhập tên người thứ {i+1}: ")
    age = int(input(f"Nhập tuổi của {name}: "))
    score= (input(f"Nhập điểm của {name}: "))
    isFloat = False
    try:
        float(number)
        isFloat = True
    except ValueError:
        isFloat = False
        
    while isFloat == False:
        number = (input("Đây không phải số thập phân, vui lòng nhập lại: "))
        try:
            float(number)
            isFloat = True
        except ValueError:
            isFloat = False
    tuples.append((name, age, score))
#sap xep tang dan
tuples.sort(key =lambda x: (x[0],x[1],x[2]))
print("Danh sách tuples sau khi sắp xếp là:")
for t in tuples:
    print(t)
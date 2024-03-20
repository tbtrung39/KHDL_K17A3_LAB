a = float(input("nhập giá trị vào a :"))
b = float(input("nhập giá trị vào b :"))
c = float(input("nhập giá trị vào c :"))
delta = b**2 - 4 * a * c
if a == 0 :
    x0 = -c / b
    print("đây là phương trình bậc 1 là :", x0)
elif a != 0 :
    if delta > 0:
        x1 = (-b + delta ** 0.5) / 2 * a
        x2 = (-b - delta ** 0.5) / 2 * a 
        print("phương trình có 2 nghiệm phân biệt :" , x1, x2) 
    elif delta == 0 :
        x = -b / 2 * a
        print("phương trình có nghiệm kép x :", x)
    else:
        print("phương trình vô nghiệm.") 
           
        
    
    
    
    
 
    
my_set = set()
while True:
    char = input("Nhap vao ky tu(Esc de ket thuc): ")
    if char == "x1b":
        break
    my_set.add(char)
my_set.difference_update({'0','1','2','3','4','5','6','7','8','9'})    
print(f"Tap hop sau khi xoa ca ky tu so la: {my_set}")        



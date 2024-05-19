a = int(input("Nhập độ dài cạnh của hình vuông:"))
import hinhhoc.my_square as my_square
print('Chu vi của hình vuông =:', end = " ")
print(my_square.ChuviHinhVuong(a))

print('Diện tích của hình vuông =:', end = " ")
print(my_square.Dien_tich_hinh_vuong(a))
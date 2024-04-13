so_luong = int(input("Nhập số lượng số trong danh sách: "))
danh_sach = []
for i in range(so_luong):
    so = int(input(f"Nhập số thứ {i+1}: "))
    danh_sach.append(so)
for so in danh_sach:
    assert so % 2 == 0, f"{so} không phải là số chẵn!"
print("Tất cả các số trong danh sách đều là số chẵn!")

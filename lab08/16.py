def create_even_numbers_list():
    # Tạo danh sách chứa toàn số chẵn từ 1 đến 100
    even_numbers = [x for x in range(1, 101) if x % 2 == 0]
    return even_numbers

# Gọi hàm và in danh sách số chẵn
even_numbers_list = create_even_numbers_list()
print("Danh sách số chẵn từ 1 đến 100:")
print(even_numbers_list)

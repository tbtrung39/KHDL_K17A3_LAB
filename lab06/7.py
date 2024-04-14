# Tạo danh sách List và in các phần tử của List ra màn hình
List = [['mon', 73], ['tue', 89], ['wed', 95], ['thu', 103], ['fri', 115], ['sat', 128], ['sun', 120]]
print("Danh sách List:", List)

# Sử dụng list comprehension để chọn ra phần tử thứ hai thuộc vị trí thứ 3 của sublist
selected_item = [sublist[1] for sublist in List if List.index(sublist) == 2]
print("Phần tử thứ hai thuộc vị trí thứ 3 của sublist:", selected_item)

# Kiểm tra độ dài của list List và thêm một sublist ngẫu nhiên
print("Độ dài của List ban đầu:", len(List))
random_sublist = ['random', 99]
List.append(random_sublist)
print("List sau khi thêm một sublist ngẫu nhiên:", List)

# Tính tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật
days = ['tue', 'wed', 'sat', 'sun']
total_sale_value = sum([sublist[1] for sublist in List if sublist[0] in days])
print("Tổng sale value trong các ngày tue, wed, sat và sun:", total_sale_value)
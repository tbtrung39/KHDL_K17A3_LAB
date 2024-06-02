# Mở các tệp văn bản
with open("m_nums.txt", "r") as f1:
    nums1 = [int(line) for line in f1]
with open("n_nums.txt", "r") as f2:
    nums2 = [int(line) for line in f2]

# Tìm các số chung
so_chung = [num for num in nums1 if num in nums2]

# Lưu kết quả vào tệp
with open("so_chung.txt", "w") as f:
    f.write(", ".join(map(str, so_chung)))

# In kết quả ra màn hình
print(", ".join(map(str, so_chung)))
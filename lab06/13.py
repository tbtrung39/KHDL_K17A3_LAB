a = ["Anh", "Em"]
b = ["Chơi", "Yêu"]
c = ["Bóng đá", "Bóng rổ"]

# Tạo ra tất cả các câu có chủ ngữ, động từ và tân ngữ từ các danh sách trên
d = [f"{subject} {verb} {object}" for subject in a for verb in b for object in c]

# In ra tất cả các câu được tạo
for sentence in d:
    print(sentence)

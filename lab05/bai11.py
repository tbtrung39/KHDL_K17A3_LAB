#11. Cho chuỗi ký tự Str1. Ta gọi một từ trong chuỗi là một dãy ký tự liên tiếp (không có ký tự trắng và dấu phẩy) các từ này được phân cách bởi các ký tự trắng hoặc dấu phẩy.Hãy viết chương trình in ra các từ trong chuỗi Str1, mỗi từ in trên một dòng. 
Str1 = "Khoa, khoa hoc ung dung"
words = Str1.split(" ")
if len(words) == 1:
    words = Str1.split(",") 
for word in words:
    print(word)

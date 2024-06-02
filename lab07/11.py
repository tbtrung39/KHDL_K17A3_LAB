n=int(input("Nhập số lượng sinh viên: "))
a=int(input("Số lượng sinh viên dự thi ngôn ngữ C++: "))
b=int(input("Số lượng sinh viên dự thi ngôn ngữ Java: "))
c=int(input("Số lượng sinh viên dự thi ngôn ngữ Python: "))
C=set(range(1,a+1))
J=set(range(a+1,a+b+1))
P=set(range(a+b+1,a+b+c+1))
C1=C-J-P
J1=J-C-P
P1=P-C-J
CJ=C&J
CP=C&P
JP=J&P
CJP=C&J&P
print("Sinh viên chỉ tham gia một ngôn ngữ:")
print("C++:", C1)
print("Java:", J1)
print("Python:", P1)
print("Sinh viên code trên 2 ngôn ngữ:")
print("C++ và Java:", CJ)
print("C++ và Python:", CP)
print("Java và Python:", JP)
print("Sinh viên dự thi cả 3 ngôn ngữ:")
print("C++, Java, Python:", CJP)
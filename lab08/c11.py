def average_score():
    name = input("Nhập tên sinh viên: ")
    math = float(input("Điểm toán của SV là: "))
    physics = float(input("Điểm lý của sv là: "))
    chemistry = float(input("Điểm hóa của sv là: "))
    average = (math+physics+chemistry)/3
    student = {"Tên SV :":name, "Điểm toán: ":math, "Điểm lý: ":physics, "Điểm hóa: ":chemistry,"Điểm trung bình: ":average}
    print(student)
average_score()

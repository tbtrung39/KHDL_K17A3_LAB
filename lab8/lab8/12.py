def employee():
    name = input("Nhập tên nhân viên: ")
    place_of_origin = input("Quê của nhân viên: ")
    experience = int(input("Thâm niên công tác của nhân viên(năm): "))
    return name, place_of_origin, experience
def employee_salary(experience):
    basic_salary = 10000000
    increase_per_year = 3000000
    salary = basic_salary + increase_per_year * experience
    return salary
def  employee_output(name,place_of_origin,experience,salary):
    print("Thông tin của nhân viên là: ")
    print("Tên nhân viên : ", name)
    print("Quê quán của nhân viên ở: ", place_of_origin)
    print("Thâm niên công tác của nhân viên : ", experience, "năm")
    print("Lương nhân viên là: ", salary)
name , place_of_origin , experience = employee()
salary = employee_salary(experience)
output = employee_output(name,place_of_origin,experience,salary)
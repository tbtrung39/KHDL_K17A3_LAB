weekdays = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

day = int(input("nhap so tu 1 den 7: "))

if day in weekdays:
    print("ngay ban chon la:", weekdays[day])
else:
    print("Invalid input. nhap so tu 1 den 7.")
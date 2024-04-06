a = int(input("Nhập vào thứ (1 -> 7) trong tuần: "))

if a == 1:
    print(f"{a} là Sunday trong tuần")
elif a == 2: 
    print(f"{a} là Monday trong tuần")
elif a == 3: 
    print(f"{a} là Tuesday trong tuần")
elif a == 4: 
    print(f"{a} là Wednesday trong tuần")
elif a == 5: 
    print(f"{a} là Thursday trong tuần")
elif a == 6: 
    print(f"{a} là Friday trong tuần")
elif a == 7: 
    print(f"{a} là Saturday trong tuần")
else:
    print("Số bạn nhập không phải là một ngày trong tuần.")
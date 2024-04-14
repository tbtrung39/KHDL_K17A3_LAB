def kiem_tra_so_chan(List_so):
    for so in List_so:
        assert so % 2 ==0, f"So {so} khong phai la so chan!"
List_so = [int(x) for x in input("Nhap vao cac so cach nhau bang dau cach: ").split()]
kiem_tra_so_chan(List_so)
print("tat cac cac so trong list deu la so chan")
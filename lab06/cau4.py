#1
list = [[0],[1],[2],[3],[4],[5],[6]]
list[0] = [1,2,3]
print(list)
#2
list = [[0],[1],[2],[3],[4],[5],[6]]
list[6] = [1,2,3]
print(list)
#3
list = [[0],[1],[2],[3],[4],[5],[6]]
list[4] = [1,2,3]
print(list)
#xoa phan tu k
List = [0, 1, 2, 3, 4, 5, 6]
k= int(input("Nhap vao gia tri k can xoa : "))
if k in List:
    List.remove(k)
    print("danh sach sau khi xoa ", k , "la: ")
    print(List)
else:
    print("phan tu", k ,"khong ton tai trong danh sach")
#tang dan
List = [0, 1, 2, 3, 4, 5, 6]
sorted_List = sorted(List)
print(sorted_List)
#giam dan
List = [0, 1, 2, 3, 4, 5, 6]
sorted_List_desc = sorted(List, reverse=True)
print(sorted_List_desc)
with open(r"lab11\package_7\M_nums.txt", mode = "r") as m, open(r"lab11\package_7\N_nums.txt") as n:
    so_m = set(map(int, m.read().split()))
    so_n = set(map(int, n.read().split()))
    
so_chung = so_m.intersection(so_n)

with open("lab11\package_7\so_chung.txt", mode = "w") as f:
    f.write('\n'.join(map(str, so_chung)))
    
with open("lab11\package_7\so_chung.txt", mode = "r") as f:
    print("Các số chung trong cả 2 file là:") 
    print(f.read())      
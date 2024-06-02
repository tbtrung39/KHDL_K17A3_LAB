
from package.phuong_trinh import giai_pt_bac_nhat, giai_pt_bac_hai
print("Giải phương trình bậc nhất:")
a, b = 2, 3
print(f"{a}x + {b} = 0: x = {giai_pt_bac_nhat(a, b)}")

a, b = 0, 0
print(f"{a}x + {b} = 0: {giai_pt_bac_nhat(a, b)}")

a, b = 0, 5
print(f"{a}x + {b} = 0: {giai_pt_bac_nhat(a, b)}")

print("\nGiải phương trình bậc hai:")
a, b, c = 1, 3, 2
print(f"{a}x^2 + {b}x + {c} = 0: x = {giai_pt_bac_hai(a, b, c)}")

a, b, c = 1, 2, 1
print(f"{a}x^2 + {b}x + {c} = 0: x = {giai_pt_bac_hai(a, b, c)}")


x = 0.5  
n = 10    
cos = 1
i = 1

while abs(cos) > 1e-4:
  cos *= -x**i / (i * (i - 1))
  i += 2

cos_gan_dung = 1 + cos
print(f"cos({x}) ≈ {cos_gan_dung}")

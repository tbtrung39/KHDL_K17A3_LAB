import math

x=0.5
cos_approx=1
n=1
term=x**2/2
while abs(term)>1e-4:
    cos_approx-=term
    n+=2
    term*=-1*x**2/(n*(n-1))
true_value=math.cos(x)
error=abs(cos_approx-true_value)
print(f"Gia tri gan dung cua cos({x}) la: {cos_approx}")
print(f"Gia tri chinh xac cua cos({x}) la: {true_value}")
print(f"Sai so: {error}")
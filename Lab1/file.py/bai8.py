import math
x=float(input("Nhập vào x: "))
z=float(input("Nhập vào z: "))
f = (((x**2)*math.sin(z)+(abs(x))**0.5)/((math.log(z))+math.exp(x-1)))/ math.atan(x*z)
print(f)
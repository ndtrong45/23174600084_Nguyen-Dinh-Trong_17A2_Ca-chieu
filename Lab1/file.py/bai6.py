x1,y1= map(int, input("Nhập tọa độ vecto a:").split())
x2,y2= map(int, input("Nhập tọa độ vecto b:").split())
# Tính toán tổng 2 vecto
x=x1+x2 
y=y1+y2
# Tính toán hiệu 2 vecto
a=x1-x2
b=y1-y2

d=((x1**2)+(x2**2))**0.5 # Tính toán độ dài vecto a
e=((y1**2)+(y2**2))**0.5 # Tính toán độ dài vecto b
t=x1*y1+x2*y2 # Tính toán tích vô hướng của vecto a và b
cos=t/(d*e) # Tính toán cos(a,b)
print("Vecto a + b:",x,",",y)
print("Vecto a - b:",a,",",b)
print("Độ dài vecto a:",d)
print("Độ dài vecto b:",e) 
print("Cosin góc hợp giữa hai vecto a và b:",round(cos,2))
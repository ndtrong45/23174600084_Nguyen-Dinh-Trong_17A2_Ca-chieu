a1 = float(input("Nhập hệ số a1: "))
b1 = float(input("Nhập hệ số b1: "))
c1 = float(input("Nhập hệ số c1: "))
a2 = float(input("Nhập hệ số a2: "))
b2 = float(input("Nhập hệ số b2: "))
c2 = float(input("Nhập hệ số c2: "))
x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1) # Tính x
y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1) # Tính y
print("Nghiệm của hệ phương trình là: ",round(x,2),",",round(y,2))

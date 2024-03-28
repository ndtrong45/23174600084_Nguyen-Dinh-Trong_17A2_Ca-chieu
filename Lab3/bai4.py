# Hình 1
n=int(input("Nhập vào chiều cao: "))
for i in range(1, n + 1):
        print(" " * (n - i) + "* "*i)
for i in range(n, 1,-1):
        print(" " * (n - i) + "* "*i)
# Hình 2
a=int(input("Nhập vào chiều cao tán lá cây thông: "))
b=int(input("Nhập vào chiều cao thân cây thông: "))
for i in range(1, a + 1):
        print(" " * (a - i) + "*"*(2*i-1))
for i in range(1,b+1):
        print(" " * (a-2) + "*"*3)
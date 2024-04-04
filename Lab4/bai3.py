n = int(input("Nhập số từ bàn phím: "))
count = 0
a = n 

while True:
    phan_du = a % 10
    count += 1 
    a = a // 10
    if a == 0:
        break
print("Số chữ số của số nguyên là:",count)
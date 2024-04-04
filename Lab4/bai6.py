n = int(input("Nhập số từ bàn phím: "))
count = 0
a = n 

while True:
    phan_du = a % 10
    count += 1 
    a = a // 10
    if a == 0:
        break
print("Cách đọc: ")
for i in range(count, 0, -1):
    chu_so_thu_i = n // 10**(i-1)
    if chu_so_thu_i == 1:
        print("one", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 2:
        print("two", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 3:
        print("three", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 4:
        print("four", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 5:
        print("five", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 6:
        print("six", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 7:
        print("seven", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 8:
        print("eight", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 9:
        print("nine", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 0:
        print("zero", end = " ")
        n = n % 10**(i-1)

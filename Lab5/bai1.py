n=int(input("Nhập vào số nguyên dương: "))
nhi_phan=""

if n < 0:
    print("Vui lòng nhập số dương")
else:
    while n > 0:
        phan_du = n % 2
        nhi_phan = str(phan_du) + nhi_phan
        n = n // 2
        
print("Số nhị phân tương ứng là:",nhi_phan)
nguyen_dinh_trong = {}
n = int(input("Nhập vào n: "))
for x in range(1, n+1):
    nguyen_dinh_trong[x] = x ** 3
print("Từ điển có key là x và value là x^3 có độ dài bằng",n,"là: \n",nguyen_dinh_trong)
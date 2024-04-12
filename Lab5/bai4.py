van_ban = input("Nhập vào chuỗi văn bản: ")
a=""

for i in van_ban:
    if i.isdigit():
        a+=i
print("Chuỗi sau khi loại bỏ các kí tự không phải là số là:",a)

a=float(a)
ktra=True

for i in range(2,(int(a**0.5)+1)):
    if a%i == 0:
        ktra=False
        break

if ktra:
    print("Chuỗi đó là số nguyên tố")
else:
    print("Chuỗi đó không phải là số nguyên tố")   
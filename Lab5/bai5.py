str1 = input("Nhập vào chuỗi 1: ")
str2 = input("Nhập vào chuỗi 2: ")
tron_chuoi = ""
min = 0

if len(str1) < len(str2):
    min = len(str1)
else:
    min = len(str2)

for i in range(min):
    tron_chuoi += str1[i] + "-" + str2[i] + "-"

print("Chuỗi sau khi trộn là: ", tron_chuoi.strip("-"))
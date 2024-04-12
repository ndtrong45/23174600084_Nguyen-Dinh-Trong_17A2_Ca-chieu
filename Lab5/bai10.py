chuoi = input("Nhập vào chuỗi: ")
a = ''

for i in chuoi:
    if i != ' ':
        a += i

print("Chuỗi sau khi xóa khoảng trắng:",a)
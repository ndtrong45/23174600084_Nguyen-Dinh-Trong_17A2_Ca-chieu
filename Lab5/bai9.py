str1 = input("Nhập vào chuỗi 1:")
str2 = input("Nhập vào chuỗi 2:")

if len(str1) == len(str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1            
    if count <= 1:
        print("Có thể thay đổi chuỗi 1 thành chuỗi 2")
    else:
        print("Không thể thay đổi chuỗi 1 thành chuỗi 2")
else:
    print("Không thể thay đổi chuỗi 1 thành chuỗi 2")
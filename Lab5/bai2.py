str1 = input("Nhập vào chuỗi ký tự thứ nhất: ")
str2 = input("Nhập vào chuỗi ký tự thứ hai: ")
len_str1 = len(str1)
len_str2 = len(str2)
min = 0
chuoi_con = ""

if len_str1 > len_str2:
    min = len_str2
else:
    min = len_str1
    
for i in range(min, 0, -1):
    for j in range(len_str1 - i + 1):
        a = str1[j:(j + i)]
        if a in str2:
            chuoi_con = a
    if chuoi_con:
        break

if chuoi_con:
    print("Chuỗi ký tự con chung có độ dài ngắn nhất là:",chuoi_con)
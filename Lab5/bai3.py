van_ban = input("Nhập vào chuỗi văn bản: ")
tu_can_tim = input("Nhập vào từ cần tìm kiếm: ")

if tu_can_tim in van_ban:
    print("Vị trí của ",tu_can_tim,"trong văn bản là:",van_ban.find(tu_can_tim))
else:
    print("Từ cần tìm kiếm không có trong văn bản")

max_count=0

for i in van_ban:
    count = 0
    for j in van_ban:
        if i == j:
            count+=1
    if count > max_count:
        max_count=count
        a=i
print("Từ xuất hiện nhiều nhất trong chuỗi là:",a)
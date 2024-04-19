n = int(input("Nhập số phần tử của dãy số(lớn hơn 2 phần tử): "))
day_so = []

for i in range(n):
    print("Nhập phần tử thứ",i+1,end=":")
    x = float(input())
    day_so.append(x)
   
cong_sai = day_so[1] - day_so[0]
for i in range(2, len(day_so)):
    if day_so[i] - day_so[i - 1] == cong_sai:
        print("Dãy số tạo thành cấp số cộng")  
    else:
        print("Dãy số không tạo thành cấp số cộng")
        
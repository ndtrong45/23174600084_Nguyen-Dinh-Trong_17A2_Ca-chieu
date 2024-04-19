n = int(input("Nhập số phần tử của mảng: "))
mang = []

for i in range(n):
    print("Nhập phần tử thứ",i+1,end=":")
    x = int(input())
    mang.append(x)

tong_chan = 0
tong_le = 0
for i in mang:
    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i

print("Tổng các số chẵn trong mảng là:",tong_chan)
print("Tổng các số lẻ trong mảng là:",tong_le)


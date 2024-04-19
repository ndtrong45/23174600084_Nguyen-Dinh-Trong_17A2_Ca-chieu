n = int(input("Nhập số phần tử của mảng: "))
mang = []

for i in range(n):
    print("Nhập phần tử thứ",i+1,end=":")
    x = float(input())
    mang.append(x)

print("Số lớn nhất trong mảng là:",max(mang))
print("Số bé nhất trong mảng là:",min(mang))

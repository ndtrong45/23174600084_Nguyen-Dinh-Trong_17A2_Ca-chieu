n = int(input("Nhập số phần tử của mảng: "))
mang = []

for i in range(n):
    print("Nhập phần tử thứ",i+1,end=":")
    x = int(input())
    if x > 0 :
        mang.append(x)
    else:
        print("Vui lòng nhập số nguyên dương")
        break

print("Các số nguyên tố có trong mảng là:",end=" ")
for x in mang:
    a=True
    if x < 2 :
        a=False
    else:
        for i in range(2,int(x**0.5+1)):
            if x % i == 0:
                a=False
                break
    if a:
        print(x,end=" ")   
print("\n")
print("Các số hoàn hảo trong mảng là:",end=" ")
for x in mang:
    tong_uoc_so = 0
    for i in range(1, x):
        if x % i == 0:
            tong_uoc_so += i
    if x == tong_uoc_so:
        print(x,end=" ") 
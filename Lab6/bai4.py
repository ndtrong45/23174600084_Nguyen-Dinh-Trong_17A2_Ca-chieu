#Danh sách fibonacci
n = int(input("Nhập số lượng số Fibonacci bạn muốn tạo: "))

fibonacci = [0,1]
[fibonacci.append(fibonacci[i-1]+fibonacci[i-2]) for i in range(2, n)]

print("Danh sách Fibonacci chứa", n, "số đầu tiên là:", fibonacci)
#Danh sách các số nguyên tố nhỏ hơn 100
so_nt = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
print("Các số nguyên tố nhỏ hơn 100 là:",so_nt)

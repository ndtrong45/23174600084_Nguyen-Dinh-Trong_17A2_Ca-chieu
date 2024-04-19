m = int(input("Nhập số hàng của ma trận:"))
n = int(input("Nhập số cột của ma trận:"))

print("Nhập các phần tử của ma trận:")
matrix = []
for i in range(m):
    row1 = []
    for j in range(n):
        element = int(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))
        row1.append(element)
    matrix.append(row1)

# Tính tổng của ma trận
total_sum = 0
for row in matrix:
    total_sum += sum(row)
print("Tổng của các phần tử trong ma trận là:", total_sum)

print("\nNhập ma trận thứ hai có kích thước", n, "x", m)
matrix2 = []
for i in range(n):
    row2 = []
    for j in range(m):
        element = int(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))
        row2.append(element)
    matrix2.append(row2)

# Tính tích của hai ma trận
product_matrix = []
if len(matrix[0]) == len(matrix2):
    transposed_matrix2 = [[matrix2[j][i] for j in range(len(matrix2))] for i in range(len(matrix2[0]))]
    for row1 in matrix:
        row_result = []
        for row2 in transposed_matrix2:
            dot_product = sum([x * y for x, y in zip(row1, row2)])
            row_result.append(dot_product)
        product_matrix.append(row_result)

    print("\nTích của hai ma trận là:")
    for row in product_matrix:
        print(row)
else:
    print("Hai ma trận không thể nhân với nhau.")

# Tính và in ra ma trận chuyển vị của ma trận ban đầu
print("\nMa trận chuyển vị của ma trận ban đầu là:")
transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for row in transposed_matrix:
    print(row)


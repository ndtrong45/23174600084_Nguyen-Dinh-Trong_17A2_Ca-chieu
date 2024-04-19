size = int(input("Nhập kích thước của ma trận vuông: "))

print("Nhập các phần tử của ma trận vuông:")
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        element = float(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))
        row.append(element)
    matrix.append(row)

# Tìm ma trận nghịch đảo (nếu có)
det = 0
if size == 2:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
elif size == 3:
    det = matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) - \
          matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) + \
          matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])

if det == 0:
    print("Ma trận không có ma trận nghịch đảo.")
else:
    inverse = []
    for i in range(size):
        row_inverse = []
        for j in range(size):
            sub_matrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            cofactor = ((-1) ** (i + j)) * (sub_matrix[0][0] * sub_matrix[1][1] - sub_matrix[0][1] * sub_matrix[1][0])
            row_inverse.append(cofactor / det)
        inverse.append(row_inverse)

    print("\nMa trận nghịch đảo của ma trận đã nhập là:")
    for row in inverse:
        print(row)

# Kiểm tra xem ma trận đã nhập có phải là ma trận đối xứng hay không
is_symmetric = True
for i in range(size):
    for j in range(i + 1, size):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break

if is_symmetric:
    print("\nMa trận đã nhập là ma trận đối xứng.")
else:
    print("\nMa trận đã nhập không phải là ma trận đối xứng.")

def factorial(n):
    """Tính giai thừa của n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def permutations(n, r):
    """Tính số hoán vị của n phần tử lấy r phần tử mỗi lần."""
    return factorial(n) // factorial(n-r)

def combinations(n, r):
    """Tính số tổ hợp của n phần tử lấy r phần tử mỗi lần."""
    return factorial(n) // (factorial(r) * factorial(n-r))

print(f"Số hoán vị của 5 phần tử lấy 3 phần tử mỗi lần: {permutations(5, 3)}")
print(f"Số tổ hợp của 5 phần tử lấy 3 phần tử mỗi lần: {combinations(5, 3)}")
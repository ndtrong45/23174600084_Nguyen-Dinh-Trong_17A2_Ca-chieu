def sumPdivisors(n):
    """Tính tổng của các ước số chính của số n."""
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

print(f"Tổng các ước số chính của 36 là: {sumPdivisors(36)}")
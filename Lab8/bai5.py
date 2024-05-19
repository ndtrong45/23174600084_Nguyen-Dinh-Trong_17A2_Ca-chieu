def sum_proper_divisors(n):
    """Tính tổng các ước số chính của số n"""
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def are_amicable(a, b):
    """Kiểm tra xem a và b có phải là số amicable hay không"""
    if sum_proper_divisors(a) == b and sum_proper_divisors(b) == a:
        return True
    else:
        return False

a = 220
b = 284
if are_amicable(a, b):
    print(f"{a} và {b} là số amicable")
else:
    print(f"{a} và {b} không phải là số amicable")
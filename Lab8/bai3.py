def cubesum(n):
    """Tính tổng các lập phương của các chữ số riêng lẻ của số n."""
    total = 0
    for digit in str(n):
        total += int(digit) ** 3
    return total

def PrintArmstrong():
    """In ra tất cả các số Armstrong."""
    for i in range(1, 1001):
        if isArmstrong(i):
            print(i)

def isArmstrong(n):
    """Kiểm tra xem số n có phải là số Armstrong hay không."""
    return n == cubesum(n)

print(f"Tổng các lập phương của các chữ số riêng lẻ của 123 là: {cubesum(123)}")
PrintArmstrong()
print(f"Số 153 có phải là số Armstrong không? {isArmstrong(153)}")
print(f"Số 407 có phải là số Armstrong không? {isArmstrong(407)}")
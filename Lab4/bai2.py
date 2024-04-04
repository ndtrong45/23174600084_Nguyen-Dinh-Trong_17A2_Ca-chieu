so = 2
print("Các số nguyên tố nhỏ hơn 100 là:",end="")
while so < 100:
    nto = True
    if so < 2:
        nto = False
    else:
        for i in range(2, so):
            if so % i == 0:
                nto = False
                break
    if nto:
        print(so,end=" ")
    so += 1
print("\n")
i = 1
print("Các số chính phương nhỏ hơn 100 là:",end=" ")
while i * i < 100:
    print(i * i,end=" ")
    i += 1
print("\n")
a, b = 0, 1
print("Dãy số Fibonacci nhỏ hơn 1000 là: 0 ",end="")
while b < 1000:
    print(b,end=" ")
    a, b = b, a + b

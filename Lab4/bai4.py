n = int(input("Nhập một số nguyên lớn hơn 10: "))
a = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0
while a <= n:
    s1 += 6**a
    s2 += 1/(3**((2*a)+1))
    s3 += ((-1)**a)*(a**2)
    s4 += a*(a+1)*(a+2)
    a += 1
print("\nS1=",s1)
print("\nS2=",s2)
print("\nS3=",s3)
print("\nS4=",s4)
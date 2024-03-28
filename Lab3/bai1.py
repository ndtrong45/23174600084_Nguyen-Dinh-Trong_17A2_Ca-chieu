n=int(input("Nhập vào 1 số nguyên dương: "))
if n<=0:
    print("Vui lòng nhập lại")
else:
    # Tính tổng S1=1+2+3+...+n
    s1=0
    for i in range(1,n+1):
        s1+=i
    print("S1=",s1) 
    # Tính tổng S2=(1/1)+(1/2)+(1/3)+...+(1/n) 
    s2=0
    for i in range(1,n+1):
        s2+=(1/i)
    print("S2=",s2)
    # Tính tổng S3=(1/(2**0.5)+1/(4**0.5)+...+1/((2*n)**0.5))
    s3=0
    for i in range(2,n+1,2):
        s3+=(1/(i**0.5))
    print("S3=",s3)
    # Tính tổng S3=1-(1/2)+(1/3)-(1/4)+...+(((-1)**(n-1))/n)
    a=0
    b=0
    for i in range(1,n+1):
        if i%2 == 0:
            a+=(1/i)
        else:
            b+=(1/i)
    print("S4=",b-a)

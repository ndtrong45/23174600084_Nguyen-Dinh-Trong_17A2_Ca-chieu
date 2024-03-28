# Tìm các số nguyên tố từ 100 đến 1000
print("Các số nguyên tố từ 100 đến 1000 là: ",end="")
for n in range(100,1001):
    if n > 1:
        a = True
        for i in range(2,500):
            if n % i == 0:
                a = False
                break
        if a:
            print(n,end=" ")
print("\n")
# Tìm các số chính phương từ 1 đến 1000
print("Các số chính phương từ 1 đến 1000 là: ",end="")           
for i in range(1,1001):
    if i**0.5 == int(i**0.5):
        print(i,end=" ")
print("\n")
# Tìm dãy fibonaci từ 1 đến 100            
print("Dãy fibonaci từ 1 đến 100 là: ",end="")
a,b = 0,1
for i in range(1,101):
  print(a,end=" ")
  if a + b >= 100:
    break
  a,b = a+b,a 
print("\n")
# Tìm các số hoàn hảo nhỏ hơn 500
print("Các số hoàn hảo nhỏ hơn 500 là: ",end="")
for n in range(1,501):
  s=0
  for i in range(1,n):
    if n % i == 0:
      s+=i
  if s== n:
    print(n,end=" ")
print("\n")    
# Tính tổng của các số ngũ giác trong đoạn từ 1 đến 200
print("Tổng của các số ngũ giác trong đoạn từ 1 đến 200 là: ",end="")    
s=0
for n in range(1,201):
  p=(n*(3*n-1))/2
  if p <= 200:
    s+=p
print(s)



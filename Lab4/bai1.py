tong = 0
so_chan = " "
so_le = " "
k = 0
n = " "

while tong <= 1000:
    so = int(input("Nhập vào số nguyên dương:"))
    tong += so
    k += 1
    n += str(so) + " "
    if so % 2 == 0:
        so_chan += str(so) + " "
    else:
        so_le += str(so) + " "   

print("Các só đã nhập từ bàn phím là:",n)
print("Các số lẻ đã nhập là:",so_le)
print("Các số chẵn đã nhập là:",so_chan)
print("Số lượng số nguyên đã nhập là:",k)
    
            
        
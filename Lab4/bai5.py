a, b = map(int, input("Nhập vào hai số nguyên a và b: ").split())
print(
"""
Chương trình hiển thị menu phép tính:
    1. Phép cộng hai số
    2. Phép trừ hai số
    3. Phép nhân hai số
    4. Phép chia hai số
    5. Phép tính lũy thừa hai số 
    6. Phép tính căn bậc 2 hai số
    0. Thoát chương trình
"""
)
while True:
    lua_chon = int(input("Nhập vào lựa chọn: "))
    if lua_chon == 1:
        print(a,"+",b,"=",a+b)
        break
    elif lua_chon == 2:
        print(a,"-",b,"=",a-b)
        break
    elif lua_chon == 3:
        print(a,"*",b,"=",a*b)
        break
    elif lua_chon == 4:
        print(a,"/",b,"=",a/b)
        break
    elif lua_chon == 5:
        gt_a = 1
        gt_b = 1
        for i in range (1,a+1):
            gt_a*=i
        for i in range (1,b+1):
            gt_b*=i
        print(a,"!","=",gt_a)
        print(b,"!","=",gt_b)
        break
    elif lua_chon == 6:
        print("Căn bậc 2 của",a,"là:",a**0.5)
        print("Căn bậc 2 của",b,"là:",b**0.5)
        break
    elif lua_chon == 0:
        break
    else:
        print("Lựa chọn sai, vui lòng nhập lại")
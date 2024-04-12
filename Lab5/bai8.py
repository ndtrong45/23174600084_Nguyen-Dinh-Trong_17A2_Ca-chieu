while True:
    chuoi = input("Nhập vào chuỗi có độ dài hơn 10 ký tự: ")
    if len(chuoi) > 10:
        break
    else:
        print("Vui lòng nhập lại")

print("Chuỗi ký tự con từ vị trí 2 đến vị trí 8:",chuoi[1:8])
print("Chuỗi ký tự con gồm 5 ký tự từ vị trí 5:",chuoi[4:9])
print("Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:",chuoi[-3:])
print("Chuỗi sau khi chuyển thành chữ thường:",chuoi.lower())
print("Chuỗi sau khi chuyển thành chữ hoa:",chuoi.upper())
print("Chuỗi sau khi được đảo ngược:",chuoi[::-1])
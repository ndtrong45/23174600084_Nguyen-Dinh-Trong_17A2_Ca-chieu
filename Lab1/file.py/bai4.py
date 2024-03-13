canh_day=float(input("Nhập vào độ dài cạnh đáy của hình chóp: "))
chieu_cao=float(input("Nhập vào chiều cao của hình chóp: "))
dien_tich_xq=(chieu_cao*canh_day/2)*4 # Tính toán diện tích xung quanh
dien_tich_tp=dien_tich_xq+canh_day**2 # Tính toán diện tích toàn phần
the_tich=(canh_day**2)*chieu_cao/3 # Tính toán thể tích
print("Diện tích xung quanh:",round(dien_tich_xq,2))
print("Diện tích toàn phần:",round(dien_tich_tp,2))
print("Thể tích:",round(the_tich,2))
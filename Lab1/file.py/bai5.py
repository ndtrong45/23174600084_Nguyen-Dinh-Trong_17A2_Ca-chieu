so_gio=float(input("Nhập vào số giờ sử dụng máy lọc không khí: "))
cong_suat=220*1.5 # Tính toán công suất
dien_nang=cong_suat*so_gio/1000 # Tính toán điện năng tiêu thụ
tien_dien=dien_nang*5000 # Tính toán tổng tiền điện 
print("Tổng số tiền điện phải trả là:",tien_dien,"đồng")
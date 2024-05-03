danh_sach = {}
for i in range(10):
    print("Nhập tên sinh viên thứ",i+1,end=":")
    ten = input()
    diem_thi = int(input("Nhập điểm thi: "))
    danh_sach[ten] = diem_thi

danh_sach_xep_loai = {'F': 0, 'D': 0, 'C': 0, 'B': 0, 'A': 0}
for ten,diem_thi in danh_sach.items():
    if diem_thi >= 8.5:
        danh_sach_xep_loai['A'] += 1
    elif 7.0 <= diem_thi < 8.5:
        danh_sach_xep_loai['B'] += 1
    elif 5.5 <= diem_thi < 7.0:
        danh_sach_xep_loai['C'] += 1
    elif 4.0 <= diem_thi < 5.5:
        danh_sach_xep_loai['D'] += 1
    else:
        danh_sach_xep_loai['F'] += 1
        
print("Thống kê số lượng sinh viên ở mỗi loại học lực:\n",danh_sach_xep_loai)

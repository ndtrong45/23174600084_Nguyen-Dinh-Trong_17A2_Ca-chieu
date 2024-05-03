kho = {
  "banana": 6,
  "apple": 5,
  "orange": 32,
  "pear": 15
}

gia_tien = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

tong_gia_tri = 0
print("HÓA ĐƠN MUA HÀNG")

for ten_mat_hang, so_luong in kho.items():
  
  gia_tri_mat_hang = so_luong * gia_tien[ten_mat_hang]
  tong_gia_tri += gia_tri_mat_hang

  print(f"- {ten_mat_hang}: {so_luong} x {gia_tien[ten_mat_hang]} = {gia_tri_mat_hang}")

print(f"Tổng giá trị đơn hàng là: {tong_gia_tri}")
def tinh_giai_thua(n):
  # Hàm tính giai thừa của một số
  giai_thua = 1
  for i in range(1, n + 1):
    giai_thua *= i
  return giai_thua
def tinh_to_hop(n,k):
  # Hàm tính tổ hợp chập k của n
  return tinh_giai_thua(n) // (tinh_giai_thua(k) * tinh_giai_thua(n - k))
def main():
  # Hàm main của chương trình."""
  # Số lượng viên bi trong hộp
  so_luong_bi = 50
  # Số lượng bi đỏ
  so_luong_bi_do = 20
  # Số lượng bi xanh
  so_luong_bi_xanh = 15
  # Số lượng bi vàng
  so_luong_bi_vang = 15

  # Số lượng bi muốn rút
  so_luong_bi_rut = int(input("Nhập số lượng bi muốn rút: "))

  # Xác suất để tất cả là bi đỏ
  xac_suat_do = tinh_to_hop(so_luong_bi_do, so_luong_bi_rut) / tinh_to_hop(so_luong_bi, so_luong_bi_rut)

  # Xác suất để ít nhất một viên là bi xanh
  xac_suat_xanh = 1 - tinh_to_hop(so_luong_bi_xanh, so_luong_bi_rut) / tinh_to_hop(so_luong_bi, so_luong_bi_rut)

  # Xác suất để đúng hai viên là bi vàng
  xac_suat_vang = tinh_to_hop(so_luong_bi_vang, 2) * tinh_to_hop(so_luong_bi - so_luong_bi_vang, so_luong_bi_rut - 2) / tinh_to_hop(so_luong_bi, so_luong_bi_rut)

  print("Xác suất để tất cả là bi đỏ:",round(xac_suat_do,4))
  print("Xác suất để ít nhất một viên là bi xanh:",round(xac_suat_xanh,4))
  print("Xác suất để đúng hai viên là bi vàng:",round(xac_suat_vang,4))
main()

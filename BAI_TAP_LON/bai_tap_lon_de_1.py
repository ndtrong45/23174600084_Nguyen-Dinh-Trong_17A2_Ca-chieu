import csv
import random

def main():
  """Chương trình mô phỏng trò chơi tung xúc xắc."""

  # Nhập điểm số mục tiêu từ người dùng
  diem_muc_tieu = int(input("Nhập điểm số mục tiêu: "))

  # Khởi tạo biến lưu trữ kết quả
  tong_diem = 0
  luot_choi = 0
  thang = False

  # Vòng lặp cho phép người chơi tung xúc xắc hoặc dừng lại
  while True:
    luot_choi += 1

    # Tung xúc xắc và tính điểm
    diem_tung = random.randint(1, 6)
    tong_diem += diem_tung

    # Hiển thị kết quả lượt tung
    print(f"Lượt {luot_choi}: Tung được {diem_tung}, tổng điểm: {tong_diem}")

    # Kiểm tra nếu người chơi thắng
    if tong_diem == diem_muc_tieu:
      thang = True
      break

    # Kiểm tra nếu người chơi thua
    if tong_diem > diem_muc_tieu:
      break

    # Hỏi người chơi có muốn tiếp tục hay không
    lua_chon = input("Tiếp tục tung xúc xắc (c/k)? ").lower()
    if lua_chon != "c":
      break

  # Tính xác suất người chơi thắng
  xac_suat_thang = 0
  if thang:
    xac_suat_thang = 1 / 6**luot_choi

  # Lưu kết quả vào file CSV
  with open("ket_qua.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([diem_muc_tieu, tong_diem, thang, xac_suat_thang])

  # Hiển thị kết quả cuối cùng
  if thang:
    print(f"Bạn thắng!  Tổng điểm: {tong_diem}, Xác suất thắng: {xac_suat_thang:.2f}")
  else:
    print(f"Bạn thua!  Tổng điểm: {tong_diem}")

if __name__ == "__main__":
  main()

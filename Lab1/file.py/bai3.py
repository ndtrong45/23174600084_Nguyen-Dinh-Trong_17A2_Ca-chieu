tien_ban_dau = 10000  # Số tiền đầu tư ban đầu
amount_after_5_years = tien_ban_dau * (1 + 0.6)**5 # Tính toán số tiền sau 5 năm
amount_after_10_years = tien_ban_dau * (1 + 0.6)**10 #Tính toán số tiền sau 5 năm
growth_rate = (amount_after_10_years - amount_after_5_years) / amount_after_5_years # Tính số tiền tăng trưởng
print("Số tiền sau 5 năm:",amount_after_5_years)
print("Số tiền sau 10 năm:",amount_after_10_years)
print("Tỷ lệ tăng trưởng:",growth_rate)

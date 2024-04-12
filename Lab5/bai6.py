str = input("Nhập một chuỗi: ")
ky_tu_dac_biet = []
slg_ky_tu = {}
tong_ky_tu = len(str)

for i in str:
    if not i.isalnum():  
        ky_tu_dac_biet.append(i)
        if i in slg_ky_tu:
            slg_ky_tu[i] += 1
        else:
            slg_ky_tu[i] = 1

for i in set(ky_tu_dac_biet):
    print("Ký tự",i,"xuất hiện",slg_ky_tu[i],"lần trong chuỗi")

for i in set(ky_tu_dac_biet):
    ti_le = (slg_ky_tu[i] / tong_ky_tu) * 100
    print("Ký tự",i,"chiếm",round(ti_le,2),"%")
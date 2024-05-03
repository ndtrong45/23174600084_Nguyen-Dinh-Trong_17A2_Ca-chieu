van_ban = "Postman of our area, Mr. Ramesh Gupta, is a very sincere person. He knows his work very well. He can tell any address of the locality. He has detail map of the area in his mind. He is working in this for last fifteen years. We never missed any letter or parcel. He is always in his khaki uniform. For illiterate people he also read the letters. He is always smiling, although his work is quite difficult. He has to cover long distances by his cycle even in the extreme weather. He is a hard worker. I like him."
a = van_ban.lower().split()
so_luong_tu = {}
for tu in a:
    if tu in so_luong_tu:
      so_luong_tu[tu] += 1
    else:
      so_luong_tu[tu] = 1
tu_nhieu_nhat = max(so_luong_tu, key=so_luong_tu.get)
tu_it_nhat = min(so_luong_tu, key=so_luong_tu.get)
print("Từ xuất hiện nhiều nhất:", tu_nhieu_nhat, "(",so_luong_tu[tu_nhieu_nhat], "lần)")
print("Từ xuất hiện ít nhất:", tu_it_nhat, "(",so_luong_tu[tu_it_nhat], "lần)")

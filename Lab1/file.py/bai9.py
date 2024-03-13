x1,y1= map(int, input("Nhập tọa độ M:").split())
x2,y2= map(int, input("Nhập tọa độ N:").split())
x3,y3= map(int, input("Nhập tọa độ P:").split())
x4,y4= map(int, input("Nhập tọa độ Q:").split())
# Tính tọa độ trung điểm của MN
xmn=x1+x2
ymn=y1+y2
# Tính tọa độ trung điểm của NP
xnp=x2+x3
ynp=y2+y3
# Tính tọa độ trung điểm của PQ
xpq=x3+x4
ypq=y3+y4
# Tính tọa độ trung điểm của QM
xqm=x1+x4
yqm=y1+y4
print("Tọa độ trung điểm của MN:",xmn,",",ymn)
print("Tọa độ trung điểm của NP:",xnp,",",ynp)
print("Tọa độ trung điểm của PQ:",xpq,",",ypq)
print("Tọa độ trung điểm của QM:",xqm,",",yqm)
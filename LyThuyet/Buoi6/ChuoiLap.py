s = input("Nhập chuỗi: ")

tu = s.split()
da_xuat_hien = []
ket_qua = None

for x in tu:
    if x in da_xuat_hien:
        ket_qua = x
        break
    da_xuat_hien.append(x)

print("Từ lặp đầu tiên:", ket_qua)
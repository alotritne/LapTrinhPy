# Các loại tiền
tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

x = int(input("Nhập số tiền X: "))

tong_to = 0

print(f"So tien {x} duoc doi thanh:")

for loai in tien:
    so_to = x // loai
    x = x % loai
    
    tong_to += so_to
    
    print(f"Loai {loai} gom {so_to} to")

print("TONG CONG CO", tong_to, "TO")
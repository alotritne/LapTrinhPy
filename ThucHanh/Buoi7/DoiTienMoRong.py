# Các loại tiền
tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

a = int(input("Nhập số tiền cần trả: "))
b = int(input("Nhập số tiền khách đưa: "))

# Khách đưa thiếu
if a > b:
    print("Khách còn thiếu:", a - b)

# Khách đưa vừa đủ
elif a == b:
    print("Cảm ơn khách hàng. Hẹn gặp lại")

# Khách đưa dư
else:
    tien_thoi = b - a

    print("Số tiền cần thối lại:", tien_thoi)

    tong_to = 0

    for loai in tien:
        so_to = tien_thoi // loai
        tien_thoi = tien_thoi % loai

        if so_to > 0:
            print(f"Loại {loai} gồm {so_to} tờ")
            tong_to += so_to

    print("Tổng cộng có", tong_to, "tờ")

    input("Nhấn Enter để kết thúc...")

    print("Cảm ơn khách hàng. Hẹn gặp lại")
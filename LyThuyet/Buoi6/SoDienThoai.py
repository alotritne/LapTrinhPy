s = input("Nhập số điện thoại: ")

khong_co = []

for i in range(10):
    if str(i) not in s:
        khong_co.append(i)

print("Các chữ số không xuất hiện:", khong_co)
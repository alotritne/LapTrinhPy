def is_strobogrammatic(num):
    # Các cặp số khi xoay 180 độ
    mapping = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    rotated = ""

    # Duyệt ngược chuỗi số
    for digit in reversed(num):
        if digit not in mapping:
            return False
        rotated += mapping[digit]

    return rotated == num


# =========================
# TEST
# =========================

numbers = ["916", "68910", "88", "101", "9966"]

for n in numbers:
    if is_strobogrammatic(n):
        print(f"{n} là số strobogrammatic")
    else:
        print(f"{n} không phải số strobogrammatic")
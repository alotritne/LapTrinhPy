# ==================================================
# PHÁT SINH SỐ STROBOGRAMMATIC N CHỮ SỐ
# 2 <= n <= 10
# ==================================================

# --------------------------------------------------
# a. STROBOGRAMMATIC THƯỜNG
# --------------------------------------------------

NORMAL_PAIRS = [
    ('0', '0'),
    ('1', '1'),
    ('6', '9'),
    ('8', '8'),
    ('9', '6')
]

# --------------------------------------------------
# b. STROBOGRAMMATIC MỞ RỘNG
# --------------------------------------------------

EXTENDED_PAIRS = [
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('5', '5'),
    ('6', '9'),
    ('8', '8'),
    ('9', '6')
]


# ==================================================
# HÀM ĐỆ QUY PHÁT SINH
# ==================================================

def build_strobogrammatic(n, total_len, pairs):

    # hết ký tự
    if n == 0:
        return [""]

    # còn 1 ký tự ở giữa
    if n == 1:

        middle = []

        for a, b in pairs:
            if a == b:
                middle.append(a)

        return middle

    result = []

    middle_numbers = build_strobogrammatic(n - 2, total_len, pairs)

    for mid in middle_numbers:

        for a, b in pairs:

            # số đầu không được là 0
            if n == total_len and a == '0':
                continue

            result.append(a + mid + b)

    return result


# ==================================================
# NHẬP n
# ==================================================

n = int(input("Nhập n (2 <= n <= 10): "))

if n < 2 or n > 10:
    print("n không hợp lệ!")
else:

    # ==============================================
    # a. STROBOGRAMMATIC THƯỜNG
    # ==============================================

    print("\na. Các số strobogrammatic gồm", n, "chữ số:\n")

    normal_numbers = build_strobogrammatic(
        n,
        n,
        NORMAL_PAIRS
    )

    for num in normal_numbers:
        print(num, end=" ")

    # ==============================================
    # b. STROBOGRAMMATIC MỞ RỘNG
    # ==============================================

    print("\n\nb. Các số strobogrammatic mở rộng gồm", n, "chữ số:\n")

    extended_numbers = build_strobogrammatic(
        n,
        n,
        EXTENDED_PAIRS
    )

    for num in extended_numbers:
        print(num, end=" ")
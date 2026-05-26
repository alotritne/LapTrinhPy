import math

# =========================
# KIỂM TRA STROBOGRAMMATIC MỞ RỘNG
# =========================

def is_strobogrammatic(num):
    # mapping khi xoay 180 độ
    mapping = {
        '0': '0',
        '1': '1',
        '2': '2',
        '5': '5',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    rotated = ""

    for digit in reversed(num):
        if digit not in mapping:
            return False

        rotated += mapping[digit]

    return rotated == num


# =========================
# KIỂM TRA SỐ NGUYÊN TỐ
# =========================

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# =========================
# KIỂM TRA SỐ NGUYÊN TỐ STROBOGRAMMATIC
# =========================

def is_strobogrammatic_prime(n):
    s = str(n)

    return is_strobogrammatic(s) and is_prime(n)


# =========================
# TEST
# =========================

numbers = [11, 101, 181, 619, 16091, 123, 888]

for n in numbers:
    if is_strobogrammatic_prime(n):
        print(f"{n} là số nguyên tố strobogrammatic")
    else:
        print(f"{n} không phải số nguyên tố strobogrammatic")
import math

LIMIT = 1_000_000

# ==================================================
# STROBOGRAMMATIC THƯỜNG
# ==================================================

NORMAL_MAP = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
}

# ==================================================
# STROBOGRAMMATIC MỞ RỘNG
# ==================================================

EXTENDED_MAP = {
    '0': '0',
    '1': '1',
    '2': '2',
    '5': '5',
    '6': '9',
    '8': '8',
    '9': '6'
}

# ==================================================
# HÀM XOAY SỐ
# ==================================================

def rotate_number(num_str, mapping):

    rotated = ""

    for ch in reversed(num_str):

        if ch not in mapping:
            return None

        rotated += mapping[ch]

    return rotated


# ==================================================
# KIỂM TRA STROBOGRAMMATIC
# ==================================================

def is_strobogrammatic(n):

    s = str(n)

    rotated = rotate_number(s, NORMAL_MAP)

    return rotated == s


# ==================================================
# KIỂM TRA STROBOGRAMMATIC MỞ RỘNG
# ==================================================

def is_extended_strobogrammatic(n):

    s = str(n)

    rotated = rotate_number(s, EXTENDED_MAP)

    return rotated == s


# ==================================================
# KIỂM TRA NGUYÊN TỐ
# ==================================================

def is_prime(n):

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        if n % i == 0:
            return False

    return True


# ==================================================
# a. STROBOGRAMMATIC < 1 TRIỆU
# ==================================================

print("a. CÁC SỐ STROBOGRAMMATIC:\n")

for i in range(LIMIT):

    if is_strobogrammatic(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# b. SỐ NGUYÊN TỐ STROBOGRAMMATIC
# ==================================================

print("b. SỐ NGUYÊN TỐ STROBOGRAMMATIC:\n")

for i in range(LIMIT):

    if is_strobogrammatic(i) and is_prime(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# c. STROBOGRAMMATIC MỞ RỘNG
# ==================================================

print("c. STROBOGRAMMATIC MỞ RỘNG:\n")

for i in range(LIMIT):

    if is_extended_strobogrammatic(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# d. NGUYÊN TỐ STROBOGRAMMATIC MỞ RỘNG
# ==================================================

print("d. NGUYÊN TỐ STROBOGRAMMATIC MỞ RỘNG:\n")

for i in range(LIMIT):

    if is_extended_strobogrammatic(i) and is_prime(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# e.
# KHÔNG PHẢI STROBOGRAMMATIC
# KHÔNG PHẢI NGUYÊN TỐ
# NHƯNG SỐ XOAY LẠI LÀ NGUYÊN TỐ
# ==================================================

print("e. CÁC SỐ THỎA ĐIỀU KIỆN:\n")

for i in range(LIMIT):

    s = str(i)

    rotated = rotate_number(s, NORMAL_MAP)

    # bỏ nếu không xoay được
    if rotated is None:
        continue

    rotated_num = int(rotated)

    if (
        not is_strobogrammatic(i)
        and not is_prime(i)
        and is_prime(rotated_num)
    ):
        print(f"{i} -> {rotated_num}")
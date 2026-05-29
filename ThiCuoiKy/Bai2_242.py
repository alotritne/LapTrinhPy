import math
# in ra bảng cửu chương
def bangCuuChuong(a, b):
    if a < b:
        print("Ban cuu chuong tu a -> b:")
        for i in range(a, b + 1):
            print(f"Bang cuu chuong {i}")
            for j in range(1, 11):
                print(f"{i} * {j} = {i * j}")
    elif a > b:
        print("Ban cuu chuong tu b -> a:")
        for i in range(b, a + 1):
            print(f"Bang cuu chuong {i}")
            for j in range(1, 11):
                print(f"{i} * {j} = {i * j}")

# kiểm tra số nguyên tố
def laSNT(n):
    if n < 2:
        return False
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
    return True

# liệt kê số nguyện tố
def lietKeSNT(n):
    for i in range(2, n + 1):
        if laSNT(i) == True:
            print(i)

# kiểm tra có phải ước sô không
def laUocSo(a, b):
    return a % b == 0

# liệt kê các ước số l2a số nguyên tố
def lietKeCacUocSoLaSNT(n):
    for i in range(2, n):
        if laSNT(i) and laUocSo(n, i):
            print(i)

a = int(input("Nhap vao a: "))
b = int(input("Nhap vao b: "))
bangCuuChuong(a, b)


n = int(input("Nhap vao n: "))
print(f"cac so nguyen to < {n}: ")
lietKeSNT(n)

print(f"Cac uoc so cua {n} la snt:")
lietKeCacUocSoLaSNT(n)
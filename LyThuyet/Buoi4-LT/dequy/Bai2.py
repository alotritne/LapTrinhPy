def GiaiThua(n: int):
    if (n == 1):
        return 1
    return n * GiaiThua(n - 1)

n = int(input("Nhap vao so n: "))

print(GiaiThua(n))
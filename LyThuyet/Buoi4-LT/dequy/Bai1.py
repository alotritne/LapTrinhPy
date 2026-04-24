def Sum(n: int):
    if (n == 0):
        return 0
    return n % 10 + Sum(n // 10)

n: int = int(input("Nhap vao n: "))
print(Sum(n))
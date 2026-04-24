def APowerB(n: int, m: int) -> int:
    if (m == 0):
        return 1
    return n * APowerB(n, m - 1)
    

n = int(input("Nhap vao n: "))
m = int(input("Nhap vao m: "))

print(APowerB(n, m))
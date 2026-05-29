n = input("Nhap vao N: ")

# hàm kiểm tra số đồng nhất
soDongNhat = lambda n: int(n) > 0 and all(char == n[0] for char in n)

# hoàn kiểm tra số hoàn thiện
soHoanThien = lambda n: int(n) > 0 and sum(i for i in range(1, int(n)) if int(n) % i == 0) == int(n)

if soDongNhat(n):
    print(f"{n} la so dong nhat")
else:
    print(f"{n} khong phai la so dong nhat")

if soHoanThien(n):
    print(f"{n} la so hoan thien")
else:
    print(f"{n} khong phai la so hoan thien")

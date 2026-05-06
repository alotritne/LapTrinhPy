# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập danh sách số nguyên
lst = []

while True:
    n = int(input("Nhập số nguyên: "))
    lst.append(n)

    tiep = input("Bạn có muốn nhập tiếp không? (Y/N): ").strip().upper()

    if tiep == "N":
        break

# a) In ra các số nguyên tố
print("\nCác số nguyên tố trong list:")
primes = [x for x in lst if is_prime(x)]
print(primes)

# b) Tính trung bình cộng số âm và số dương
so_am = [x for x in lst if x < 0]
so_duong = [x for x in lst if x > 0]

if so_am:
    tbc_am = sum(so_am) / len(so_am)
    print("Trung bình cộng số âm:", tbc_am)
else:
    print("Không có số âm")

if so_duong:
    tbc_duong = sum(so_duong) / len(so_duong)
    print("Trung bình cộng số dương:", tbc_duong)
else:
    print("Không có số dương")

# c) Số lớn nhất, nhỏ nhất
print("Số lớn nhất:", max(lst))
print("Số nhỏ nhất:", min(lst))

# d) Kiểm tra list có tăng dần hay không
tang_dan = True

for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        tang_dan = False
        break

if tang_dan:
    print("Danh sách đã được sắp xếp tăng dần")
else:
    print("Danh sách chưa được sắp xếp tăng dần")
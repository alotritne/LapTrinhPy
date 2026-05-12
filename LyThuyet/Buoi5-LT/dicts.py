# Nhập 2 chuỗi
s1 = input("Nhập chuỗi S1: ")
s2 = input("Nhập chuỗi S2: ")

# Đưa mỗi chuỗi vào dict
dict1 = {}
dict2 = {}

# Đếm ký tự trong S1
for ch in s1:
    dict1[ch] = dict1.get(ch, 0) + 1

# Đếm ký tự trong S2
for ch in s2:
    dict2[ch] = dict2.get(ch, 0) + 1

# a) In ra ký tự xuất hiện trong cả 2 chuỗi
print("\nCác ký tự xuất hiện trong cả 2 chuỗi:")
common = []

for ch in dict1:
    if ch in dict2:
        common.append(ch)

print(common)

# b) Đếm ký tự chỉ có trong S1 và chỉ có trong S2
count_s1 = 0
count_s2 = 0

for ch in dict1:
    if ch not in dict2:
        count_s1 += 1

for ch in dict2:
    if ch not in dict1:
        count_s2 += 1

print("\nSố ký tự có trong S1 nhưng không có trong S2:", count_s1)
print("Số ký tự có trong S2 nhưng không có trong S1:", count_s2)

# c) In các ký tự chỉ có trong từng chuỗi
only_s1 = []
only_s2 = []

for ch in dict1:
    if ch not in dict2:
        only_s1.append(ch)

for ch in dict2:
    if ch not in dict1:
        only_s2.append(ch)

print("\nKý tự có trong S1 nhưng không có trong S2:")
print(only_s1)

print("Ký tự có trong S2 nhưng không có trong S1:")
print(only_s2)
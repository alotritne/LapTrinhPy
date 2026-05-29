# kiểm tra bội số
n = int(input("Nhap vao n: "))
boiso = lambda n: n % 13 == 0 or n % 19 == 0
if boiso(n):
    print(f"{n} la boi so cua 13 hoac 19")
else:
    print(f"{n} khong phai la boi so cua 13 hoac 19")


# kiểm tra tam giác
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

tamgiac = lambda a, b, c: a + b > c and a + c > b and b + c > a

if tamgiac(a, b, c):

    if a == b == c:
        print("Tam giac deu")

    elif a == b or a == c or b == c:
        print("Tam giac can")

    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giac vuong")

    else:
        print("Tam giac thuong")

else:
    print("Khong phai tam giac")
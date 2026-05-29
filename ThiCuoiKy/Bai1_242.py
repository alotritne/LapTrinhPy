chieuDaiDay = float(input("Nhap vao chieu dai day hinh chu nhat > 2.134: "))
chieuRong = float(input("Nhap vao chieu rong hinh chu nhat > 3.4567: "))
chieuCao = float(input("Nhap vao chieu cao hinh chu nhat > 4.1: "))
soLe = int(input("Nhap vao so le can hien thi > 2: "))


dienTichDay = round(chieuDaiDay * chieuRong, soLe)
theTich = round(chieuDaiDay * chieuRong * chieuCao, soLe)

print("Dien tich day hinh chu nhat =", dienTichDay, "cm\u00b2")
print("The tich hinh khoi =", theTich, "cm\u00b3")
# 1. Cho người dùng nhập vào hai số nguyên và trả về tích của chúng. Nếu kết quả
# lớn hơn 1000 thì trả về tổng của chúng.

a = input()
b = input()

try:
    so1 = int(a)
    so2 = int(b)
    tich = so1 * so2
    if tich > 1000:
        print("Tổng hai so la: ", so1+so2)
    else:
        print("Tích hai so la: ", tich)
except:
    print("dinh dang dau vao khong hop le!")



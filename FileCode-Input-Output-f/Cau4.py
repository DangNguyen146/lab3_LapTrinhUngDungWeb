n = input()
text = input()

try:
    print(text[len(text)-int(n):len(text)])
except:
    print("dinh dang dau vao khong hop le!")
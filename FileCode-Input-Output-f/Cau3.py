text = input()
try:
    for item in text:
        if(text.index(item)%2!=0):
            print (item)
except:
    print("dinh dang dau vao khong hop le!")


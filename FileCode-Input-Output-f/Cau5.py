n = int(input("Nhập số phần tử của dãy số : "))
mylist = []
for i in range(n):
   val = int(input('Nhập một số: '))
   mylist.append(val)
if (mylist[0] == mylist[n-1]):
   print("true")
else:
   print("false")
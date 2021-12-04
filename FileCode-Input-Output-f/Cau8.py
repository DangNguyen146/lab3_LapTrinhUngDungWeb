import random

n = int(input("Nhập số phần tử của dãy số : "))
mylist = []
for i in range(n):
   val = random.randint(1, 1000)
   mylist.append(val)



path_w = 'f.txt'
s = ''
for item in mylist:
    temp = ''
    for i in range(mylist.index(item)):
        temp += ' '
    s += temp + str(item) + '\n'

with open(path_w, mode='w') as f:
    f.write(s)

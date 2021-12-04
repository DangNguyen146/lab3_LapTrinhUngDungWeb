n = int(input("Nhập số phần tử của dãy số : "))
mylist = []
for i in range(n):
   val = int(input('Nhập một số: '))
   mylist.append(val)

mylist2 = list(set(mylist))

path_a = 'f.txt'
f = open(path_a)
print(f.read())

with open(path_a, mode='a') as f:
    for item in mylist2:
        f.write('\n'+ str(item))

with open(path_a) as f:
    print(f.read())

f.close()

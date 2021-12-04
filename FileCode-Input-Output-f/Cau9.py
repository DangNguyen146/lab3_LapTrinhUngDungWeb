mylist = []

f = open('f.txt', 'r', encoding='UTF-8')
data = f.read()
data = data.replace(" ", "")
data = data.rstrip("\n")
mylist = data.split("\n")
for i in mylist:
    if(len(mylist)-1 != mylist.index(i)):
        print(i+ '+', end='')
    else:
        print(i+ '= ', end='')
sums=0
for i in mylist:
    sums += int(i)
print(sums)

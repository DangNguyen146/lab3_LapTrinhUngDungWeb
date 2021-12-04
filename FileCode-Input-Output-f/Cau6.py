def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n)
    return False


n = int(input("Nhập số phần tử của dãy số : "))
mylist = []
for i in range(n):
   val = int(input('Nhập một số: '))
   mylist.append(val)
mylist2 = sorted(mylist)
for item in mylist2:
    is_prime(item)
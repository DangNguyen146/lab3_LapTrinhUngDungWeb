path_a = 'f.txt'
f = open(path_a)
print(f.read())

l = 'Lập trình ứng dụng WEB'

with open(path_a, mode='a') as f:
    f.write('\n' + l)

with open(path_a) as f:
    print(f.read())

f.close()



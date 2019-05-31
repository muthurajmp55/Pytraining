def gen1():
    n=1

    while True:
        yield n
        n = n + 1
j=0
for i in gen1():
    print(i)

    j=j+1

    if j> 15:
        break
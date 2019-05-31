k=[7,4,13,99,5]


for start in range(len(k)):
    min=start
    for r in range(len(k)):
        if k[r]> k[min]:
            min=r
            k[min],k[start] = k[start], k[min]

print(k)
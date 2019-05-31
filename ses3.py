
x = input("give a word")
y = input("give a letter")


count = 0
l = len(x)

def word(x,y,l,count):
    for i in range(l):
        if x[i] == y :
            count = count +1 
    print(count)      


word(x,y,l,count) 




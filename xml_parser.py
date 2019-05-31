import xml.etree.ElementTree as ET




filename = 'word_search.txt'
#count = 0

def search_word(x):
    count=0
    with open(filename) as f:
        contents = f.read()
    print(contents)
    words = contents.split()
    print(words)

    for word in words:
        print(word)
        if word == x:
            print('h')
            count += 1
    print("total count" + str(count))

def print_result():
    # global count
    if count > 0:
        print("There was a match!!")
        print("The word appeared " + str(count) + " times!")
    else:
        print("There was no match!!")

sword = input("Enter the word you want to search: \n>")
search_word(sword)
print_result()




roles =('admin', 'root', ['a', 'b', 'c'])

user_roles=('admin', 'root', 'c')

x = list((2,2,2,2,2))

for i in x:
     if (i == 2) | (i == 3):
         x.remove(i)

print(x)




inlst = ['BHX', 'AR', 'DEFab', 'ABR', 'DEFyr', 'HYt', 'wqw', 'DEF-a']
tem=''
olt=[]
for i in inlst:
    if str(i).startswith('DEF'):
        tem  = tem +  str(i)
        olt.append(tem)
        tem=''
    else:
        tem  = tem + str(i)

print(olt)



def check(roles):
    if ('admin' in roles) and ('root' in roles):
        if isinstance(roles[2],str):
            if  'a' == roles[2] or 'b' == roles[2] or 'c' == roles[2]:
                print('these satisfy both conditions')
        elif isinstance(roles[2],list):
            if 'a' in roles[2] or 'b' in roles[2] or 'c' in roles[2]:
                print('these satisfy both conditions')
check(roles)
check(user_roles)


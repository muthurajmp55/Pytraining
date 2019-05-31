import re
s = "RSQ(name['BAKD DK'], name['A DKJ'])"

k='f,sf,sf(ABCC,nb,nm,AC)fd,fd,fd'

print(re.sub(r"name\['(.*?)'\]", r"'\1'", s))
#k=k.replace('')
k1=re.sub(r"\((\w+),", r"('\1',", k)
print(k1)
k2=re.sub(r",(\w+)\)", r",'\1')", k1)
print(k2)
k3=re.sub(r"\((\w+),(\w+),(\w+),(\w+)\)",r"('\1','\2','\3','\4')",k)
print(k3)


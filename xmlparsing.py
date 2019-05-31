import xml.etree.ElementTree as ET
'''
tree=ET.parse('sample.xml')
root=tree.getroot()

print(root)
for child in root:
    print(child.tag,child.attrib)'''

n=5
print('*' *10 )
for i in range(0,n):
    print (' ' * (n-i),end='')
    print('*' * ((2 * i) + 1))

for i in range(n-2, -1,-1):
    print(' ' * (n - i), end='')
    print('*' *( (2*i) +1 ))
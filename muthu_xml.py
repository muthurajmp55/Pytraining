print('-' * 75)

import xml.etree.ElementTree as ET

# Filename
xml_fname = 'employee.xml'

# Parse the XML file
tree = ET.parse(xml_fname)
print('XML Parsed ->', tree)

print('-' * 75)

# Get the root tag
root = tree.getroot()
print('Root Tag ->', root.tag)
print('Attributes ->', root.attrib)
print('Size ->', root.attrib['size'])

print('-' * 75)

# Iterate through the employee tag
for emp in root.findall('employee'):
    ename = emp.attrib['fname'] + ' ' + emp.attrib['lname']
    eid = emp.find('id').text
    eloc = emp.find('location').text
    esal = emp.find('salary').text

    print(ename, eid, eloc, esal, sep=' -> ')

print('-' * 75)

# Update the location details
for loc in root.iter('location'):
    if loc.text == 'Noida':
        loc.text += ' Urban'
        loc.set('Office', 'Olympia Tech Park')
    elif loc.text == 'Mumbai':
        loc.text += ' City'
        loc.set('Office', 'Tidel Park')
    elif loc.text == 'Chennai':
        loc.text += ' City'
        loc.set('Office', 'Ramanujan IT Park')

tree.write('emp_upd.xml')
print('XML Updated and Saved')

print('-' * 75)

all_emp = root.iter('employee')
print(all_emp)

print('-' * 75)

# Remove the employee
for emp in root.findall('employee'):
    esal = int(emp.find('salary').text)
    print('Salary ->', esal, '->', type(esal))

    if esal < 30000:
        root.remove(emp)

tree.write('emp_removed.xml')

print('Data Removed and Saved')

print('-' * 75)

# Adding the tag
all_emp = root.findall('employee')

for emp in all_emp:
    team = ET.SubElement(emp, 'team')
    name = ET.SubElement(team, 'name')

    print(team)

    if emp.attrib['fname'] == 'gana':
        name.text = 'Development'
    elif emp.attrib['fname'] == 'ram':
        name.text = 'Testing'

tree.write('emp_added.xml')

print('Data Added and Saved')

print('-' * 75)

for child in root:
    print(child.tag)

print('-' * 75)
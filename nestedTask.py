names= [
    ['Alice','Bob','Charlie'],
    ['David','Eve','Frank'],
    ['Grace','Heidi','Ivan'],
    ['judy','Ken','Laura']
]

alice_found= False

for list in names:
    if 'Alice' in list:
        list.remove("Alice")
        Alice_found = True


if Alice_found:
    new_name = input("Alice found. enter a new name to add: ")
    names[0].append(new_name) 

print(names)

for list in names:
    for name in list:
        print(name)
    


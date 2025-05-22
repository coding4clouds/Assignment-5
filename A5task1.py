dictionary={'Radha':100,'Raju':75,'Alice':85}
name=input('Enter students name: ').capitalize()
keys=dictionary.keys()
if name in keys:
    print(name,':',dictionary[name])
else:
    print('Student not found')

print('This Program Calculates Weight and Mass')

#Ask For
mass = int(input('What is the mass of the object?'))

#Calculate Mass of The Object
weight = mass * 9.8

#Determining The Weight of the Object

if weight >= 500:
    print('This Object is too Heavy')
    print(weight)
elif weight <= 100:
    print('This Object is too Light')
    print(weight)
else:
    print('Here is the Weight of the Object')
    print(weight)



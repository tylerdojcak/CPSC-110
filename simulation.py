#Stephen Dojcak
#Promotion Simulation
#Pledge: Stephen Dojcak


from random import *


#variables
rounds = 50
bias = 2
#employee class
class Employee:
    favor = 0
    rank = 0


#levels
level1 = []
level2 = []
level3 = []
level4 = []
level5 = []

for i in range(500):
    employee = Employee()
    level1.append(employee)
for employee in level1:
    employee.favor = employee.favor + randint(0,1)

for i in range(200):
    employee = Employee()
    level2.append(employee)
for employee in level2:
    employee.favor = employee.favor + randint(0,1)

for i in range(75):
    employee = Employee()
    level3.append(employee)
for employee in level3:
    employee.favor = employee.favor + randint(0,1)

for i in range(25):
    employee = Employee()
    level4.append(employee)
for employee in level4:
    employee.favor = employee.favor + randint(0,1)

for i in range(10):
    employee = Employee()
    level5.append(employee)
for employee in level5:
    employee.favor = employee.favor + randint(0,1)

#loop
for i in range(rounds):
#ranking    
    for employee in level1:
        employee.rank = employee.rank + randint(0, 25)
        if employee.favor == 1:
            employee.rank = employee.rank + bias

    for employee in level2:
        employee.rank = employee.rank + randint(0, 25)
        if employee.favor == 1:
            employee.rank = employee.rank + bias

    for employee in level3:
        employee.rank = employee.rank + randint(0, 25)
        if employee.favor == 1:
            employee.rank = employee.rank + bias

    for employee in level4:
        employee.rank = employee.rank + randint(0, 25)
        if employee.favor == 1:
            employee.rank = employee.rank + bias

    for employee in level5:
        employee.rank = employee.rank + randint(0, 25)
        if employee.favor == 1:
            employee.rank = employee.rank + bias


    #employees leaving
    shuffle(level1)
    for i in range(round(500*.15)):
        del level1[0]

    shuffle(level2)
    for i in range(round(200*.15)):
        del level2[0]

    shuffle(level3)
    for i in range(round(75*.15)):
        del level3[0]

    shuffle(level4)
    for i in range(round(25*.15)):
        del level4[0]

    shuffle(level5)
    for i in range(round(10*.15)):
        del level5[0]



    #promotions
    while len(level5) < 10:
        top = max(level4, key = lambda employee: employee.rank)
        level4.remove(top)
        level5.append(top)

    while len(level4) < 25:
        top = max(level3, key = lambda employee: employee.rank)
        level3.remove(top)
        level4.append(top)

    while len(level3) < 75:
        top = max(level2, key = lambda employee: employee.rank)
        level2.remove(top)
        level3.append(top)

    while len(level2) < 200:
        top = max(level1, key = lambda employee: employee.rank)
        level1.remove(top)
        level2.append(top)

    while len(level1) < 500:
        employee = Employee()
        employee.favor = employee.favor + randint(0,1)
        level1.append(employee)


#count
a = 0
for employee in level5:
    if employee.favor == 1:
        a = a + 1

print("Favored employees in top level: ", a)
print("Unfavored employees in top level: ", 10-a)
print("")

b = 0
for employee in level4:
    if employee.favor == 1:
        b = b + 1

print("Favored employees in second level: ", b)
print("Unfavored employees in second level: ", 25-b)
print("")

c = 0
for employee in level3:
    if employee.favor == 1:
        c = c + 1

print("Favored employees in third level: ", c)
print("Unfavored employees in third level: ", 75-c)
print("")

d = 0
for employee in level2:
    if employee.favor == 1:
        d = d + 1

print("Favored employees in fourth level: ", d)
print("Unfavored employees in fourth level: ", 200-d)
print("")

e = 0
for employee in level1:
    if employee.favor == 1:
        e = e + 1

print("Favored employees in bottom level: ", e)
print("Unfavored employees in bottom level: ", 500-e)
print("")






    



    

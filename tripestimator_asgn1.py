#Stephen Dojcak
#Trip Estimator
#Pledge: Stephen Dojcak

print("Hello! We can help calculate how long your trip will take.")
dist = float(input("How many miles will you be travelling? "))
while dist <= 0:
    dist = float(input("Please give a positive distance. How many miles will you be travelling? "))

speed = float(input("Now, how fast will you be travelling in miles per hour? "))
while speed <= 0:
    speed = float(input("Please give a positive speed. How fast will you be travelling in miles per hour? "))


conf = int(input("So you will be travelling " + str(dist) + " miles at " + str(speed) + " miles per hour. Is this correct? Press '1' for yes or '0' for no. " )) 
while conf!= 1:
    dist = float(input("How many miles will you be travelling? "))
    while dist <= 0:
        dist = float(input("Please give a positive distance. How many miles will you be travelling? "))
    speed = float(input("How fast will you be travelling in miles per hour? "))
    while speed <= 0:
        speed = float(input("Please give a positive speed. How fast will you be travelling in miles per hour? "))
    print("So you will be travelling ", dist, " miles at ", speed, " miles per hour.")
    conf = int(input("Is this correct? Press '1' for yes or '0' for no. "))


time = (dist/speed)*60
print("It will take you", round(time, 2), "minutes to go", dist, "miles at", speed, "miles per hour.")

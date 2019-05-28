n = int(input("Choose a non-negative number for which to take the factorial. "))
while n < 0:
    n = int(input("Number cannot be negative. Pick again. "))
    
    
facn = 1


for i in range(0, n, 1):
    facn = facn*(i+1)

print(n,"!", " = ", facn, sep="")

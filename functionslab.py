def area(l,w):
    a = l*w
    print("Area = ", a)
    
def perimeter(l,w):
    p = 2*l + 2*w
    print("Perimeter = ", p)

def isSquare(l,w):
    if l==w:
        return True
        
    else:
        return False
    


l = float(input("Length of rectangle? "))
w = float(input("Width of rectangle? "))

x = isSquare(l,w)

area(l,w)
perimeter(l,w)
isSquare(l,w)
print("Square? ",x)

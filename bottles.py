n = int(input("How many bottles of beer on the wall? "))

if n < 0:
    print("ERROR")

for i in range(n, -1, -1):
    if i > 2:
        print(i, "bottles of beer on the wall,", i, "bottles of beer. ", end="")
        print("Take one down, pass it around,", i-1, "bottles of beer on the wall.")
    if i == 2:
        print(i, "bottles of beer on the wall,", i, "bottles of beer. ", end="")
        print("Take one down, pass it around,", i-1, "bottle of beer on the wall.")
    if i == 1:
        print(i, "bottle of beer on the wall,", i , "bottle of beer. ", end="")
        print("Take one down, pass it around,", i-1, "bottles of beer on the wall.")
    if i ==0:
        print(i, "bottles of beer on the wall,", i, "bottles of beer. ", end="")
        print("Go to the store and buy some more,", n, "bottles of beer on the wall.")

       

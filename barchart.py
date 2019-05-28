#Stephen Dojcak
#Bar Charts
#Pledge: Stephen Dojcak


def info(file):
    longest = 0
    x = open(file, "r")
    title = x.readline()
    for line in x:
        lines = line.split()
        if len(lines[0]) > longest:
            longest = len(lines[0])
    x.close
    return longest
    

def chart(file, longest):
    y = open(file, "r")
    title = y.readline()
    print(title)
    underline = "-"
    for i in range(len(title) - 1):
        underline = underline + "-"
    print(underline)
    print()
    for line in y:
        lines = line.split()
        while len(lines[0]) < longest + 1:
            lines[0] = lines[0] + " "
        count = int(lines[1])
        print(lines[0] + ("+" * count))
    y.close


    

z = input("For which file would you like to create a chart? ")

info(z)
longest = info(z)
chart(z, longest)

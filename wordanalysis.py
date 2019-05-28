#Stephen Dojcak
#WordAnalysis
#Testing Reading Difficulty
#Pledge: Stephen Dojcak

n = int(input("How many words will you enter? "))

length = 0

for i in range(1,n+1,1):
    if i == 1:
        length = length + len(input("1st word: "))
    elif i == 2:
        length = length + len(input("2nd word: "))
    elif i == 3:
        length = length + len(input("3rd word: "))
    else:
        length = length + len(input(str(i)+"th word: "))


avg = length/n
print("The average word length is", round(avg, 2))

if avg >= 6:
    print("The text is hard.")
elif avg >= 4:
    print("The text is intermediate.")
else:
    print("The text is easy.")

labs = input("Enter grades: ")
labs = labs.split(",")
print(labs)

total = 0
for lab in labs:
    total = total + int(lab)

avg = total / len(labs)

print(avg)

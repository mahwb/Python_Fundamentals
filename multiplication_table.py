string = ""
num = 0
for y in range(0,13):
    for x in range(0,13):
        num = x * y
        if x == 0 and y == 0:
            string += 'x'
        elif x == 0:
            string += str(y)
        elif y == 0:
            string += " " + str(x)
        else:
            string += " " + str(num)
    string += "\n"
print string
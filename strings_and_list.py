# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
words = words.replace('day','month')
print words

# Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
last = x[len(x)-1]
print first
print last
y = [first, last]
print y

# New List
# [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
half = x[0:len(x)/2]
y = [half]
for num in range(len(x)/2,len(x)):
    y.append(x[num])
print y
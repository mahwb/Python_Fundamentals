# Multiples
# print odd numbers from 1 to 1000
odd = []
for num in range(1,1000):
    if num % 2 != 0:
        odd.append(num)
print odd

# print all the multiples of 5 from 5 to 1,000,000
five = []
for num in range(5,1000000):
    if num % 5 == 0:
        five.append(num)
print five

# Sum
a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in range(0,len(a)):
    sum += a[num]
print sum

# Average
avg = sum / len(a)
print avg
# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number print "Foo". 
# If it is a perfect square print "Bar". If it is neither print "FooBar". Do not use the python math library for this exercise. For example, 
# if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".
def isSquare(x):
    if x == 1:
        return True
    return x**0.5 == int(x**0.5)

def isPrime(x):
    # check that number is greater that 1
    if x > 1:
        for i in range(2, x + 1):
            # check that only x and 1 can evenly divide x
            if x % i == 0 and i != x:
                return False
        return True
    else:
        return False # if number is negative

psquare = 0
prime = 0

for num in range(100,100000):
    if isSquare(num):
        psquare += 1
        print "Bar"
    elif isPrime(num):
        prime += 1
        print "Foo"
    else:
        print "FooBar"

print "Prime count: " + str(prime)
print "Perfect Square count: " + str(psquare)
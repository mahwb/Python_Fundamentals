def odd_even():
    string = ""
    for x in range(1,2001):
        string += "Number is " + str(x) + ". "
        if x % 2 == 0:
            string += "This is an even number.\n"
        else:
            string += "This is an odd number.\n"
    return string
print odd_even()

def multiply(arr, val):
    newarr = []
    for num in range(0,len(arr)):
        newarr.append(arr[num]*val)
    return newarr

a = [2,4,10,16]
b = multiply(a, 5)
print b

def layered_multiples(arr):
    # your code here
    # [6,12,15]
    new_array = []
    sub_array = []
    for num in range(0,len(arr)):
        for multiples in range(0, arr[num]):
            sub_array.append(1)
        new_array.append(sub_array)
        sub_array = []
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
# output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
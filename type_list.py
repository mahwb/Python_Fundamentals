# input
list1 = ['magical unicorns',19,'hello',98.98,'world']
# output
# "The array you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

# input
list2 = [2,3,1,7,4,12]
# output
# "The array you entered is of integer type"
# "Sum: 29"

# input
list3 = ['magical','unicorns']
# output
# "The array you entered is of string type"
# "String: magical unicorns"

def type_list(arr):
    sum = 0;
    string = ''
    result = ''

    for item in range(0,len(arr)):
        if isinstance(arr[item], str):
            string += ' ' + arr[item]
        elif isinstance(arr[item], int) or isinstance(arr[item], float):
            sum += arr[item]
    if string != '' and sum > 0:
        result += "The array you entered is of mixed type"
    if string != '' and sum == 0: 
        result += "The array you entered is of string type"
    if string == '' and sum > 0: 
        result += "The array you entered is of integer type"
    if string != '': 
        result += "\nString:" + string
    if sum > 0:
        result += "\nSum: " + str(sum) 
    print result

type_list(list1)
type_list(list2)
type_list(list3)
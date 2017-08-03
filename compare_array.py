def compare_arr(l1, l2):
    checked = False
    if l1 == l2:
        checked = True
    if checked:
        print "The lists are the same"
    else:
        print "The lists are different"

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compare_arr(list_one,list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compare_arr(list_one,list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compare_arr(list_one,list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compare_arr(list_one,list_two)
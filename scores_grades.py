# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
import random

def scores_grades():
    random_num = random.randint(0,100)
    if random_num >= 60 and random_num <= 69:
        return "Score: " + str(random_num) + "; Your grade is D"
    elif random_num >= 70 and random_num <= 79:
        return "Score: " + str(random_num) + "; Your grade is C"
    elif random_num >= 80 and random_num <= 89:
        return "Score: " + str(random_num) + "; Your grade is B"
    elif random_num >= 90 and random_num <= 100:
        return "Score: " + str(random_num) + "; Your grade is A"
    else:
        return "Score: " + str(random_num) + "; Your grade is F"

print "Scores and Grades"
for x in range(0,10):
    print scores_grades()
print "End of program. Bye!"
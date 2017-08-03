# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!
import random

def coin_tosses(num):
    heads = 0
    tails = 0
    string = "String the program...\n"
    for x in range(0, num):
        string += "Attempt #" + str(x + 1) + ": Throwing a coin... "
        random_num = round(random.random())
        if random_num == 0:
            tails += 1
            string += "It's a tail! ... "
        else:
            heads += 1
            string += "It's a head! ... "
        string += "Got " + str(heads) + " head(s) so far and " + \
            str(tails) + " tail(s) so far\n"
    string += "Ending the program, thank you!"
    return string

print coin_tosses(100)

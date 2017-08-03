def find_characters(list, char):
    new_list = []
    for word in range(0,len(list)):
        if list[word].find(char) > 0:
            new_list.append(list[word])
    print new_list

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
find_characters(word_list, char)
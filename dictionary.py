x = {"name": "Byron", "age": "28", "country of birth": "Canada", "favorite language": "Python"}

def read_dict(arr):
    # for key,val in x.iteritems():
    #     print "My", key, "is", val
    print "My name is", arr["name"]
    print "My age is", arr["age"]
    print "My country of birth is", arr["country of birth"]
    print "My favorite language is", arr["favorite language"]
read_dict(x)
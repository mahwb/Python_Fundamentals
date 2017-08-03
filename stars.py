# ****
# ******
# *
# ***
# *****
# *******
# *************************

def draw_stars(arr):
    stars=''
    for y in range(0,len(arr)):
        for x in range(0,arr[y]):
            stars += "*"
        stars+="\n"
    return stars

x = [4, 6, 1, 3, 5, 7, 25]
print draw_stars(x)


# ****
# ttt
# *
# mmmmmmm
# *****
# *******
# jjjjjjjjjjj
def draw_stars_char(arr):
    str=''
    for y in range(0,len(arr)):
        if isinstance(arr[y], int):
            for x in range(0,arr[y]):
                str += "*"
            str+="\n"
        else: 
            for x in range(0,len(arr[y])):
                str += arr[y][0].lower()
            str+="\n"
    return str

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print draw_stars_char(x)
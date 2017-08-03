name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "peacock"]

def make_dict(arr1, arr2):
  # your code here    
    if len(arr1) >= len(arr2):
        new_dict = {}
        index = 0
        while index != len(arr2):
            new_dict[arr1[index]] = arr2[index]
            index += 1
    else:
        new_dict = make_dict(arr2, arr1)
    return new_dict

print make_dict(name,favorite_animal)
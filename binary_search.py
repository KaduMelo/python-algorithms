def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        half = int((low + high)/2)

        kick = list[half]

        if kick == item:
            return half
        if kick > item:
            high = half - 1
        else:
            high = half + 1
    
    return None

binary_search([1,4,6,8,10,11], 1)
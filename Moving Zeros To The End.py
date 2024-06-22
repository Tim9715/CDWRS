def move_zeros(lst):
    null = lst.count(0)
    while null != 0:
        lst.pop(lst.index(0))
        lst.append(0)
        null -= 1
    return lst
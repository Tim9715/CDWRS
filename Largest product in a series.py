def greatest_product(st):
    min_ind, max_ind, max_pr, lena = 0, 5, 0, len(st)
    while lena != 0:
        c, b = 1, st[min_ind:max_ind]
        if len(b) == 5:
            for i in b:
                c *= int(i)
            if c > max_pr: max_pr = c
            min_ind += 1
            max_ind += 1
            lena -= 1
        else: break
    return max_pr
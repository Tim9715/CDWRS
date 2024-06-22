def valid_ISBN10(isbn): 
    a = [j for j in isbn if len(isbn) == 10 and ((isbn[0:9].isdigit() and isbn[-1] == 'X') or isbn.isdigit())]
    if len(a) == 0: return False
    if isbn.isdigit(): b = (int(a[0])*1 + int(a[1])*2 + int(a[2])*3 + int(a[3])*4 + int(a[4])*5 + int(a[5])*6 + int(a[6])*7 + int(a[7])*8 + int(a[8])*9 + int(a[9])*10) % 11
    else: b = (int(a[0])*1 + int(a[1])*2 + int(a[2])*3 + int(a[3])*4 + int(a[4])*5 + int(a[5])*6 + int(a[6])*7 + int(a[7])*8 + int(a[8])*9 + 10*10) % 11
    if b == 0: return True
    else: return False
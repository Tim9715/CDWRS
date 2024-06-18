def pig_it(text):
    a, c = text.split(' '), []
    for i in a:
        if i.isalpha():
            c.append(i[1:] + i[0] + 'ay')
        else:
            c.append(i)
    return ' '.join(c)
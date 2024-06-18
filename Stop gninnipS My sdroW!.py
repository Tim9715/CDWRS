def spin_words(sentence):
    a = ''
    for i in sentence.split():
        if len(a) == 0 and len(i) < 5:
            a += '' + i
        elif len(a) > 0 and len(i) < 5:
            a += ' ' + i
        elif len(a) == 0 and len(i) >= 5:
            a += '' + i[::-1]
        elif len(a) > 0 and len(i) >= 5:
            a += ' ' + i[::-1]
    return a
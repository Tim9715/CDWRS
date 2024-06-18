def first_non_repeating_letter(string):
    c = [i for i in string if string.lower().count(i.lower()) == 1]
    return c[0] if len(c) > 0 else ''
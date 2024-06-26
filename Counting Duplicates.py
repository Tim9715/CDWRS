def duplicate_count(text):
    counter = {}
    for elem in text.upper():
        counter[elem] = counter.get(elem, 0) + 1
    doubles = {element: count for element, count in counter.items() if count > 1}
    return len(doubles)
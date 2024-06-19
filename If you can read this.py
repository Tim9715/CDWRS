def to_nato(a):
    nato, c = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
              'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
              'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike',
              'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec',
              'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
              'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',
              'Z': 'Zulu'}, ''
    for i in a:
        if i.isalpha():
            c += nato[i.upper()] + ' '
        elif i == " ":
            pass
        else:
            c += i + ' '
    return c[:-1]
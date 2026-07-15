COLOR_TO_VALUE = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

def value(colors):

    #return int(str(COLOR_TO_VALUE[colors[0]]) + str(COLOR_TO_VALUE[colors[1]]))

    first = COLOR_TO_VALUE[colors[0]]
    second = COLOR_TO_VALUE[colors[1]]

    return first * 10 + second
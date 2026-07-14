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

def color_code(color):
    return COLOR_TO_VALUE[color]

def colors():
    return list(COLOR_TO_VALUE.keys())

    #colors_list =[]

    #for color in COLOR_TO_VALUE:
        #colors_list.append(color)

    #return colors_list
        

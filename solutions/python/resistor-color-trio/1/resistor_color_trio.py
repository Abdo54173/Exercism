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
def label(colors):

    first = str(COLOR_TO_VALUE[colors[0]])
    second = str(COLOR_TO_VALUE[colors[1]])
    no_zeros = COLOR_TO_VALUE[colors[2]]

    color_label = first + second + "0" * no_zeros

    color_label_int =int(color_label)

    if color_label_int != 0 and color_label_int % 1_000_000_000 == 0:
        return f"{color_label_int // 1_000_000_000} gigaohms"

    if color_label_int != 0 and color_label_int % 1_000_000 == 0:
        return f"{color_label_int // 1_000_000} megaohms"
    
    if color_label_int != 0 and color_label_int % 1000 == 0:
        return f"{color_label_int // 1000} kiloohms"

    return f"{color_label_int} ohms"

    
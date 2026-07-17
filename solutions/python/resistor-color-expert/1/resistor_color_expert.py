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

TOLERANCE_VALUES = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%",
}

UNITS = [
    "ohms",
    "kiloohms",
    "megaohms",
    "gigaohms",
]


def resistor_label(colors):

    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        digits = (
            str(COLOR_TO_VALUE[colors[0]])
            + str(COLOR_TO_VALUE[colors[1]])
        )
        multiplier = COLOR_TO_VALUE[colors[2]]
        tolerance = TOLERANCE_VALUES[colors[3]]

    elif len(colors) == 5:
        digits = (
            str(COLOR_TO_VALUE[colors[0]])
            + str(COLOR_TO_VALUE[colors[1]])
            + str(COLOR_TO_VALUE[colors[2]])
        )
        multiplier = COLOR_TO_VALUE[colors[3]]
        tolerance = TOLERANCE_VALUES[colors[4]]

    resistance = int(digits + "0" * multiplier)

    unit_index = 0

    while resistance >= 1000 and unit_index < len(UNITS) - 1:
        resistance /= 1000
        unit_index += 1

    return f"{resistance:g} {UNITS[unit_index]} {tolerance}"
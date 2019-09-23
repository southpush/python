color_dict = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
}


def value(colors):
    return int(''.join(str(color_dict[i]) for i in colors[0: 2]))

# create colored text
def colortext(txtstyle:int, txtcolor: int, backcolor: int, text: str):
    return f'\033[{txtstyle};{txtcolor};{backcolor}m {text} \033[0;0m'

# create colored text with 265 color scheme using ansi (txtcolors = [txt, colorcode])
def ansicolortext(backcolor: int, *txtcolors: list):
    __a = f'\033[48;5;{backcolor}m'
    for i in txtcolors:
        __a = f"{__a}\033[38;5;{i[1]}m{i[0]} "
    __a = f"{__a}\033[0;0m"
    return __a

print(ansicolortext(255, ["hello, world!", 000]))
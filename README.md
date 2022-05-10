# Python-Easy-Colored-Text
## A Python (3.X) module for easily creating colored text without Colorama (another Python module)

### Variables:
- None

### Functions:
- `colortext(txtstyle:int, txtcolor: int, backcolor: int, text: str)`:
  </br>Arguments:
  - txtstyle: integer from 0 - 5.
    - 0: none
    - 1: **bold**
    - 2: light
    - 3: *italicised*
    - 4: underlined
    - 5: blink
  - txtcolor: integer from 30 - 37. (list [here](thatn00b123/Python-Easy-Colored-Text))
  - backcolor integer from 40 - 47 (list also [here](thatn00b123/Python-Easy-Colored-Text))
  - txt: string that will be colored and returned

- `ansicolortext(backcolor: int, *txtcolors: list)`:
  </br>RUN `$ echo $TERM` IF YOU ARE ON LINUX OR A LINUX BASED OS!
  </br>Arguments:
  - backcolor: integer. (list of color codes [here](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797))
  - txtcolors: n number of lists that are 2 indexes long. Index 0 is the string of text, and index 1 is the color code (found above)

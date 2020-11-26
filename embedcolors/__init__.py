import random
__version__ = "0.1.1"
__author__ = 'Lukas Canter'
__credits__ = 'Author'

red = 0xFF1A1A
orange = 0xFF751A
yellow = 0xFFF81A
lime = 0x4AFF1A
green = 0x319718
cyan = 0x23FFDA
blue = 0x23B0FF
purple = 0x2328FF
magenta = 0xC523FF
pink = 0xFF64CF
black = 0x000000


def rand():
    randomcolorchoice = random.randint(0, 0xffffff)
    return randomcolorchoice


def choice(colorone, colortwo):
    randomcolorchoice = random.choice([colortwo, colorone])
    return randomcolorchoice

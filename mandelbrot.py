import numpy as np
import os
from getkey import getkey, keys

# gradient = " ░▒▓█ ░▒▓█ ░▒▓█ ░▒▓█"
# gradient = " ·-+=*≡#@"
gradient = " ·-+=*≡# @"
# gradient = " █"*30
# gradient = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{\C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
# gradient = " ·-+=*≡#@"*20
# gradient = " ▪️"


def mandelbrot(c, depth=100):
    z = 0
    i = 0
    while i < depth:
        z = pow(z, 2) + c
        if abs(z) > 10000:
            return i
        i += 1
    return i


def mandelbrot_pretty(c, depth=100):
    jump = depth / (len(gradient))
    z = 0
    i = 0
    while i < depth:
        z = pow(z, 2) + c
        if abs(z) > 10000:  # inf
            # transformed using sigmoid function
            val = int(1/((1/depth)+(1.1**-i)))
            return gradient[int(val // jump)]
        i += 1
    val = int(1/((1/depth)+(1.1**-i)))
    # print(f'max value = {depth}\n{jump=}\n{len(gradient)=}\n{val=}\n{(val // jump)=}')
    return gradient[int(val // jump)]


def make_mandel(rows, cols, zoom=1, x=0, y=0, depth=100):

    x_left = -2.1 / zoom + x
    x_right = 0.6 / zoom + x
    y_top = 1.2 / zoom + y
    y_bot = -1.2 / zoom + y

    real_part = np.linspace(x_left, x_right, rows)
    imag_part = np.linspace(y_top, y_bot, cols)
    real_mesh, imag_mesh = np.meshgrid(real_part, imag_part)
    complex_array = real_mesh + 1j * imag_mesh
    mandel = vectorized_mandelbrot_pretty(complex_array)
    for row in mandel:
        print(''.join(row))


def main():
    zoom = 1
    x = 0
    y = 0
    while True:
        cols, rows = os.get_terminal_size()
        make_mandel(cols, rows, depth=100, zoom=zoom, x=x, y=y)
        user = getkey()
        if user == "a":
            x -= (1/zoom)
        elif user == "d":
            x += (1/zoom)
        elif user == "s":
            y -= (1/zoom)
        elif user == "w":
            y += (1/zoom)
        elif user == "p":
            zoom *= 2
        elif user == "l":
            zoom *= .5


vectorized_mandelbrot_pretty = np.vectorize(mandelbrot_pretty)
if __name__ == '__main__':
    main()

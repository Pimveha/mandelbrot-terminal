import numpy as np
from time import sleep
import os

# gradient = " ░▒▓█"
gradient = " ·-+=*≡#@"
# gradient = " ·-+=*≡#@ ·-+=*≡#@ ·-+=*≡#@ ·-+=*≡#@ ·-+=*≡#@ ·-+=*≡#@ ·-+=*≡#@ ·-+=*≡#@ ·-+=*≡#@"*2
# gradient = " ▪️"


def mandelbrot(c, depth=100):
    z = 0
    i = 0
    while i < depth:
        z = pow(z, 2) + c
        # z = z**2 + c
        if abs(z) > 10000:
            return i
        i += 1
    return i


def mandelbrot_pretty(c, depth=100):
    jump = depth // (len(gradient)-1)
    # jump = depth // (len(gradient)-(len(gradient)//2))
    # jump = depth // (len(gradient)-(len(gradient)//5))
    z = 0
    i = 0
    while i < depth:
        z = pow(z, 2) + c
        if abs(z) > 10000:
            # val = int(1/((1/len(gradient))+(2**-i)))
            val = int(1/((1/depth)+(1.1**-i)))
            # val = int(1/((1/depth)+(1.3**-i)))
            # print(val)
            return gradient[val // jump]
        i += 1
    # val = int(1/((1/depth)+(1.3**-i)))
    val = int(1/((1/depth)+(1.1**-i)))
    # print(val)
    return gradient[val // jump]


def transform(x):
    return 1/((1/len(gradient))+(2**-x))


def terminal_mandel(x_lower, x_upper, step, depth=100):
    real_part = np.linspace(-2, 0.6, 100)
    imag_part = np.linspace(-1.2, 1.2, 100)
    real_mesh, imag_mesh = np.meshgrid(real_part, imag_part)
    complex_array = real_mesh + 1j * imag_mesh
    # print(complex_array)
    jump = depth // (len(gradient)-1)
    for row in complex_array:
        x_arr = []
        for elem in row:
            x_arr.append(gradient[(mandelbrot(elem) // jump)]*2)
        print("".join(x_arr))

    # print("".join(x_arr))

    # for map(lambda x: x/10.0, range(5, 50, 15))


def make_mandel(rows, cols, zoom=1, x=0, y=0, depth=100):

    x_left = -2.1 / zoom + x
    x_right = 0.6 / zoom + x
    y_top = 1.2 / zoom + y
    y_bot = -1.2 / zoom + y

    real_part = np.linspace(x_left, x_right, rows)
    imag_part = np.linspace(y_top, y_bot, cols)
    real_mesh, imag_mesh = np.meshgrid(real_part, imag_part)
    complex_array = real_mesh + 1j * imag_mesh
    jump = depth // (len(gradient)-1)
    mandel = vectorized_mandelbrot_pretty(complex_array)
    for row in mandel:
        print(''.join(row))


def main():
    # cols, rows = os.get_terminal_size()
    # center_x, center_y = rows//2, cols//2

    zoom = 1
    x = 0
    y = 0
    while True:
        cols, rows = os.get_terminal_size()
        make_mandel(cols, rows, depth=100, zoom=zoom, x=x, y=y)
        user = input()
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

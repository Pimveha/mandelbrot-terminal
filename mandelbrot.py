import numpy as np
from time import sleep
import os

# gradient = " ░▒▓█"
gradient = " ·-+=*≡#@"


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


def make_mandel(rows, cols, depth=100):
    real_part = np.linspace(-2, 0.6, rows)
    imag_part = np.linspace(-1.2, 1.2, cols)
    real_mesh, imag_mesh = np.meshgrid(real_part, imag_part)
    complex_array = real_mesh + 1j * imag_mesh
    jump = depth // (len(gradient)-1)
    for row in enumerate(complex_array):
        x_arr = []
        for elem in enumerate(row):
            x_arr.append(gradient[(mandelbrot(elem) // jump)])
            # gradient[(mandelbrot(elem) // jump)]
        print("".join(x_arr))


def main():
    # cols, rows = os.get_terminal_size()
    # center_x, center_y = rows//2, cols//2
    while True:
        cols, rows = os.get_terminal_size()
        make_mandel(cols, rows, depth=100)
        sleep(10)


if __name__ == '__main__':
    main()

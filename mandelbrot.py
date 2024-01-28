import numpy as np

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


def main():
    # print(mandelbrot(-1+2j, 100))
    # print(mandelbrot(.1+.1j, 100))

    terminal_mandel(-2.4, 2, 0.1)


if __name__ == '__main__':
    main()

import numpy as np

# gradient = " ░▒▓█"
gradient = " ·-+=*≡#@"


def mandelbrot(c, depth=1000):
    z = 0
    i = 0
    while i < depth:
        z = z**2 + c
        # print(z)
        if z > 10000:
            return i
        i += 1
    return i


def terminal_mandel(x_lower, x_upper, step):
    arr = np.arange(x_lower, x_upper, step, dtype=np.float32)
    for x in arr:
        print(mandelbrot(x))

    # for map(lambda x: x/10.0, range(5, 50, 15))


def main():
    # print(mandelbrot(-1, 100))
    terminal_mandel(-2.4, 2, 0.1)


if __name__ == '__main__':
    main()

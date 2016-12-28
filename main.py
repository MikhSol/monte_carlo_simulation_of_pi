from random import random
import time
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def estimate_pi(trials):
    start = time.process_time()
    count = 0
    for _ in range(trials + 1):
        x, y = random(), random()
        if x * x + y * y <= 1:
            count += 1
    logger.info("estimate pi with " + str(trials) +
                " trials processing time: " +
                str(time.process_time() - start))
    return 4 * count / trials


def generate_sample(trials):
    in_x, in_y, out_x, out_y = [], [], [], []
    for _ in range(trials + 1):
        x, y = random(), random()
        if x * x + y * y <= 1:
            in_x.append(x), in_y.append(y)
        else:
            out_x.append(x), out_y.append(y)
    return in_x, in_y, out_x, out_y


def draw_estimation(trials):
    in_x, in_y, out_x, out_y = generate_sample(trials)
    plt.plot(in_x, in_y, 'x', color='r')
    plt.plot(out_x, out_y, 'o', color='b')
    plt.show()


def main():
    print(estimate_pi(10000000))
    draw_estimation(10000)


if __name__ == '__main__':
    main()
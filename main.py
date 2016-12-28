from random import random
import time
import logging

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


def main():
    print(estimate_pi(10000000))


if __name__ == '__main__':
    main()
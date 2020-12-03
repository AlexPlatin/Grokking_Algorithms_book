def recursive_factorial(x: int) -> int:
    if x == 1:
        return 1
    else:
        return x * recursive_factorial(x - 1)


def loop_factorial(x: int) -> int:
    if x == 1:
        return 1
    else:
        for i in range(x - 1, 0, -1):
            x *= i
        return x


if __name__ == '__main__':
    import time
    start = time.perf_counter()
    print(recursive_factorial(100))
    print("Recursive - {} s".format(time.perf_counter() - start))
    start = time.perf_counter()
    print(loop_factorial(100))
    print("Loop - {} s".format(time.perf_counter() - start))

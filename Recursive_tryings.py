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


def recursive_sum(list_values: list) -> int:
    if len(list_values) == 0:
        return 0
    else:
        return list_values.pop(0) + recursive_sum(list_values)


def recursive_max(list_values: list) -> int:
    if len(list_values) == 2:
        return list_values[0] if list_values[0] > list_values[1] else list_values[1]
    submax = recursive_max(list_values[1:])
    return list_values[0] if list_values[0] > submax else submax


if __name__ == '__main__':
    print(recursive_sum([2, 20, 3, 4]))

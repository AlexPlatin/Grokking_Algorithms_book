def find_smallest_number(list_values: list) -> int:
    """Get and return index of minimal value of input list"""
    smallest_value = list_values[0]
    smallest_index = 0
    for num in range(1, len(list_values)):
        if list_values[num] < smallest_value:
            smallest_value = list_values[num]
            smallest_index = num
    return smallest_index


def selection_sort(list_values: list) -> list:
    """Sort input list values"""
    end_list = list()
    for _ in range(len(list_values)):
        index_min = find_smallest_number(list_values)
        end_list.append(list_values.pop(index_min))
    return end_list


if __name__ == "__main__":
    print(selection_sort([4, 52, 3, 45, 7, 100, 12, 1]))
    print(selection_sort([4, 52, 3, 45, 7, 100, 12, 1]))

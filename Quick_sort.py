def quicksort(list_of_values: list) -> list:
    if len(list_of_values) < 2:
        return list_of_values
    pivot_elem = list_of_values[0]
    less_part = [i for i in list_of_values[1:] if i <= pivot_elem]
    greater_part = [i for i in list_of_values[1:] if i > pivot_elem]
    return quicksort(less_part) + [pivot_elem] + quicksort(greater_part)

print(quicksort([1, 2, 5, 4, 3, 5, 6]))
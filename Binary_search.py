def binary_search(values: list, item: int):
    """Binary search in sorted list"""
    low_index = 0
    high_index = len(values) - 1
    while low_index <= high_index:
        mid = (low_index + high_index) // 2
        mid_item = values[mid]
        if mid_item == item:
            return mid
        elif mid_item > item:
            high_index = mid - 1
        elif mid_item < item:
            low_index = mid + 1
    return None


def recursive_binary_search(values, item, low, high):
    """Recursive binary search"""
    if low <= high:
        mid = (low + high) // 2
        mid_val = values[mid]
        if mid_val == item:
            return mid
        elif mid_val > item:
            return recursive_binary_search(values, item, low, mid - 1)
        elif mid_val < item:
            return recursive_binary_search(values, item, mid + 1, high)
    else:
        return None


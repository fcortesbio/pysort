def bubble_sort(data: iter, mode: str = "nd") -> list:
    """
    Sorts a list using the bubble sort algorithm.

    Args:
        data: The list to be sorted.
        mode: Optional. The sorting order.
              "nd": Sorts in non-decreasing (ascending) order (default).
              "ni": Sorts in non-increasing (descending) order.

    Returns:
        The sorted list.

    Raises:
        ValueError: If an invalid mode is provided.
    """
    if mode not in ("nd", "ni"):
        raise ValueError("Invalid mode. Choose 'nd' or 'ni'.")
    data = list(data) # ensures original list remains unchanged
    unsorted = (lambda x, y: x > y) if mode == "nd" else (lambda x, y: x < y)

    swaps = True
    while swaps:
        swaps = False
        for i in range(len(data)-1):
            if unsorted(data[i], data[i+1]):
                data[i], data[i + 1] = data[i + 1], data[i]
                swaps = True
    return data

if __name__ == "__main__":
    example_list = [8, 10, 6, 2, 4]
    print("Example list: ", example_list)
    sorted_list = bubble_sort(example_list)
    print("Sorted list (non-decreasing): ", sorted_list)
    sorted_list_backwards = bubble_sort(example_list, "ni")
    print("Sorted list (non-increasing): ", sorted_list_backwards)
    name = "Scarlet"
    print("Scarlet, but sorted: ", bubble_sort(name))
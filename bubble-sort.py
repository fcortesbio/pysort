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
    data = list(data) # ensures original list remains unchanged
    
    if mode not in ("nd", "ni"):
        raise ValueError("Mode must be 'nd' for non-decreasing or 'ni' for non-increasing")
    
    swap_needed = (lambda x, y: x > y) if mode == "nd" else (lambda x, y: x < y)

    swaps = True
    while swaps:
        swaps = False
        for i in range(len(data)-1):
            if swap_needed(data[i], data[i+1]):
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
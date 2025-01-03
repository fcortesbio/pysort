def select_sort(data: iter, mode: str = "nd") -> list:
    """
    Sorts a list using the selection sort algorithm.

    Args:
        data (list): The list to sort.
        mode (str): Sorting mode, "nd" for non-decreasing (ascending),
                    "ni" for non-increasing (descending).
    Returns:
        list: The sorted list.

    Raises:
        ValueError: If an invalid mode is provided.
    """
    data = list(data)  # Make a copy to avoid mutating the input

    if mode not in ("nd", "ni"):
        raise ValueError("Mode must be 'nd' for non-decreasing or 'ni' for non-increasing")

    swap_needed = (lambda current, value: current > value) if mode == "nd" else (lambda current, value: current < value)

    for i in range(len(data)):
        first_index = i
        for j in range(i + 1, len(data)):
            if swap_needed(data[first_index], data[j]):
                first_index = j

        if first_index != i:
            data[i], data[first_index] = data[first_index], data[i]  # Swap local minimum with first unsorted item

    return data

if __name__ == "__main__":
    example_list = [8, 10, 6, 2, 4, 12]
    print("Example list: ", example_list)
    sorted_list = select_sort(example_list)
    print("Sorted list (non-decreasing): ", sorted_list)
    sorted_list_backwards = select_sort(example_list, "ni")
    print("Sorted list (non-increasing): ", sorted_list_backwards)
    name = "Scarlet"
    print("Scarlet, but sorted: ", select_sort(name))

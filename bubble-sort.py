# Sorting elements of a list in a non-decreasing order;
# Take the first and second elements and compare them; 
# if we determine that they're in the wrong order (i.e., the first is greater than the second), we'll swap them round; 
# if the order is valid, we'll do nothing. 

def bubble_sort(data: list)-> list:
    """Sorts a list in a non-decreasing order using the bubble sort algorithm.
    Args: 
        data: The list to be sorted
    Returns: 
        The sorted list.
    """
    swaps = 1
    while swaps > 0:
        swaps = 0 
        for i, item in enumerate(data[:-1]):
            if item > data[i+1]:
                swaps += 1
                data[i], data[i+1] = data[i+1], data[i];
    return data

if __name__ == "__main__":
    example_list = [8, 10, 6, 2]
    print("Example list: ", example_list)
    sorted_list = bubble_sort(example_list)
    print("Sorted list: ", sorted_list)
# Sorting elements of a list in a non-decreasing order;
# Take the first and second elements and compare them; 
# if we determine that they're in the wrong order (i.e., the first is greater than the second), we'll swap them round; 
# if the order is valid, we'll do nothing. 

def bubble_sort(list_: list)-> list:
    """Sorts a list in a non-decreasing order using the bubble sort algorithm.
    Args: 
        list_: The list to be sorted
    Returns: 
        The sorted list.
    """
    swaps = 1
    while swaps > 0:
        swaps = 0 
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                swaps += 1
                list[i], list[i+1] = list[i+1], list[i];
    return list

example_list = [8, 10, 6, 2]
print("Example list: ", example_list)
sorted_list = bubble_sort(example_list)
print("Sorted list: ", sorted_list)
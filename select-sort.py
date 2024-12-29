# find the smallest element
# exchange with the first unordered element
# repeat until the full list is sorted

def select_sort(data: list, mode: str = "nd")-> list:
    """
    Sorts a list using the selection sort algorithm.    
    """
    data = list(data)
    
    outdated = (lambda current, value: current > value) if mode == "nd" else (lambda current, value: current < value)

    if mode not in ("nd", "ni"):
        raise ValueError
    
    print("Original list: ", data)
    print("Non-decreasing sort" if mode == "nd" else "Non-increasing")

    for i in data:
        # sub list from data[i] to data[N]
        subdata = data[i:]
        min_index = i
        print("subdata evaluated: ", subdata)
        upd = 0

        # find the local min value in subdata
        for j in range(len(subdata)):
            print("Current min index: ", min_index,"- Current min value: ", subdata[min_index])
            
            if outdated(subdata[min_index], subdata[j]): 
                min_index = i + j
                print("Min index has changed")
                upd += 1
        # if minimum is not the first value; swap the local minimum with the first unordered element
        if upd > 0:
            data[i], data[min_index] = data[min_index], data[i]  # Swap in data
            print("Swapped local minimum with first unsorted element")
    
    return data

if __name__ == "__main__":
    example_list = [8, 10, 6, 2, 4]
    print("Example list: ", example_list)
    sorted_list = select_sort(example_list)
    print("Sorted list (non-decreasing): ", sorted_list)
    sorted_list_backwards = select_sort(example_list, "ni")
    print("Sorted list (non-increasing): ", sorted_list_backwards)


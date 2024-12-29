def select_sort(data: list, mode: str = "nd")-> list:
    return data

if __name__ == "__main__":
    example_list = [8, 10, 6, 2, 4]
    print("Example list: ", example_list)
    sorted_list = select_sort(example_list)
    print("Sorted list (non-decreasing): ", sorted_list)
    sorted_list_backwards = select_sort(example_list, "ni")
    print("Sorted list (non-increasing): ", sorted_list_backwards)


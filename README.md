# My Python Collection of Sorting Algorithms

This repository contains a collection of sorting algorithms implemented in Python. This project was created as practice for the TalentoTech bootcamp.

## Sorting Algorithms

### 1. Simple Sorts (Generally O(n^2) time complexity)

* **Bubble Sort:**  Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 
    * Completed: [bubble-sort.py](bubble-sort.py)
* **Selection Sort:**  Finds the smallest (or largest) element in the unsorted portion of the list and swaps it with the first unsorted element. Repeats this process until the entire list is sorted.
    * Completed: [select-sort.py](select-sort.py)
* **Insertion Sort:** Builds a sorted array one element at a time by shifting elements as needed. Efficient for small datasets or nearly sorted data.
    * To be implemented
* **Shell Sort:** A generalization of Insertion Sort that improves efficiency by comparing elements further apart.
    * To be implemented

### 2. Efficient Sorts (Generally O(n log n) time complexity)

* **Merge Sort:** Divides the list into halves, recursively sorts them, and then merges the sorted halves. Stable and efficient, but often requires extra space.
    * To be implemented
* **Quick Sort:** Partitions the list around a "pivot" element and recursively sorts the sublists. Generally very fast, but performance can degrade to O(n^2) in worst-case scenarios.
    * To be implemented
* **Heap Sort:** Uses a heap data structure to efficiently sort the elements. In-place and guarantees O(n log n) time complexity.
    * To be implemented

### 3. Specialized Sorts

* **Counting Sort:** Sorts integers with a known range by counting the occurrences of each value. Efficient for specific types of data.
    * To be implemented
* **Radix Sort:** Sorts integers digit by digit. Can be very efficient for integers with a fixed number of digits.
    * To be implemented
* **Bucket Sort:** Distributes elements into "buckets" and then sorts the buckets individually. Efficient when data is uniformly distributed.
    * To be implemented

## How to Use

1. Clone the repository: `git clone https://github.com/your-username/sorting-algorithms.git`
2. Navigate to the directory: `cd sorting-algorithms`
3. Run any of the Python files to see the sorting algorithms in action (e.g., `python bubble-sort.py`)

## Contributing

Contributions are welcome! If you'd like to add a new sorting algorithm or improve an existing one, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
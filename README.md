# My Python collection of sorting algorithms
Made as a practice project on Algorithms for TalentoTech bootcamp

## Sorting algorithms finished or to be included:

### 1. Simple Sorts (Generally O(n^2) time complexity)

**Bubble Sort**: description
*Completed: bubble-sort.py*

**Selection Sort**: description 

Completed: select-sort.py

**Insertion Sort**: Builds a sorted array one element at a time by shifting elements as needed. Efficient for small datasets or nearly sorted data.   

**Shell Sort**: A generalization of Insertion Sort that improves efficiency by comparing elements further apart.   


### 2. Efficient Sorts (Generally O(n log n) time complexity)

**Merge Sort**: Divides the list into halves, recursively sorts them, and then merges the sorted halves. Stable and efficient, but often requires extra space.   

**Quick Sort**: Partitions the list around a "pivot" element and recursively sorts the sublists. Generally very fast, but performance can degrade to O(n^2) in worst-case scenarios.   

**Heap Sort**: Uses a heap data structure to efficiently sort the elements. In-place and guarantees O(n log n) time complexity.   

### 3. Specialized Sorts

**Counting Sort**: Sorts integers with a known range by counting the occurrences of each value. Efficient for specific types of data.   

**Radix Sort**: Sorts integers digit by digit. Can be very efficient for integers with a fixed number of digits.   

**Bucket Sort**: Distributes elements into "buckets" and then sorts the buckets individually. Efficient when data is uniformly distributed.
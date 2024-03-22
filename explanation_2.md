Time Complexity:

The algorithm uses a modified binary search approach to find the target element in the rotated sorted array.
In each iteration of the binary search, the search space is divided in half, reducing the search space significantly.
Hence, the time complexity of the algorithm is O(log n), where n is the number of elements in the input array.

Space Complexity:

The space complexity of the algorithm is O(1), meaning it uses constant space regardless of the size of the input array.
The algorithm only uses a constant amount of extra space for variables such as start, end, and mid.

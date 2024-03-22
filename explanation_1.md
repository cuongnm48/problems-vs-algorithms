Time Complexity:
The time complexity of the sqrt function is O(log(n)), where n is the input number.
This efficiency arises from the binary search algorithm employed in the function.
In each iteration of the binary search, the search interval is halved, leading to a logarithmic time complexity. Even for very large numbers, the number of iterations required to find the floor square root remains relatively low due to the logarithmic nature of the search.
Therefore, the function can efficiently find the square root of large integers with a time complexity that grows logarithmically with the magnitude of the input.

Space Complexity:
The space complexity of the sqrt function is O(1), meaning it uses constant space regardless of the input size.
The function does not utilize any data structures whose size scales with the input. It only maintains a few integer variables (start, end, mid, mid_squared, and floor_sqrt) throughout its execution, which do not depend on the size of the input.

Time Complexity:

- Divide Step: The input array is divided into two halves in each recursive call. This operation has a time complexity of O(1).
- Merge Step: Merging two sorted subarrays takes linear time proportional to the size of both arrays being merged. In the worst-case scenario, it takes O(n) time, where n is the size of the original array.
- Recursion: The merge sort algorithm divides the input array recursively until each subarray has only one element. This process requires log(n) levels of recursion, where n is the size of the input array.
- Overall: The time complexity of merge sort is O(n log(n)), where n is the size of the input array. This is because the divide step happens log(n) times, and the merge step takes O(n) time.

Space Complexity:

- Divide and Conquer: During the divide step, the input array is divided into smaller subarrays. However, this operation doesn't require additional space as it's done in place.
- Recursion Stack: The recursion stack keeps track of function calls during the recursive process. In the worst-case scenario, the maximum depth of recursion is log(n), where n is the size of the input array.
- Temporary Arrays: During the merge step, temporary arrays are created to hold the merged elements. The size of these temporary arrays is proportional to the size of the input array.
- Overall: The space complexity of merge sort is O(n) due to the space required for the recursion stack and temporary arrays.

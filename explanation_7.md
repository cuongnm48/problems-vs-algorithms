Time Complexity:

- Insertion (add_handler): Time complexity: O(n), where n is the number of parts in the path. During insertion, we traverse through the Trie from the root to the leaf node corresponding to the path. This traversal takes linear time relative to the number of parts in the path.
- Lookup (lookup): Time complexity: O(n), where n is the number of parts in the path. Similar to insertion, lookup also involves traversing the Trie from the root to the leaf node corresponding to the path. The time taken is linear relative to the number of parts in the path.

Space Complexity:

- RouteTrie: Space complexity: O(m * k), where m is the maximum number of parts in a path and k is the number of unique parts in all paths. The RouteTrie consists of nodes, each representing a part of the path. The number of nodes created is proportional to the number of unique parts in all paths. The maximum depth of the Trie is limited by the length of the longest path, which contributes to the space complexity.
- Router: Space complexity: O(1) for Router initialization and O(m) for each additional handler added, where m is the number of parts in the path. The Router class mainly holds a single instance of RouteTrie. Initializing the Router incurs constant space. Each additional handler added consumes space linearly relative to the number of parts in the path.

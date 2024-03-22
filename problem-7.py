class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode()
        self.root.handler = handler

    def insert(self, path_parts, handler):
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]
        current_node.handler = handler

    def find(self, path_parts):
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]
        return current_node.handler


class RouteTrieNode:
    def __init__(self):
        self.handler = None
        self.children = {}


class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.route = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.route.insert(path_parts, handler)

    def lookup(self, path):
        if not path or path == '/':
            return self.route.root.handler

        path_parts = self.split_path(path)
        handler = self.route.find(path_parts)

        if handler:
            return handler
        elif self.not_found_handler:
            return self.not_found_handler
        else:
            return None

    def split_path(self, path):
        return [part for part in path.split('/') if part]


# Test cases
# router = Router("root handler", "not found handler")
# router.add_handler("/home/about", "about handler")

# print(router.lookup("/"))  # should print 'root handler'
# print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
# print(router.lookup("/home/about"))  # should print 'about handler'
# print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
# print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one

router = Router("root handler", "not found handler")
router.add_handler("/blog", "blog handler")
router.add_handler("/blog/2020", "2020 blog handler")
router.add_handler("/blog/2020/03", "March 2020 blog handler")

# Test cases
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/blog"))  # should print 'blog handler'
print(router.lookup("/blog/2020"))  # should print '2020 blog handler'
print(router.lookup("/blog/2020/03"))  # should print 'March 2020 blog handler'
print(router.lookup("/missing"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/blog/"))  # should print 'blog handler' or None if you did not handle trailing slashes
print(router.lookup(""))  # should print 'root handler'
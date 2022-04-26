# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        index = 0

        while index <= len(paths) - 1:
            path = paths[index]

            if path not in node.children:
                node.insert(path)

            node = node.children[path]
            index += 1
    
        node.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        index = 0

        while index <= len(paths) - 1:
            path = paths[index]

            if path not in node.children:
                return None

            node = node.children[path]
            index += 1

        return node.handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie()
        self.add_handler("/", root_handler)

        self.not_found_handler = not_found_handler

    def add_handler(self, path_string, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        if not isinstance(path_string, str):
            print(f"TypeError: Expected <class str> got {type(path_string)}")
            return

        paths = self.split_path(path_string)
        self.route_trie.insert(paths, handler)

    def lookup(self, path_string):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        paths = self.split_path(path_string)
        response = self.route_trie.find(paths)

        if response is None:
            return self.not_found_handler
        
        return response

    def split_path(self, path_string):
        paths = [path for path in path_string.split("/") if path != ""]
        paths.insert(0, "/")
        return paths

        

router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler") 


print(router.lookup("/"))
# should print 'root handler'

print(router.lookup("/home")) 
# should print 'not found handler'

print(router.lookup("/home/about"))
 # should print 'about handler'

print(router.lookup("/home/about/"))
# should print 'about handler'

print(router.lookup("/home/about/me")) 
# should print 'not found handler'

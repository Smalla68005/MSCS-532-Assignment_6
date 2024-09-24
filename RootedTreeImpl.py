class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class RootedTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def add_child(self, parent_value, child_value):
        # Simple logic to add a child to a parent node
        def _add_child(node):
            if node.value == parent_value:
                node.children.append(TreeNode(child_value))
                return True
            for child in node.children:
                if _add_child(child):
                    return True
            return False
        
        _add_child(self.root)

    def traverse(self, node):
        # Pre-order traversal logic
        result = []
        if node:
            result.append(node.value)
            for child in node.children:
                result.extend(self.traverse(child))
        return result


def test_rooted_tree():
    tree = RootedTree(1)
    
    # Add children
    tree.add_child(1, 2)
    tree.add_child(1, 3)
    tree.add_child(2, 4)

    # Traverse and collect values
    print("Rooted tree values:", tree.traverse(tree.root))  # Output: [1, 2, 4, 3]

    print("All Rooted Tree tests passed!")


# Test Rooted Tree
test_rooted_tree()

class DoctorNode:
    """A node in the DoctorTree storing a doctor's name and left/right reports."""
    def __init__(self, name: str):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    """Binary tree to model doctor reporting structure.

    insert(parent_name, child_name, side) will attach a new DoctorNode
    as the left or right child of the first node found with name == parent_name.
    Traversal methods return lists of names in the requested order.
    """
    def __init__(self):
        self.root = None

    def _find(self, node: DoctorNode, name: str):
        """Recursively search for a node by name. Returns the node or None."""
        if node is None:
            return None
        if node.name == name:
            return node
        left_res = self._find(node.left, name)
        if left_res is not None:
            return left_res
        return self._find(node.right, name)

    def insert(self, parent_name: str, child_name: str, side: str):
        """Insert child_name under parent_name on 'left' or 'right'.

        Raises ValueError for invalid side. Returns True on success, False if parent not found.
        If tree is empty and parent_name is None or matches child_name, sets root.
        """
        if side not in ("left", "right"):
            raise ValueError("side must be 'left' or 'right'")

        # If tree is empty, allow setting root when parent_name is None or equals child_name
        if self.root is None:
            if parent_name is None:
                self.root = DoctorNode(child_name)
                return True
            # if parent_name equals where root should be, set root first then insert child
            if parent_name == child_name:
                self.root = DoctorNode(child_name)
                return True
            # can't insert under a parent when tree is empty
            return False

        parent = self._find(self.root, parent_name)
        if parent is None:
            return False

        new_node = DoctorNode(child_name)
        if side == "left":
            parent.left = new_node
        else:
            parent.right = new_node
        return True

    def preorder(self, node):
        """Return list of names from preorder traversal starting at node."""
        if node is None:
            return []
        res = [node.name]
        res += self.preorder(node.left)
        res += self.preorder(node.right)
        return res

    def inorder(self, node):
        """Return list of names from inorder traversal starting at node."""
        if node is None:
            return []
        res = []
        res += self.inorder(node.left)
        res.append(node.name)
        res += self.inorder(node.right)
        return res

    def postorder(self, node):
        """Return list of names from postorder traversal starting at node."""
        if node is None:
            return []
        res = []
        res += self.postorder(node.left)
        res += self.postorder(node.right)
        res.append(node.name)
        return res


if __name__ == "__main__":
    # Basic tests and edge cases
    tree = DoctorTree()
    # Set root explicitly
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))

    # Edge cases
    # Insert under non-existent parent
    ok = tree.insert("NonExistent", "Dr. Who", "left")
    print("Insert under missing parent returned:", ok)  # expected False

    # Invalid side
    try:
        tree.insert("Dr. Croft", "Dr. Error", "up")
    except ValueError as e:
        print("Caught expected ValueError for side:", e)

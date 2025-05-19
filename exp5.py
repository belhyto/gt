class GameTreeNode:
    def __init__(self, state, value=None):
        self.state = state  # Represents the game state
        self.value = value  # Evaluation value (useful for AI)
        self.children = []  # List of child nodes

    def add_child(self, child_node):
        """Adds a child node to the current node."""
        self.children.append(child_node)

    def display(self, level=0):
        """Recursively displays the tree structure."""
        print(" " * (level * 4) + f"State: {self.state}, Value: {self.value}")
        for child in self.children:
            child.display(level + 1)

# Example: Creating a simple game tree
if __name__ == "__main__":
    root = GameTreeNode("Start")
    node1 = GameTreeNode("Move 1")
    node2 = GameTreeNode("Move 2")
    node1_1 = GameTreeNode("Move 1-1", value=10)
    node1_2 = GameTreeNode("Move 1-2", value=-5)
    node2_1 = GameTreeNode("Move 2-1", value=7)

    root.add_child(node1)
    root.add_child(node2)
    node1.add_child(node1_1)
    node1.add_child(node1_2)
    node2.add_child(node2_1)

    # Display the tree
    root.display()

class Node:
    def __init__(self, point, left_child, right_child):
        self.point = point
        self.left_child = left_child
        self.right_child = right_child



def print_preorder(node):
    """
    Prints the KD-Tree in pre-order.
    
    Parameters:
    - node: The current node being visited.
    """
    if node:
        # Visit the current node
        print(node.point)
        
        # Visit the left subtree
        print_preorder(node.left_child)
        
        # Visit the right subtree
        print_preorder(node.right_child)


def kd_tree(point_list, depth=0, start=0, end=None):
    """
    Recursively constructs a KD-Tree from a list of k-dimensional points.
    
    Parameters:
    - point_list: List of k-dimensional points.
    - depth: Current depth of recursion.
    - start: Starting index for the current subset of points.
    - end: Ending index for the current subset of points.
    
    Returns:
    - Root node of the constructed KD-Tree.
    """
 
    # The ending index is the last one of the pont list by default
    if end is None:
        end = len(point_list)

    # No node in the current sub-tree
    if start >= end:
        return None
    
    # Ensure all points have the same dimension
    num_dimensions = len(point_list[0])
    if not all(len(point) == num_dimensions for point in point_list):
        raise ValueError("All points must have the same dimension")

    # Select axis based on depth so that axis cycles through all valid values
    axis = depth % num_dimensions

    # Sort point list based on the current axis
    point_list[start:end] = sorted(point_list[start:end], key=lambda x: x[axis])

    # Choose median as pivot element
    median = (start + end) // 2

    # Create node and construct subtrees
    return Node(
        point_list[median],
        kd_tree(point_list, depth + 1, start, median),
        kd_tree(point_list, depth + 1, median + 1, end)
    )
points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
tree = kd_tree(points) 
print_preorder(tree)

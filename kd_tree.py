class Node:
    def __init__(self, point, left_child, right_child):
        self.point = point
        self.left_child = left_child
        self.right_child = right_child

def kd_tree(point_list, depth=0, start=0, end=None):
    
    # The ending index is the last one of the pont list by default
    if end is None:
        end = len(point_list)

    # No node in the current sub-tree
    if start >= end:
        return None
    
    # Select axis based on depth so that axis cycles through all valid values
    k = len(point_list[0])  # assumes all points have the same dimension
    axis = depth % k

    # Sort point list and choose median as pivot element
    point_list.sort(key=lambda x: x[axis])
    median = len(point_list) // 2  # choose median

    # Create node and construct subtrees
    return Node(
        point_list[median],
        kd_tree(point_list[:median], depth + 1),
        kd_tree(point_list[median + 1:], depth + 1)
    )

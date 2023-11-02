class Node:
    def __init__(self, median=None, left=None, right=None, points_list=None):
        self.median = median
        self.points_list = points_list
        self.left = left
        self.right = right

class KDTree:
    def __init__(self, threshold=2, dimensions=2):
        self.root = None
        self.threshold = threshold
        self.dimensions = dimensions

    def build_tree(self, points):
        self.root = build_kd_tree(points, self.threshold, 0, self.dimensions)

    def range_search(self, query_point, radius):
        return kd_tree_range_search(self.root, query_point, radius, 0, self.dimensions)

def build_kd_tree(points, threshold=2, depth=0, dimensions=2):
    if len(points) <= threshold:
        return Node(points_list=points)

    # Select axis based on depth so that axis cycles through all valid values
    axis = depth % dimensions
    sorted_points = sorted(points, key=lambda point: point[axis])

    # Correct median calculation
    median_index = len(sorted_points) // 2

    # Create a new node and construct the subtrees
    return Node(
        median=sorted_points[median_index][axis],
        left=build_kd_tree(sorted_points[:median_index], threshold, depth + 1, dimensions),
        right=build_kd_tree(sorted_points[median_index:], threshold, depth + 1, dimensions)
    )

def kd_tree_range_search(node, query_point, radius, depth=0, dimensions=2):
    if node is None:
        return []

    results = []
    axis = depth % dimensions

    # Check if the current node is a leaf node
    if node.median is None:
        # Check if points in the leaf node are within the query range
        if node.points_list is not None:
            for point in node.points_list:
                if all(abs(point[dim] - query_point[dim]) <= radius for dim in range(dimensions)):
                    results.append(point)
        return results

    # For non-leaf nodes
    dist_axis = query_point[axis] - node.median

    # Determine which side of the node the query point lies
    next_branch = node.left if dist_axis < 0 else node.right
    opposite_branch = node.right if dist_axis < 0 else node.left

    # Search the next branch
    results = kd_tree_range_search(next_branch, query_point, radius, depth + 1, dimensions)

    # If the query circle crosses the dividing line, search the opposite branch
    if abs(dist_axis) < radius:
        results.extend(kd_tree_range_search(opposite_branch, query_point, radius, depth + 1, dimensions))

    # Check if points in the leaf node are within the query range
    if node.points_list is not None:
        for point in node.points_list:
            if all(abs(point[dim] - query_point[dim]) <= radius for dim in range(dimensions)):
                results.append(point)

    return results
def preorder_traversal(root):
    """
    Preorder tree traversal also known as root-to-leaf or serial traversal.
    """
    if root is not None:
        if(root.median is not None):
            # print(root.median)
            preorder_traversal(root.left)
            preorder_traversal(root.right)
        else:
            print(root.points_list)

def create_inverted_index(node, inverted_index = {}):


def create_inverted_index(node, inverted_index = {}):

    # Base case: If the node is a leaf node, print its points
    if node.median is None:
        index = len(inverted_index)
        # print(index, node.points_list)
        inverted_index[index] = node.points_list
        
    
    # Recursive case: Traverse the left and right subdtrees
    if node.left:
        create_inverted_index(node.left)
    if node.right:
        create_inverted_index(node.right)
    return inverted_index
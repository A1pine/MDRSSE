class Node:
    def __init__(self, partition_value=None, points_left=None, points_right=None, left=None, right=None):
        self.partition_value = partition_value
        self.points_left = points_left
        self.points_right = points_right
        self.left = left
        self.right = right

def build_kd_tree(points, threshold=3, depth=0):
    if not points:
        return None
    
    # Select axis based on depth so that axis cycles through all valid values
    axis = depth % 2
    sorted_points = sorted(points, key=lambda point: point[axis])
    median = len(sorted_points) // 2
    
    # If the number of points is less than or equal to the threshold, then it's a leaf node
    if len(points) <= threshold:
        if median == 0:
            return Node(points_left=sorted_points[:median], points_right=sorted_points[median:])
        return Node(points_left=sorted_points[:median], points_right=sorted_points[median:])
    
    # Create a new node and construct the subtrees
    return Node(
        partition_value=sorted_points[median][axis],
        left=build_kd_tree(sorted_points[:median], threshold, depth + 1),
        right=build_kd_tree(sorted_points[median:], threshold, depth + 1)
    )

node_counter = 1
def print_leaf_nodes(node):
    global node_counter

    # Base case: If the node is a leaf node, print its points
    if node.points_left or node.points_right:
        if node.points_left:
            print(f'n{node_counter}, {node.points_left}')
            node_counter += 1
        if node.points_right:
            print(f'n{node_counter}, {node.points_right}')
            node_counter += 1
        return
    
    # Recursive case: Traverse the left and right subtrees
    if node.left:
        print_leaf_nodes(node.left)
    if node.right:
        print_leaf_nodes(node.right)



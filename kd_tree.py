class Node:
    def __init__(self, median=None, left=None, right=None, points_list=None):
        self.median = median
        self.points_list = points_list
        self.left = left
        self.right = right

def build_kd_tree(points, threshold=2, depth=0, dimensions = 2):
    if len(points) <= threshold:
        return Node(points_list=points)
    
    
    # Select axis based on depth so that axis cycles through all valid values
    axis = depth % dimensions
    sorted_points = sorted(points, key=lambda point: point[axis])
    median = len(sorted_points) // dimensions

    PAMList = sorted_points[median:]
    PBMList = sorted_points[:median]

    
    
    # Create a new node and construct the subtrees
    return Node(
        median=sorted_points[median][axis],
        left=build_kd_tree(sorted_points[:median], threshold, depth + 1),
        right=build_kd_tree(sorted_points[median:], threshold, depth + 1)
    )

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


# def create_inverted_index(node, index=None, path=''):
#     if index is None:  # If there is no index yet, create an empty one
#         index = {}
#     if node is not None:
#         if node.points_list is not None:  # If we're at a leaf node
#             for point in node.points_list:
#                 # Convert the point to a string to use as a key
#                 point_str = str(point)
#                 if point_str not in index:
#                     index[point_str] = []
#                 # Add the path to this node to the list of paths for this point
#                 index[point_str].append(path)
#         else:  # If we're not at a leaf node
#             # Recurse on the left and right children, adding 'L' or 'R' to the path
#             create_inverted_index(node.left, index, path + 'L')
#             create_inverted_index(node.right, index, path + 'R')
#     return index

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
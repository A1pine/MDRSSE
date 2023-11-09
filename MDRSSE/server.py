# server.py
from MDRSSE.kdtree import KDTree

class MDRSSEServer:
    def __init__(self):
        self.kd_tree = KDTree()
        self.encrypted_data = {}
        self.tags = {}

    def build_index(self, encrypted_data, tags):
        self.encrypted_data = encrypted_data
        self.tags = tags
        data_points = [list(map(float, point.split(','))) for point in tags.keys()]
        self.kd_tree.build_tree(data_points)

    def range_search(self, query):
        if self.kd_tree.root is None:
            raise ValueError("Index not built yet")
        indices = self.kd_tree.range_search(query['point'], query['radius'])
        return [self.encrypted_data[self.tags[self.point_to_string(point)]] for point in indices]

    def point_to_string(self, point):
        return ','.join(f'{coord:.1f}' for coord in point)


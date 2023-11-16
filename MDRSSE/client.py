# client.py

import json
from cryptography.fernet import Fernet
import hashlib

class MDRSSEClient:
    def __init__(self):
        # Master key for Fernet symmetric encryption, corresponds to 'K' in the paper
        self.master_key = Fernet.generate_key()
        self.fernet = Fernet(self.master_key)

    def encrypt_data(self, data):
        # Encrypts data records (ER) using symmetric encryption
        return self.fernet.encrypt(json.dumps(data).encode())

    def decrypt_data(self, encrypted_data):
        # Decrypts the encrypted data records
        return json.loads(self.fernet.decrypt(encrypted_data).decode())
    
    def decrypt_results(self, encrypted_results):
        return [self.decrypt_data(encrypted_data) for encrypted_data in encrypted_results]

    def point_to_string(self, point):
        # Converts a data point to a string representation
        return ','.join(f'{coord:.1f}' for coord in point)

    def generate_tag(self, point):
        # Generates a tag for each data point using a PRF (pseudorandom function)
        # This tag corresponds to 'T' in the paper
        point_str = self.point_to_string(point)
        return hashlib.sha256((point_str + self.master_key.decode()).encode()).hexdigest()

    def prepare_data(self, data_points):
        # Prepares the encrypted data store (EDS) and the set of tags (ST)
        encrypted_data = {}  # EDS
        tags = {}  # ST
        for point in data_points:
            encrypted_point = self.encrypt_data(point)  # Encrypting each data point (ER)
            tag = self.generate_tag(point)  # Generating tag (T)
            encrypted_data[tag] = encrypted_point
            tags[self.point_to_string(point)] = tag
        return encrypted_data, tags

    def create_search_query(self, query_range):
        # Prepares the search query (q) for the range search (RS)
        return {'point': query_range['point'], 'radius': query_range['radius']}

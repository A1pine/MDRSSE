# main.py

from MDRSSE.client import MDRSSEClient
from MDRSSE.server import MDRSSEServer

def ClientSearch(client, query_range):
    # Client prepares the search query (q) for the range search (RS)
    return client.create_search_query(query_range)

def ServerSearch(server, query):
    # Server performs the range search (RS) on the encrypted KD-Tree (kdt')
    # using the search query (q) and returns encrypted results (ER)
    return server.range_search(query)

def Search(query_range, client, server):
    # Main search function that orchestrates the client and server search
    # Client prepares the search token (q)
    search_token = ClientSearch(client, query_range)

    # Server performs the search with the search token (q)
    encrypted_search_results = ServerSearch(server, search_token)

    # Client decrypts the results (ER)
    return client.decrypt_results(encrypted_search_results)

def main():
    client = MDRSSEClient()
    server = MDRSSEServer()

    data_points = [
    [66, 430],
    [32, 120],
    [47, 110],
    [27, 200],
    [35, 470],
    [36, 280],
    [42, 250],
    [64, 210],
    [50, 365],
    [58, 510],
    [47, 540],
    [67, 620]]
    encrypted_data, tags = client.prepare_data(data_points)
    server.build_index(encrypted_data, tags)

    query_range = {'point': [35, 470], 'radius': 2.0}
    decrypted_results = Search(query_range, client, server)

    print("Decrypted Search Results:", decrypted_results)

if __name__ == "__main__":
    main()

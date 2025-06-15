import heapq
import matplotlib.pyplot as plt
import networkx as nx 
from collections import defaultdict

def dijkstra_via_heap(graph: dict, start_vertex: str) -> tuple[dict, dict]:

    distances = {vertex: float('inf') for vertex in graph}
    distances[start_vertex] = 0
    
    dict_of_previous = {vertex: None for vertex in graph}
    
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                dict_of_previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances, dict_of_previous


def get_path(dict_of_previous: dict, start_vertex: str, end_vertex: str) -> list:

    path = []
    current_vertex = end_vertex
    
    while current_vertex is not None:
        path.insert(0, current_vertex)
        
        if current_vertex == start_vertex:
            break
        current_vertex = dict_of_previous[current_vertex]
    
    if not path or path[0] != start_vertex:
        return []
        
    return path


def get_distance(distances: dict, end_vertex: str) -> float:
    return distances.get(end_vertex, float('inf'))


def visualize_graph_and_path(graph_data: dict, shortest_path: list = None, start_node: str = None, target_node: str = None):
   
    G = nx.Graph() 
    edge_labels = {}
    
    for u, neighbors in graph_data.items():
        
        for v, weight in neighbors:
            
            if not G.has_edge(u, v):
                G.add_edge(u, v, weight=weight)
                edge_labels[(u, v)] = weight

    plt.figure(figsize=(10, 10)) 

    pos = nx.planar_layout(G)
   
    node_colors = []
    for node in G.nodes():
        if shortest_path and node in shortest_path:
            node_colors.append('yellow')
        else:
            node_colors.append('skyblue')

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1000)

    all_edges = G.edges(data=True)
    path_edges = []
    other_edges = []

    if shortest_path and len(shortest_path) > 1:
        for i in range(len(shortest_path) - 1):
            u, v = shortest_path[i], shortest_path[i+1]
            
            if G.has_edge(u, v):
                path_edges.append((u, v))
            elif G.has_edge(v, u):
                path_edges.append((v, u))

    for u, v, data in all_edges:
        if (u, v) not in path_edges and (v, u) not in path_edges:
            other_edges.append((u, v))

    nx.draw_networkx_edges(G, pos, edgelist=other_edges, edge_color='gray', width=1.0)
    
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3.0)

    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue', font_size=8)

    plt.axis('off')
    plt.show()



if __name__ == '__main__':
    graph_sample = {
        'A': [('B', 1), ('C', 4), ('E', 10)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1), ('E', 6)],
        'D': [('B', 5), ('C', 1), ('G', 1)],
        'E': [('A', 10), ('C', 6)],
        'G': [('D', 1)]
    }
    
    start_vertex = 'A'
    target_vertex = 'E'

    shortest_distances, dict_of_previous = dijkstra_via_heap(graph_sample, start_vertex)
    
    print(f'Найкоротший шлях від вершини "{start_vertex}" до вершини {target_vertex} \n')
    
    dist = get_distance(shortest_distances, target_vertex)
    if dist == float('inf'):
        print(f'Шлях до точки "{target_vertex}" не знайдено')
        path_to_target = []
    else:
        print(f'Найкоротший шлях до точки "{target_vertex}" знайдено: \nДистанція - {dist}')
        path_to_target = get_path(dict_of_previous, start_vertex, target_vertex)
        print(f'Шлях: {" -> ".join(path_to_target)}')
        
    print('\nПерелік найкоротших шляхів до всіх вершин\n')
    
    for vertex in graph_sample:
        if vertex == start_vertex:
            continue
            
        current_path = get_path(dict_of_previous, start_vertex, vertex)
        distance = get_distance(shortest_distances, vertex)
        
        if current_path:
            print(f'Шлях від {start_vertex} до {vertex}: {" -> ".join(current_path)}. Загальна довжина: {distance}')
        else:
            print(f'Шлях від {start_vertex} до {vertex} не знайдено.')

    visualize_graph_and_path(graph_sample, path_to_target, start_vertex, target_vertex)
from DataStructures.Map import map_linear_probing as mlp
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Graph import vertex as v
from DataStructures.Graph import edge as e
from DataStructures.Graph import digraph as dg
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as s

def bfs(my_graph, source):
    graph_search = mlp.new_map(num_elements= dg.order(my_graph), load_factor=0.5, prime=109345121)
    bfs_vertex(my_graph, source, graph_search)
    return graph_search

def bfs_vertex(my_graph, source, visited_map):
    cola = q.new_queue()
    q.enqueue(cola, source)
    
    while not q.is_empty(cola):
        vertex = q.dequeue(cola)

        adj_list = dg.adjacents(my_graph, vertex)

        for i in range(sl.size(adj_list)):
            w = sl.get_element(adj_list, i)

            if not mlp.contains(visited_map, w):

                prev_info = mlp.get(visited_map, vertex)

                mlp.put(visited_map, w, {
                    "edge_from": vertex,
                    "dist_to": prev_info["dist_to"] + 1
                })

                q.enqueue(q, w)

    return visited_map


def has_path_to(key_v, visited_map):
    return map.contains(visited_map, key_v)
    
def path_to(vertex, visited_map):
    # Si el vértice no fue visitado, no hay un camino
    info = visited_map.get(vertex) 
    if info is None or not info['marked']:
        return None
    
    camino = s.new_stack()
    while vertex is not None:
        s.push(camino, vertex)
        vertex = visited_map[vertex]['edge_from']

    return camino


"""
def dijkstra():
    pass
def dist_to():
    pass
def has_path_to():
    pass
def path_to():
    pass
    """
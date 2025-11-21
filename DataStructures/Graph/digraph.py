from DataStructures.Map import map_linear_probing as mlp
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Graph import vertex as v
from DataStructures.Graph import edge as e


def new_graph(order):
    num_edges = 0
    vertex = mlp.new_map(order, 0.5, prime=109345121)
    
    graph = {'vertices': vertex,
             'num_edges': num_edges}
    
    return graph

def insert_vertex(my_graph, key_u, info_u):
    
    if mlp.contains(my_graph["vertices"], key_u) == True:
        update_vertex_info(my_graph, key_u, info_u)
    else:
        vertice_n = v.new_vertex(key_u, info_u)
        mlp.put(my_graph['vertices'], key_u, vertice_n)
    
    return my_graph 
     
            
def update_vertex_info(my_graph, key_u, new_info):
    
    vertice = mlp.get(my_graph["vertices"], key_u)
    vertice = new_info
    mlp.put(my_graph["vertices"], key_u, vertice)
    
    return my_graph
    
'''  
def add_edge():
    pass
def contains_vertex():
    pass
'''
def order(my_graph):
    order = mlp.size(my_graph)
    return order

def size(my_graph):#numero de arcos del grafo
    vertices = mlp.key_set(my_graph)
    s = 0
    for llave in vertices:
        vertice = mlp.get(my_graph,llave)
        adyacentes = v.get_adjacents(vertice)
        s += mlp.size(adyacentes)
    return s

def degree(my_graph, llave):
    vertice = mlp.get(my_graph, llave)
    degree = v.degree(vertice)
    return degree

def adjacents(my_graph, key_u):
    vertice = mlp.get(my_graph, key_u)
    adyacentes = v.get_adjacents(vertice)
    lista = mlp.key_set(adyacentes)
    
    return lista


def vertices(my_graph):
    lista = mlp.key_set(my_graph)
    
    return lista


"""
edges_vertex()
get_vertex()
update_vertex_info()
get_vertex_information(
    """
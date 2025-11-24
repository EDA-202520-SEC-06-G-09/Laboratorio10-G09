from DataStructures.Map import map_linear_probing as mlp
from DataStructures.List import array_list as al
from DataStructures.Stack import stack as st
from DataStructures.List import single_linked_list as sl
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Graph import vertex as v
from DataStructures.Graph import edge as e
from DataStructures.Graph import digraph as dg

def new_dfs_structure(graph, source):
    """
    Crea la estructura de búsqueda para DFS.

    Atributos:
    - source: vertice de inicio
    - marked: mapa de visitados
    - edge_to: mapa que guarda de dónde llegué a cada vertice
    """
    search = {
        "source": source,
        "marked": map.new_map(num_elements=dg.order(graph), load_factor=0.5),
        "edge_to": map.new_map(num_elements=dg.order(graph), load_factor=0.5)
    }
    return search


def dfs(graph, source):
    """
    Ejecuta DFS desde el vertice source.
    Retorna la estructura de búsqueda con marked y edge_to llenos.
    """
    search = new_dfs_structure(graph, source)
    dfs_vertex(graph, search, source)
    return search


def dfs_vertex(graph, search, vertex):
    """
    DFS recursivo desde vertex.
    Marca vertex y explora sus adyacentes no visitados.
    """
    map.put(search["marked"], vertex, True)

    adj_list = dg.adjacents(graph, vertex)
    for adj in adj_list:
        if not map.contains(search["marked"], adj):
            map.put(search["edge_to"], adj, vertex)
            dfs_vertex(graph, search, adj)


def has_path_to(search, vertex):
    """
    Indica si vertex es alcanzable desde el source.
    """
    return map.contains(search["marked"], vertex)


def path_to(search, vertex):
    """
    Retorna el camino desde source hasta vertex en forma de pila.
    Si no hay camino, retorna None.
    """
    if not has_path_to(search, vertex):
        return None

    path = st.new_stack()
    current = vertex

    while current != search["source"]:
        st.push(path, current)
        entry = map.get(search["edge_to"], current)
        current = entry["value"]

    st.push(path, search["source"])
    return path

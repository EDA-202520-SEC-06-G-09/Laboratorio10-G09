from DataStructures.Map import map_linear_probing as map
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import digraph as G
from DataStructures.Graph import dijsktra_structure as dks
from DataStructures.List import array_list as lt
import math 
from DataStructures.Priority_queue import pq_entry as pq_entry
from DataStructures.Graph import edge as edge
from DataStructures.Graph import vertex as vertex
from DataStructures.Stack import stack as s


def init_structure(graph, source):
    """
    Crea e inicializa la estructura utilizada para construcción del árbol de caminos de
    costo mínimo (Algoritmo de Dijkstra) a partir del vértice source
    """
    structure = dks.new_dijkstra_structure(source, G.order(graph))
    vertices = G.vertices(graph)
    for i in range(lt.size(vertices)):
        vert = lt.get_element(vertices, i)
        map.put(structure['visited'], vert, {'marked':False, 'edge_from':None,'dist_to':math.inf})
    map.put(structure['visited'], source, {'marked':False, 'edge_from':None, 'dist_to':0})
    pq.insert(structure['pq'], 0, source )
    return structure

def dijkstra(my_graph, source):
    if not G.contains_vertex(my_graph, source):
        return None
    
    estructura = init_structure(my_graph,source)
    mapa_visitados = estructura["visited"]
    pila = estructura["pq"]
    while not pq.is_empty(pila):
        v = pq.remove(pila)
        nodo = pq_entry.get_value(v)
        peso = pq_entry.get_priority(v)
        dict = map.get(mapa_visitados, nodo)
        dict['marked'] = True
        vertice = G.get_vertex(my_graph,nodo)
        adjacentes = G.adjacents(my_graph, nodo)
        
        for i in range(lt.size(adjacentes)):
            ad = lt.get_element(adjacentes, i) #llaves adjacentes
            arco = vertex.get_edge(vertice,ad)
            pesoad = edge.weight(arco)
            dictad = map.get(mapa_visitados, ad)
            if (peso + pesoad) < dictad["dist_to"]:
                dictad["edge_from"] = nodo
                dictad["dist_to"] = peso + pesoad
                
                if not pq.contains(pila,ad):
                    pq.insert(pila,dictad["dist_to"],ad)
                else:
                    pq.improve_priority(pila,ad,dictad["dist_to"])

    return estructura
                


def dist_to(key_v, aux_structure):
    mapa = aux_structure["visited"]
    d = map.get(mapa,key_v) #diccionario marked, edge_from, dist_to 
    if d is None:
        return math.inf
    return d["dist_to"]

def has_path_to(key_v, aux_structure):
    mapa = aux_structure["visited"]
    d = map.get(mapa,key_v) #diccionario marked, edge_from, dist_to 
    if d is None:
        return False
    return d["marked"]

def path_to(key_v, aux_structure):
    if not has_path_to(key_v,aux_structure):
        return None
    
    mapa = aux_structure["visited"]
    llave = key_v
    pila = s.new_stack()
    s.push(pila,llave)
    while llave != aux_structure["source"]:
        d = map.get(mapa,llave)
        desde = d["edge_from"]
        s.push(pila,desde)
        llave = desde
        
    return pila


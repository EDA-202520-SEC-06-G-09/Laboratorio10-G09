from DataStructures.Priority_queue import pq_entry as pq
from DataStructures.List import array_list as al

def new_heap (is_min_pq=True):
    
    heap = {'elements': al.new_list(), # lista tipo arreglo
            'size': 0,
            'cmp_function': None # función que compara valores de prioridad
            }
    pareja_invalida = pq.new_pq_entry(None, None)
    al.add_first(heap['elements'], pareja_invalida) # pareja invalida que ocupa la posición 0
    if is_min_pq == True: # caso donde la cola de prioridad esta orientada a menor
        heap['cmp_function'] = default_compare_lower_value # comparación si el padre tiene una prioridad menor o igual a sus hijos
    else: # caso donde la cola de prioridad esta orientada a Mayor
        heap['cmp_function'] = default_compare_higher_value # comparación si el padre tiene una prioridad MAYOR o igual a sus hijos
    return heap


def default_compare_lower_value(father_node, child_node):
    if pq.get_priority(father_node) <= pq.get_priority(child_node):
        return True
    return False

def default_compare_higher_value(father_node, child_node):
    if pq.get_priority(father_node) >= pq.get_priority(child_node):
        return True
    return False

def insert(my_heap, priority, value):
    entrada = pq.new_pq_entry(priority,value)
    elementos_heap = my_heap["elements"]
    al.add_last(elementos_heap,entrada)
    pos = my_heap["size"] + 1
    swim(my_heap, pos)
    my_heap["size"] += 1
    
    return my_heap
   

def swim(my_heap, pos):
    
    hijo = pos
    padre = hijo // 2 #asi se hace para encontrar al padre de un nodo
    
    while hijo > 1 and priority(my_heap, al.get_element(my_heap["elements"], padre), al.get_element(my_heap["elements"], hijo)) == False: 
         
        exchange(my_heap, padre, hijo)
        
        hijo = padre #el hijo se vuelve el padre
        padre = hijo // 2 #se actualiza la nueva posicion dl padre
        
    return my_heap
   

def priority(my_heap, parent, child):
    return my_heap["cmp_function"](parent, child)
    

def exchange(my_heap, pos_i, pos_j):
    elem = my_heap["elements"]
    # Un solo intercambio. Con dos lo deshaces.
    al.exchange(elem, pos_i, pos_j)

       
def is_empty(my_heap):
    if my_heap["size"] == 0:
        return True
    
    return False

def size(my_heap):
    return my_heap["size"]


def get_first_priority(my_heap):
    
    if is_empty(my_heap) == True:
        return None
    else:
        primer = al.get_element(my_heap["elements"], 1)
        return pq.get_value(primer)


def sink(my_heap, pos):
    """Restaura la propiedad del heap empujando el nodo en `pos` hacia abajo."""
    size = my_heap["size"]
    elems = my_heap["elements"]
    i = pos

    while 2 * i <= size:
        left = 2 * i
        right = left + 1

        # elegir el mejor hijo según la orientación del heap
        best = left
        if right <= size:
            if priority(my_heap, al.get_element(elems, left), al.get_element(elems, right)) is False:
                best = right

        # si el padre ya cumple con el mejor hijo, detener
        if priority(my_heap, al.get_element(elems, i), al.get_element(elems, best)):
            break

        # bajar
        exchange(my_heap, i, best)
        i = best

    return my_heap


def remove(my_heap):
    
    if is_empty(my_heap):
        return None
    
    primero = get_first_priority(my_heap)
    ultimo = my_heap["size"]
    exchange(my_heap, 1, ultimo)
    
    al.change_info(my_heap['elements'], ultimo, pq.new_pq_entry(None, None))
    my_heap["size"] -= 1
    
    sink(my_heap, 1)
    
    return primero


def is_present_value(my_heap, value):
    """Retorna la POSICIÓN (int) donde aparece 'value'; si no existe, -1."""
    siz = size(my_heap)
    for i in range(1, siz + 1):
        entrada = al.get_element(my_heap["elements"], i)
        if pq.get_value(entrada) == value:
            return i
    return -1

def contains(my_heap, value):
    """True si 'value' está en el heap; False en caso contrario."""
    return is_present_value(my_heap, value) != -1

def improve_priority(my_heap, value, new_priority):
    """
    Mejora la prioridad de 'value' y reubica el nodo.
    Para MinPQ, 'mejor' = prioridad numéricamente menor.
    Para MaxPQ, 'mejor' = prioridad numéricamente mayor.
    Retorna la posición final si lo encontró; de lo contrario None.
    """
    # buscar la posición del value
    siz = size(my_heap)
    pos = -1
    for i in range(1, siz + 1):
        entrada = al.get_element(my_heap["elements"], i)
        if pq.get_value(entrada) == value:
            pos = i
            break
    if pos == -1:
        return None

    # actualizar prioridad
    entrada = al.get_element(my_heap["elements"], pos)
    pq.set_priority(entrada, new_priority)
    al.change_info(my_heap["elements"], pos, entrada)

    # reubicar (subir si mejoró; si no, bajar)
    swim(my_heap, pos)
    sink(my_heap, pos)

    # devolver posición final
    for i in range(1, my_heap["size"] + 1):
        if pq.get_value(al.get_element(my_heap["elements"], i)) == value and \
           pq.get_priority(al.get_element(my_heap["elements"], i)) == new_priority:
            return i
    return pos
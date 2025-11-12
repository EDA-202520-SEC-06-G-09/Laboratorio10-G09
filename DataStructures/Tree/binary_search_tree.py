from DataStructures.Tree import bst_node as bs
from DataStructures.List import single_linked_list as sl


def new_node(key, value):
  return {'key': key, 'value': value, 'left':None, 'right':None}
#import bst_node as bs

def new_map():
    new_map = {
        'root': None
    }
    return new_map

def put(my_bst,key,value):
    
    my_bst['root'] = insert(my_bst['root'], key, value)
    return my_bst
    
def insert(node, key, value):
    if node is None:
      return bs.new_node(key, value)
    else:
      if key < node['key']:
        node['left'] = insert(node['left'], key, value) 
      elif key > node['key']:
        node['right'] = insert(node['right'], key, value)   
      else:
        node['value'] = value
      
      return node
  


def get(my_bst, key):
    if my_bst["root"] is None:
        return None
    else:
        root = my_bst["root"]
        nodo = get_node(root,key)
        if nodo is None:
            return None
        return bs.get_value(nodo)


def get_node(root, key):
    if root is None:
        return None

    if key == bs.get_key(root):
        return root
    
    elif key < bs.get_key(root):
        return get_node(root["left"],key)
        
    
    elif key > bs.get_key(root):
        return get_node(root["right"],key)
       
def remove(my_bst, key):

    root = my_bst["root"]
    my_bst["root"] = remove_node(root, key)
    return my_bst


def remove_node(node, key):
    
    # Caso base: subarbol vacio
    if node is None:
        return None

    k = bs.get_key(node)

    # Buscar en subarbol izquierdo o derecho
    if key < k:
        node["left"] = remove_node(node["left"], key)
    elif key > k:
        node["right"] = remove_node(node["right"], key)
    else:
        # Caso 1: sin hijo izquierdo
        if node["left"] is None:
            return node["right"]

        # Caso 2: sin hijo derecho
        if node["right"] is None:
            return node["left"]

        # Caso 3: dos hijos
        # Reemplazar por el sucesor in-order (minimo del subarbol derecho)
        temp = get_min_node(node["right"])    # ya la tienes implementada
        node["key"] = bs.get_key(temp)
        node["value"] = bs.get_value(temp)
        node["right"] = delete_min_tree(node["right"])  # ya la tienes también
        
    node["size"] = 1 + size(node["left"]) + size(node["right"])

    return node      
        
def is_empty(my_bst):
    if my_bst["root"] is None:
        return True
    else: 
        return False
    
def contains(my_bst,key):
    if get(my_bst,key) is None:
        return False
    else:
        return True

def key_set(my_bst):
    lista = sl.new_list()
    root = my_bst["root"]
    key_set_tree(lista,root)
    return lista

def key_set_tree(lista, root):
    if root is None:
        return 
    
    else:
        key_set_tree(lista, root["left"])
        sl.add_last(lista,bs.get_key(root))
        key_set_tree(lista,root["right"])
        

    
def value_set(my_bst):
    lista = sl.new_list()
    root = my_bst["root"]
    value_set_tree(lista,root)
    return lista

def value_set_tree(lista,root):
    if root is None:
        return 
    
    else:
        key_set_tree(lista, root["left"])
        sl.add_last(lista,bs.get_value(root))
        key_set_tree(lista,root["right"])
  
    
        
def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(root):
    
    if root is None:
        return 0
    else:
        siz = 1 + size_tree(root["right"]) + size_tree(root["left"])
        return siz
    

def get_max(my_bst):
    root = my_bst["root"]
    return get_max_node(root)

def get_max_node(root):
    
    n_actual = root
    if n_actual is None:
        return None
    
    while n_actual['right'] is not None:
        n_actual = n_actual['right']
    return bs.get_key(n_actual)

def delete_max(my_bst):
    if my_bst['root'] is None:
        return my_bst
    
    my_bst['root'] = delete_max_tree(my_bst['root'])
    return my_bst

def delete_max_tree(root):
    
    if root["right"] is None: 
        return root["left"]
    
    root["right"] = delete_max_tree(root["right"])
    root["size"] = 1 + size(root["left"]) + size(root["right"])
    
    return root

def values(my_bst, key_initial, key_final):
    
    list_value = sl.new_list()
    
    return values_range(my_bst["root"], key_initial, key_final, list_value)
    

def values_range(root, key_initial, key_final, list_value):
    
    if root is None:
        return list_value
    
    if root['key'] > key_initial:
        values_range(root['left'], key_initial, key_final, list_value)
        
    if key_initial <= root['key'] <= key_final:
        sl.add_last(list_value,root['value'])
    
    if root['key'] < key_final:
        values_range(root['right'], key_initial, key_final, list_value)
    
        
    return list_value

def keys(my_bst, key_initial, key_final):
    
    list_key = sl.new_list()
    
    return keys_range(my_bst["root"], key_initial, key_final, list_key)

def keys_range(root, key_initial, key_final, list_key):
    
    if root is None:
        return list_key
    
    if root['key'] > key_initial:
        keys_range(root["left"], key_initial, key_final, list_key)
        
    if root['key'] < key_final:
        keys_range(root['right'], key_initial, key_final, list_key)
    
    if  key_initial<= root['key'] <= key_final:
        sl.add_last(list_key, root['key'])
        
    return list_key
    

def get_min(my_bst):
    
    root = my_bst["root"]
    if root is None:
        return None
    min_node = get_min_node(root)
    return bs.get_key(min_node)


def get_min_node(node):

    if node is None:
        return None
    if node.get("left") is None:
        return node
    return get_min_node(node["left"])



def delete_min(my_bst):

    root = my_bst["root"]
    if root is None:
        return my_bst
    my_bst["root"] = delete_min_tree(root)
    return my_bst


def delete_min_tree(node):

    if node is None:
        return None
    if node.get("left") is None:
        return node.get("right")
    node["left"] = delete_min_tree(node["left"])
    node["size"] = 1 + size(node["left"]) + size(node["right"])
    return node

        
def floor(my_bst, key):

    node = floor_node(my_bst["root"], key)
    return None if node is None else bs.get_key(node)


def floor_node(node, key):
    if node is None:
        return None
    k = bs.get_key(node)
    if key == k:
        return node
    if key < k:
        return floor_node(node["left"], key)
    # key > k: podria estar en derecha o ser el mismo nodo
    t = floor_node(node["right"], key)
    return t if t is not None else node    

def ceiling(my_bst, key):

    node = ceiling_node(my_bst["root"], key)
    return None if node is None else bs.get_key(node)


def ceiling_node(node, key):
    if node is None:
        return None
    k = bs.get_key(node)
    if key == k:
        return node
    if key > k:
        return ceiling_node(node["right"], key)
    # key < k: podria estar en izquierda o ser el mismo nodo
    t = ceiling_node(node["left"], key)
    return t if t is not None else node


def select(my_bst, i):

    n = size(my_bst) # retorna el indice de la llave
    if i < 0 or i >= n:
        return None
    node = select_node(my_bst["root"], i)
    return None if node is None else bs.get_key(node)


def select_node(node, i):

    if node is None:
        return None
    left_sz = size_tree(node["left"])
    if i < left_sz:
        return select_node(node["left"], i)
    if i == left_sz:
        return node
    return select_node(node["right"], i - left_sz - 1)


def rank(my_bst, key):

    return rank_node(my_bst["root"], key)


def rank_node(node, key):
    if node is None:
        return 0
    k = bs.get_key(node)
    if key <= k:
        return rank_node(node["left"], key)
    # key > k: se cuenta el nodo y todo su subarbol izquierdo
    return 1 + size_tree(node["left"]) + rank_node(node["right"], key)

def height(my_bst):
    root = my_bst['root']
    return height_tree(root)

def height_tree(root):
    
    if root is None:
        return 0
    
    left_h = height_tree(root['left'])
    right_h = height_tree(root['right'])
    
    nodo_actual = 1 
    h = nodo_actual + (max(left_h, right_h))
    
    return h 
    
    
    
    
    
    
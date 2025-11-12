from DataStructures.Tree import rbt_node as rb
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al

RED = 0
BLACK = 1

def new_node(key, value, color=RED):
    return {'key': key, 'value': value, 'left': None, 'right': None, 'color': color}

def new_map():
    rbt = {
        'root': None, 
        'type': 'RBT'
    }
    return rbt


def default_compare(a, b):
    """Retorna -1 si a<b, 0 si a==b, 1 si a>b."""
    return (a > b) - (a < b)

def put(my_rbt, key, value):
    """
    Inserta (key,value) en el RBT. Si la llave existe, actualiza el valor.
    Asegura que la raíz quede negra.
    """
    root = my_rbt.get("root")
    root = insert_node(root, key, value)
    if root is not None:
        rb.change_color(root, BLACK)  # la raiz siempre negra
    my_rbt["root"] = root
    return my_rbt

def insert_node(node_rbt, key, value):
    """
    Inserción recursiva estilo LLRB:
      1) Insertar como en BST (nuevo nodo rojo)
      2) Fix-ups: rotate_left, rotate_right y flip_colors
    """
    if node_rbt is None:
        newn = rb.new_node(key, value)      # crea nodo
        if not rb.is_red(newn):        # forzar que nazca rojo
            rb.change_color(newn, RED)
        return newn

    k = rb.get_key(node_rbt)
    if key < k:
        node_rbt["left"] = insert_node(node_rbt["left"], key, value)
    elif key > k:
        node_rbt["right"] = insert_node(node_rbt["right"], key, value)
    else:
        node_rbt["value"] = value

    # ----- Fix-ups tipo LLRB -----
    if is_red(node_rbt.get("right")) and not is_red(node_rbt.get("left")):
        node_rbt = rotate_left(node_rbt)

    if is_red(node_rbt.get("left")) and is_red(node_rbt["left"].get("left")):
        node_rbt = rotate_right(node_rbt)

    if is_red(node_rbt.get("left")) and is_red(node_rbt.get("right")):
        flip_colors(node_rbt)

    return node_rbt

def rotate_left(h):
    x = h["right"]                 # x sube
    h["right"] = x["left"]
    x["left"] = h
    # colores
    x["color"] = h["color"]
    h["color"] = RED
    return x

def rotate_right(h):
    x = h["left"]                  # x sube
    h["left"] = x["right"]
    x["right"] = h
    # colores
    x["color"] = h["color"]
    h["color"] = RED
    return x


""" def rotate_left(node_rbt):
    #solo se hace cuando hay dos rojos consecutivos a la derecha del nodo raiz 
    
    if is_red(node_rbt["right"]) == True and is_red(node_rbt["right"]["right"])== True:
        nueva_raiz = node_rbt["right"]
        node_rbt["right"] = nueva_raiz["left"]
        nueva_raiz["left"] = node_rbt
        
        #Hacer el cambio o actualizaciones de colores entre las raizes nuevas y antiguas
        
        flip_node_color(node_rbt)
        flip_node_color(nueva_raiz)
        
        return nueva_raiz
    
    else:
        return node_rbt """


""" def rotate_right(node_rbt):
     #solo se hace cuando hay dos rojos consecutivos a la izquierda del nodo raiz 
    
    if is_red(node_rbt["left"]) == True and is_red(node_rbt['left']["left"]) == True:
        nueva_raiz = node_rbt["left"]
        node_rbt["left"] = nueva_raiz["right"]
        nueva_raiz["right"] = node_rbt
        
        #Hacer el cambio o actualizaciones de colores entre las raizes nuevas y antiguas
        
        flip_node_color(node_rbt)
        flip_node_color(nueva_raiz)
        
        return nueva_raiz
    
    else:
        return node_rbt """


def is_red(node_rbt):
    
    if node_rbt is None:
        return False
    
    return  rb.is_red(node_rbt)
       

def flip_colors(rbt_node):
    flip_node_color(rbt_node)
    if rbt_node["right"] is not None:
        flip_node_color(rbt_node["right"])
    if rbt_node["left"] is not None:
        flip_node_color(rbt_node["left"])
        
    return rbt_node

def flip_node_color(rbt_node):
    if rbt_node["color"] == RED:
        rb.change_color(rbt_node,BLACK)
    else:
        rb.change_color(rbt_node,RED)
    return rbt_node
        
def get(my_bst, key):
    if my_bst["root"] is None:
        return None
    else:
        root = my_bst["root"]
        nodo = get_node(root,key)
        if nodo is None:
            return None
        return rb.get_value(nodo)


def get_node(root, key):
    if root is None:
        return None

    if key == rb.get_key(root):
        return root
    
    elif key < rb.get_key(root):
        return get_node(root["left"],key)
        
    
    elif key > rb.get_key(root):
        return get_node(root["right"],key)
    

def remove(my_rbt, key):
    """
    Elimina la llave `key` (si existe) del árbol.
    Deja la raíz en negro si el árbol queda no vacío.
    """
    if my_rbt["root"] is None:
        return my_rbt
    my_rbt["root"] = remove_node(my_rbt["root"], key)
    if my_rbt["root"] is not None:
        rb.change_color(my_rbt["root"], BLACK)
    return my_rbt

def remove_node(node, key):
    """
    Eliminación tipo BST (Hibbard):
      - Si key < node.key: borrar en izquierda
      - Si key > node.key: borrar en derecha
      - Si key == node.key:
          * Caso 0/1 hijo: conectar el hijo que exista
          * Caso 2 hijos: reemplazar por el mínimo del subárbol derecho
                         y borrar dicho mínimo en el subárbol derecho
    (No realiza rebalanceo de colores; útil y suficiente para el lab)
    """
    if node is None:
        return None

    k = rb.get_key(node)
    if key < k:
        node["left"] = remove_node(node["left"], key)
        return node
    elif key > k:
        node["right"] = remove_node(node["right"], key)
        return node

    # key == k : borrar este nodo
    # 0 o 1 hijo
    if node.get("right") is None:
        return node.get("left")
    if node.get("left") is None:
        return node.get("right")

    # 2 hijos: tomar el sucesor (mínimo del subárbol derecho)
    succ = get_min_node(node["right"])
    node["key"] = rb.get_key(succ)
    node["value"] = rb.get_value(succ)
    # eliminar el mínimo del subárbol derecho
    node["right"] = delete_min_tree(node["right"])
    return node

def delete_max(my_rbt):
    """
    Elimina el máximo (si existe) del árbol.
    """
    if my_rbt["root"] is None:
        return my_rbt
    my_rbt["root"] = delete_max_tree(my_rbt["root"])
    if my_rbt["root"] is not None:
        rb.change_color(my_rbt["root"], BLACK)
    return my_rbt

def delete_max_tree(node):
    """
    Elimina y retorna el subárbol resultante tras borrar el máximo
    del subárbol con raíz `node`.
    """
    if node is None:
        return None
    if node.get("right") is None:
        # este es el máximo; reemplazar por su hijo izquierdo
        return node.get("left")
    node["right"] = delete_max_tree(node["right"])
    return node

def delete_min(my_rbt):
    """
    Elimina el mínimo (si existe) del árbol.
    """
    if my_rbt["root"] is None:
        return my_rbt
    my_rbt["root"] = delete_min_tree(my_rbt["root"])
    if my_rbt["root"] is not None:
        rb.change_color(my_rbt["root"], BLACK)
    return my_rbt

def delete_min_tree(node):
    """
    Elimina y retorna el subárbol resultante tras borrar el mínimo
    del subárbol con raíz `node`.
    """
    if node is None:
        return None
    if node.get("left") is None:
        # este es el mínimo; reemplazar por su hijo derecho
        return node.get("right")
    node["left"] = delete_min_tree(node["left"])
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
        sl.add_last(lista,rb.get_key(root))
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
        sl.add_last(lista,rb.get_value(root))
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
    return get_max_node(my_bst)

def get_max_node(root):
    
    n_actual = root['root']
    if n_actual is None:
        return None
    
    while n_actual['right'] is not None:
        n_actual = n_actual['right']
    return n_actual["key"]



def values(my_bst, key_initial, key_final):
    
    list_value = al.new_list()
    
    return values_range(my_bst["root"], key_initial, key_final, list_value)
    

def values_range(root, key_initial, key_final, list_value):
    
    if root is None:
        return list_value
    
    if root['key'] > key_initial:
        values_range(root['left'], key_initial, key_final, list_value)
        
    if key_initial <= root['key'] <= key_final:
        al.add_last(list_value,root['value'])
    
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
    return rb.get_key(min_node)


def get_min_node(node):

    if node is None:
        return None
    if node.get("left") is None:
        return node
    return get_min_node(node["left"])


def floor(my_bst, key):

    node = floor_node(my_bst["root"], key)
    return None if node is None else rb.get_key(node)


def floor_node(node, key):
    if node is None:
        return None
    k = rb.get_key(node)
    if key == k:
        return node
    if key < k:
        return floor_node(node["left"], key)
    # key > k: podria estar en derecha o ser el mismo nodo
    t = floor_node(node["right"], key)
    return t if t is not None else node    

def ceiling(my_bst, key):

    node = ceiling_node(my_bst["root"], key)
    return None if node is None else rb.get_key(node)


def ceiling_node(node, key):
    if node is None:
        return None
    k = rb.get_key(node)
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
    return None if node is None else rb.get_key(node)


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
    k = rb.get_key(node)
    if key <= k:
        return rank_node(node["left"], key)
    # key > k: se cuenta el nodo y todo su subarbol izquierdo
    return 1 + size_tree(node["left"]) + rank_node(node["right"], key)

def height(my_bst):
    root = my_bst['root']
    return height_tree(root)

def height_tree(root):
    
    if root is None:
        return -1
    
    left_h = height_tree(root['left'])
    right_h = height_tree(root['right'])
    
    nodo_actual = 1 
    h = nodo_actual + (max(left_h, right_h))
    
    return h 
    
    
    
    
    
    


"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import threading
from DataStructures.List import single_linked_list as sl
from App import logic

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


servicefile = 'bus_routes_14000.csv'
stopsfile = 'bus_stops.csv'
initialStation = None

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def print_menu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar información de buses de singapur") # Clase 1: Implementar digraph básico
    print("2- Encontrar las paradas más concurridas") # Casa 1: Implementar digraph completo
    print("3- Encontrar una ruta entre dos paradas (DFS)") # Casa 1: Implementar funcionalidad dfs
    print("4- Encontrar una ruta entre dos paradas (BFS)") # Clase 2: Implementar funcionalidad bfs
    print("5- Encontrar la ruta mínima entre dos paradas") # Casa 2: Implementar dijkstra
    print("6- Mostrar en un mapa la ruta mínima entre dos paradas") # Trabajo Complementario: Mostrar ruta con folium
    print("0- Salir")
    print("*******************************************")


def option_one(cont):
    print("\nCargando información de transporte de singapur ....")
    logic.load_services(cont, servicefile, stopsfile)
    numedges = logic.total_connections(cont)
    numvertex = logic.total_stops(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))

def option_two(cont):
    # TODO: Imprimir los resultados de la opción 2
    ...
def _split_vertex(vertex_id):
    """
    '66009-109' -> ('66009', '109')
    """
    parts = vertex_id.split("-")
    return parts[0], parts[1]

def option_three(cont):
    # TODO: Imprimir los resultados de la opción 3
    """
    Opción 3 en view:
    - pide stop1 y stop2
    - llama a la lógica (DFS)
    - imprime por tramos de bus
    """

    analyzer = cont   # cont es el analyzer casi siempre

    stop1 = input("Parada inicial: ")
    stop2 = input("Parada destino: ")

    print("\n... OPCIÓN 3 (DFS)")
    print(f"Parada inicial: '{stop1}'")
    print(f"Parada destino: '{stop2}'\n")

    route = logic.get_route_between_stops_dfs(analyzer, stop1, stop2)

    if route is None or sl.size(route) == 0:
        print("No existe ruta entre las paradas dadas.\n")
        return

    node = route["first"]

    stop_code, bus = _split_vertex(node["info"])
    current_bus = bus
    current_chain = [stop_code]

    print(f"Tomar bus '{current_bus}' desde '{stop_code}'\n")

    node = node["next"]

    while node is not None:
        stop_code, bus_now = _split_vertex(node["info"])

        if bus_now == current_bus:
            current_chain.append(stop_code)
        else:
            print(" -> ".join(current_chain) + "\n")
            print(f"Cambiar a bus '{bus_now}' en la parada '{stop_code}'\n")
            current_bus = bus_now
            current_chain = [stop_code]

        node = node["next"]

    print(" -> ".join(current_chain) + "\n")

def option_four(cont):
    # TODO: Imprimir los resultados de la opción 4
    ...

def option_five(cont):
    # TODO: Imprimir los resultados de la opción 5
    ...

def option_six(cont):
    # (Opcional) TODO: Imprimir los resultados de la opción 6
    ...


"""
Menu principal
"""


def main():
    working = True
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n>')

        if int(inputs[0]) == 1:
            print("\nInicializando....")
            cont = logic.new_analyzer()
            option_one(cont)
        elif int(inputs[0]) == 2:
            option_two(cont)
        elif int(inputs[0]) == 3:
            option_three(cont)
        elif int(inputs[0]) == 4:
            option_four(cont)
        elif int(inputs[0]) == 5:
            option_five(cont)
        elif int(inputs[0]) == 6:
            option_six(cont)
        else:
            working = False
            print("Saliendo...")
    sys.exit(0)


if __name__ == "__main__":
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()

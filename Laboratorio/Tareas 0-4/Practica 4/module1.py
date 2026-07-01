#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      moise
#
# Created:     18/03/2024
# Copyright:   (c) moise 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Implementar un clase Grafo donde los vértices es un conjunto y las aristas es un conjunto de 2-subconjuntos de vértices.
# Los 2-subconjuntos se implementan con frozenset({v, w}) si v, w vértices (pues Python no admite conjuntos de conjuntos)
# Las funciones y métodos son los obvios. Si G es grafo:
#     G.vertices(): es el conjunto de vértices
#     G.aristas(): es el conjunto de aristas
#     G.adyacentes(v): es el conjunto de vértices adyacentes a un vértice v
#     G.agregar_arista(e): agrega la arista e

def prim(G: Grafo , pesos):
    # pre: pesos un diccionario donde las claves son las aristas y los valores son reales no negativos.
    # post: devuelve mst un MST de G.
    r = next(iter(G.vertices())) # toma un vértice de G sin quitarlo
    clave, padre = {}, {} # dos diccionarios vacíos. El primero es una "cola de prioridad". El segundo indicará quien será el padre en el MST.
    INFINITO = 2 * max(pesos.values()) # INFINITO es un valor más alto que todos los pesos
    for u in G.vertices():
        clave[u] = INFINITO
        padre[u] = None # Cuando el algoritmo termina padre[v] será el padre de v en el MST, para los v que no son raíz (el vértice r).
    clave[r] = 0
    cola = G.vertices()
    while cola != set({}):
        u = min([[clave[v],v] for v in cola])[1] # un vértice de cola con clave[u] mínima
        cola.remove(u)
        for v in G.adyacentes(u):
            e = frozenset({u, v})
            if v in cola and pesos[e] < clave[v]:
                padre[v] = u
                clave[v] = pesos[e]
    mst = Grafo(G.vertices(), set({})) # este va a ser el MST. Se inicializa como un grafo con todos los vértices de G y si aristas.
    for v in mst.vertices() - {r}:
        mst.agregar_arista(frozenset({v,padre[v]}))
    return mst
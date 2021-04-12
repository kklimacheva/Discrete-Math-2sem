import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.approximation import clique
from networkx.algorithms.approximation import independent_set
from networkx.algorithms.approximation import vertex_cover
from networkx.algorithms import covering
from networkx.algorithms.bipartite import basic
from networkx.algorithms import tournament
from networkx.algorithms import euler
from networkx.algorithms import components
from networkx.algorithms.connectivity import edge_kcomponents
from networkx.algorithms.tree import mst
from networkx.algorithms.tree import coding

g = nx.Graph()
with open('europe.txt') as f:
    s = f.readlines()
    for i in s:
        c1, c2, w = i.split()
        g.add_edge(c1, c2, weight = int(w))
g.add_nodes_from(["CY", "IS", "MT"])

#a
nx.draw(g, pos=nx.planar_layout(g), with_labels=True)
plt.savefig("graph.png")
plt.clf()
print("Number of vertices")
print(len(g.nodes))
print("Number of edges")
print(len(g.edges))

#b
g1 = max(nx.connected_components(g), key = len) #поиск максимальной компоненты G*
g2 = nx.Graph() #максимальная компонента G
g3 = nx.DiGraph() #ориентированная максимальная компонента
with open('europe.txt') as f:
    s = f.readlines()
    for i in s:
        c1, c2, w = i.split()
        if (c1 in g1) and (c2 in g1):
            g2.add_edge(c1, c2, weight = int(w))
            g3.add_edge(c1, c2)
            g3.add_edge(c2, c1)
print("In max component:")
print("Number of vertices")
print(len(g2.nodes))
print("Number of edges")
print(len(g2.edges))
print("Max degree")
print(max(val for (node, val) in g2.degree()))
print("Min degree")
print(min(val for (node, val) in g2.degree()))
print("Radius")
print(nx.radius(g2))
print("Diameter")
print(nx.diameter(g2))
print("Center")
print(nx.center(g2))
print("Girth")
print(len(min(nx.cycle_basis(g2))))
print("k-vertex-connectivity")
print(nx.node_connectivity(g2))
print("k-edge-connectivity")
print(nx.edge_connectivity(g2))

#c
nodes_color = []
for i in (g2.nodes()): #массив цветов вершин
    val = nx.greedy_color(g2).get(i)
    nodes_color.append(val)
nx.draw_planar(g2, with_labels=True, node_color =nodes_color)
plt.savefig("vertex_color.png")
plt.clf()

#d
edges_color = []
for (v1,v2) in (g2.edges()): #массив цветов ребер
    val = nx.greedy_color(nx.line_graph(g2)).get((v1,v2))
    if val == None:
        val = nx.greedy_color(nx.line_graph(g2)).get((v2,v1))
    edges_color.append(val)
nx.draw_planar(g2, with_labels = True, edge_color = edges_color)
plt.savefig("edges_color.png")
plt.clf()

#e
print("Maximum clique")
print(clique.max_clique(g2))

#f
print("Maximum stable set")
print(independent_set.maximum_independent_set(g2)) 

#g
print("Maximum matching")
print(nx.max_weight_matching(g2, maxcardinality=True, weight=0))

#i
print("Minimum edge cover")
print(covering.min_edge_cover(g2)) #ищем минимальное реберное покрытие

#j
print("Hanging vertices")
print([u for v, u in g3.edges() if len(g3[u]) == 1]) #узнаем висячие вершины
g3.remove_nodes_from([u for v, u in g3.edges() if len(g3[u]) == 1]) #убираем висячие ребра
print("The shortest closed path that visits every vertex")
print(tournament.hamiltonian_path(g3))#ищем гамильтонов путь и добавляем в него высячие ребра

#k
print("The shortest closed path that visits every edge")
print(list(euler.eulerian_circuit(g3))) #ищем эйлеров путь и добавляем в него ребра-мосты к висячим вершинам

#m
print("2-edge-connected components")
print(list(edge_kcomponents.bridge_components(g)))

#o
mstree=nx.Graph(mst.minimum_spanning_tree(g2))
print("MST")
print(mstree.edges)
print("Weight of MST")
print(sum(c for (a,b,c) in (mstree.edges.data('weight'))))
nx.draw_planar(mstree,with_labels=True)
plt.savefig("mst.png")
plt.clf()


#q
print("Renamed vertices for Prufer code")
names={}
for k, v in enumerate(mstree):
    names[v]=k
print(names)
mstree = nx.relabel_nodes(mstree, names)
pr = coding.to_prufer_sequence(mstree)
print("Prufer code")
print(pr)#получаем код Прюфера

newdict={v:k for k, v in names.items()} 
print(newdict)
translete = []
for i in pr:
    translete.append(newdict.get(i))#перевод чисел в страны
print("Prufer code for countries")
print(translete)

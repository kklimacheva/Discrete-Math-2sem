import networkx as nx
import matplotlib.pyplot as plt

fin = open("bdsm-europe.txt", "r")
g = nx.MultiGraph()
while True:
    s = fin.readline().split()
    if not s:
        break
    c1 = s[0]
    c2 = s[1]
    w = s[2]
    g.add_edge(c1, c2, weight = w)
#nx.draw(g, pos=nx.planar_layout(g), with_labels=True)
#plt.savefig("t2.png")
print("number or vertices")
print(g.number_of_nodes()) #кол-во вершин
print(len(g.nodes))#добавть CY IS MT
print("number or edges")
print(g.size()) #кол-во ребер
g1 = max(nx.connected_components(g), key = len) #поиск максимальной компоненты

fin.seek(0,0)
g2 = nx.Graph() #максимальная компонента
while True:
    s = fin.readline().split()
    if not s:
        break
    c1 = s[0]
    c2 = s[1]
    w = s[2]
    if (c1 in g1) and (c2 in g1):
        g2.add_edge(c1, c2, weight=w)
print("center")
print(nx.center(g2)) #центр макс комп
print("radius ")
print(nx.radius(g2)) #радиус
print("diameter ")
print(nx.diameter(g2)) #диаметр
print("max degree ")
print(max(val for (node, val) in g2.degree())) #макс степень
print("min degree ")
print(min(val for (node, val) in g2.degree())) #мин степень
#print(nx.minimum_cycle_basis(g2))
print(nx.node_connectivity(g2)) #вершинная k-связанность
print(nx.edge_connectivity(g2)) #реберная k-связанность
print("girth ")
print(len(min(nx.cycle_basis(g2)))) #обхват



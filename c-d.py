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
#nx.draw_planar(g, with_labels=True)
#plt.savefig("t3.png")
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
        g2.add_edge(c1, c2, weight = w)

print(nx.greedy_color(nx.line_graph(g2))) #раскраска ребер
a = []
for i in (g2.nodes()): #массив цветов вершин
    val = nx.greedy_color(g2).get(i)
    a.append(val)
b = []
for (g,f) in (g2.edges()): #массив цветов ребер
    val = nx.greedy_color(nx.line_graph(g2)).get((g,f))
    if val == None:
        val = nx.greedy_color(nx.line_graph(g2)).get((f,g))
    b.append(val)
nx.draw(g2, pos=nx.planar_layout(g2), with_labels=True, node_color =a) #рисуем раскраску вершин графа
#print(nx.greedy_color(nx.line_graph(g2))) #раскраска ребер
nx.draw(g2, pos = nx.planar_layout(g2), with_labels = True, edge_color = b) #рисуем раскраску ребер графа
plt.show()
plt.savefig("c6.png")
print(nx.greedy_color(g2)) #раскраска вершин

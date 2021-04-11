import networkx as nx
import matplotlib.pyplot as plt

fin = open("europe.txt", "r")
g = nx.MultiGraph()
while True:
    s = fin.readline().split()
    if not s:
        break
    c1 = s[0]
    c2 = s[1]
    w = s[2]
    g.add_edge(c1, c2, weight=w)
nx.draw(g, pos=nx.planar_layout(g), with_labels=True)
nx.draw_planar(g, with_labels = True)
plt.savefig("1a-2v.png")
plt.show()

#иновое создание максимальной компоненты
#g1= min(nx.connected_components(g), key=len) #поиск максимальной компоненты
#fin.seek(0,0)
#g2=nx.Graph(g) #максимальная компонента
#g2.remove_nodes_from(g1)

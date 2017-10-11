import networkx as nx
from PIL import ImageDraw

from figures.circle import Circle


class Ex5:
    def __init__(self, img):
        self.img = img

    def doEx(self, nodes, edges, startPoint, endPoint):
        specialColor = (0,0,0)
        for id_ in nodes:
            if nodes[id_] == startPoint:
                startPointId = id_
            elif nodes[id_] == endPoint:
                endPointId = id_
        graph = nx.Graph()
        graph.add_edges_from(edges)
#        path = nx.dijkstra_path(graph, startPointId, endPointId)

        draw = ImageDraw.Draw(self.img)
        c = Circle((0,0), 2, specialColor)
        c.moveTo(startPoint).render(draw)
        prevNode = startPoint
        path = nx.dijkstra_path(graph, startPointId, endPointId)
        for nodeId in path[1:]:
            currentNode = nodes[nodeId]
            c.moveTo(currentNode).render(draw)
            draw.line((prevNode, currentNode), fill=specialColor, width=1)
            prevNode = currentNode

        c.moveTo(endPoint).scale(2).render(draw)

        return self.img, path

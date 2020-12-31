class graph():
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = []
        self.gdict = gdict


    def print_vertex(self):
        return self.gdict.keys()

    def print_edges(self):
        edgelist = []
        for vrtx in self.gdict:
            for nxtval in self.gdict[vrtx]:
                if {vrtx,nxtval} not in edgelist:
                    edgelist.append({vrtx,nxtval})

        return edgelist

graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)
print(g.print_edges())
            
            

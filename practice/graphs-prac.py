class graph():
    def __init__(self,gdict=None):
        if gdict is None:
            self.gdict = {}
        else:
            self.gdict = gdict

    def print_vertex(self):
        return ( self.gict.keys())

    def print_edge(self):
        edges = []
        for keys in self.gdict:
            for idx in self.gdict[keys]:
                if {keys,idx} not in edges: 
                    edges.append({keys,idx})

        return edges

    def add_edge(self,edge = None):
        edge = set(edge)
        (vrtx1,vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]


g = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

gs = graph(g)
print(gs.print_edge())
gs.add_edge({"a", "d"})
gs.add_edge({"a", "e"})
print(gs.print_edge())

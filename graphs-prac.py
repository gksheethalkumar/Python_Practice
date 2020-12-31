import pprint

class graph():
    def __init__(self,gdict):
        if gdict is None:
            gdict = {}

        self.gdict = gdict


    def vertex(self):
        return ( list(self.gdict.keys()))


    def edges(self):
        res = []
        for vrtx in self.gdict:
            for vals in self.gdict[vrtx]:
                if {vrtx,vals} not in res:
                    res.append({vrtx,vals})
        return res

    def add_edge(self,edge):
        edge = set(edge)
        (vrtx1,vrtx2) = tuple(edge)

        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = vrtx2

    def print_gdict(self):
        return(self.gdict)

graph_ele = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

dis = graph(graph_ele)

print(dis.vertex())
print(dis.edges())
dis.add_edge(("a","e"))
dis.add_edge(("a","f"))
print(dis.edges())
pprint.pprint(dis.print_gdict())

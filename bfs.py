import collections
def bfs(graph,start):

    visited = set([start])
    queue = collections.deque([start])

    while queue:
        item = queue.popleft()
        print(item)
        for i in graph[item]:
            if i not in visited:
                visited.add(i)
                queue.append(i)



def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for i in graph[start]:
        if i not in visited:
            visited.add(i)
            dfs(graph,i,visited)

graph = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                } 


bfs(graph,"a")
print(" ")
dfs(graph,"a")

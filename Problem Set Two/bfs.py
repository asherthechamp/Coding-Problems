# Implements breadth first search

def bfs(s, adj):
    level = {s: 0}
    parent = {s: None}
    i = 1
    print(s)
    frontier = [s]
    while(frontier):
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
                    print (v)
        frontier = next
        i += 1

adj = {"s": ["a", "x"],
       "a": ["z"],
       "x": ["s", "d", "c"],
       "d": ["x", "c", "f"],
       "c": ["d", "x", "f", "v"],
       "f": ["d", "c", "v"],
       "v": ["f", "c"],
       "z": []}
s = "s"

bfs(s, adj)


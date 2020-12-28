# Implements Depth First Search

def dfs(adj, s, parent, node, answer, count):
    if parent == {}:
        parent[s]: None
    if s == node and count > 0:
        return True
    for v in adj[s]:
        count += 1
        if v not in parent:
            parent[v] = s
            answer = answer or dfs(adj, v, parent, node, answer, count)
    return answer

def dfs_check_all(v, adj, answer, count):
    parent = {}
    for s in v:
        if s not in parent:
            parent[s] = None
            answer = answer or dfs(adj, s, parent, s, answer, count)
    return answer

adj = {"s": ["a", "x"],
       "a": ["z"],
       "x": ["s", "d", "c"],
       "d": ["x", "c", "f"],
       "c": ["d", "x", "f", "v"],
       "f": ["d", "c", "v"],
       "v": ["f", "c"],
       "z": []}

v = {"s", "a", "x", "d", "c", "f", "v", "z"}

s = "s"
f = "f"
ans_init = False
# print(dfs(adj, s, {}, f, ans_init, 0))
print(dfs_check_all(v, adj, False, 0))

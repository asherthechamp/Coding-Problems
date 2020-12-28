def find_cycle(graph):
    for node in graph:
        if (node[0] == check(node, {})):
            return True
    return False

def check(node, return_node):
    if(return_node != node):
        for n in graph[node]:
            return_node = n
            check(n, return_node)
    return return_node

graph = {
  'a': {'a2', 'a3' },
  'b': {'b2', 'a'},
  'c': {},
   'a2': {'b', 'a'},
    'a3': {},
    'b2': {}
}

print(find_cycle(graph))
# False
graph['b'] = graph
print(find_cycle(graph))
# True
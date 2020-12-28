# Checks if a graph contains cycle or not

def isCyclicUtil(self, v, visited, parent):
    # Mark current node as visited
    visited[v] = True

    # Recur for all the vertices adjacent
    # for this vertex
    for i in self.graph[v]:
        # If an adjacent is not visited,
        # then recur for that adjacent
        if visited[i] == False:
            if self.isCyclicUtil(i, visited, v) == True:
                return True

        # If an adjacent is visited and not
        # parent of current vertex, then there
        # is a cycle.
        elif i != parent:
            return True

    return False

graph = {
  'a': {'a2', 'a3' },
  'b': {'b2', 'a'},
  'c': {},
   'a2': {'b', 'a'},
    'a3': {},
    'b2': {}
}

print(isCyclicUtil(graph))
# False
graph['b'] = graph
print(isCyclicUtil(graph))
# True
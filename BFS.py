# BFS requires 2 Queues
# One remembers already visited nodes.
# Another memorizes nodes to visit.

def bfs(graph, start):
    visited = list()
    need_visit = list()
    
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if not node in visited:
            for dest in graph[node]:
                if not dest in visited:
                    need_visit.append(dest)
            visited.append(node)
    return visited

if __name__ == "__main__":

    graph = dict()

    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'G', 'H', 'I']
    graph['D'] = ['B', 'E', 'F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C', 'J']
    graph['J'] = ['I']

    '''
            A       
           / \
          B   C
         /   /|\
        D   G H I
       / \      |
      E   F     J
    
    BFS should return
    B, C
    D, G, H, I
    E, F, J
    '''
    start = "A"
    print(bfs(graph, start))


    

'''

if start in visited:
        return
    
    if start in graph:
        for loc in graph[start]:
            need_visit.append(loc)
        visited.append(start)

'''
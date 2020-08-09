# DFS requires 1 Stack & 1 Queue
# Stack stores up nodes to visit.
# Queue memorizes already visited nodes.

def dfs(graph, start):
    visited = list()
    need_visit = list()
    
    need_visit.append(start)
    
    while need_visit:
        node = need_visit.pop()
        if not node in visited:
            need_visit.extend(graph[node])
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
    
    DFS should return
    A, C, I, J, H, G, B, D, F, E
    '''
    start = "A"
    print(dfs(graph, start))

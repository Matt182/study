"""
Exercise 1
"""
EX_GRAPH0 = {0:set([1,2]),1:set([]),2:set([])}
EX_GRAPH1 = {0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([])}
EX_GRAPH2 = {0:set([1,4,5]),1:set([2,6]),2:set([3,7]),3:set([7]),4:set([1]),5:set([2]),6:set([]),7:set([3]),8:set([1,2]),9:set([0,4,5,6,7,3])}

def compute_in_degrees(digraph):
    """
    compute indegs for each node
    """
    res = []
    result = {}
    for val in digraph.values():
        res += list(val)
    for node in digraph:
        result[node] = res.count(node)
    return result

def compute_in_degrees(digraph):
    """
    compute indegs foe each node
    """
    result = {}
    for node in digraph:
        result[node] = 0
        res = 0
        for val in digraph.values():
            if node in val:
                res += 1
        result[node] = res
    return result
        
def in_degree_distribution(digraph):
    """
    compure unnormalize distribution
    means that all values are ints not floats
    """
    indeg = compute_in_degrees(digraph)
    result = {}
    for val in indeg.values():
        result[val] = indeg.values().count(val)
    return result

print in_degree_distribution(EX_GRAPH0)

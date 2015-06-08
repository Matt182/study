"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2

# Set timeout for CodeSkulptor if necessary
import codeskulptor
codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

def compute_in_degrees(digraph):
    result = {}
    res = []
    for val in digraph:
        result[val] = 0
    for node in digraph.values():
        for edge in node:
            result[edge] += 1
    return result

def in_degree_distribution(digraph):
    """
    compure unnormalize distribution
    means that all values are ints not floats
    """
    length = len(digraph)
    indeg = compute_in_degrees(digraph)
    vals = indeg.values()
    setlist = set(vals)
    result = {}
    for i in setlist:
        result[i] = 0
    for i in setlist:
        result[i] = vals.count(i)
    return result

citation_graph = load_graph(CITATION_URL)
print in_degree_distribution(citation_graph)

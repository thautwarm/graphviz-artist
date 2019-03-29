import graphviz_artist as ga

# make a graph
g = ga.Graph()

# make nodes
n1 = g.new()
n2 = g.new()
n3 = g.new()

# (>), (==) and (<) could edges for graphs.
# n2 > n3 / n3 < n2 : there is an edge n2 -> n3
# (==) will be introduced later, as it's only meaningful to directed edges.
_ = n1 > n2 > n3 > n1

g.g.save()
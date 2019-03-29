import graphviz_artist as ga

# use attr module to see which Graphviz Attributes
# could be auto-completed.
import graphviz_artist.attr as attr

# for some reason, the name of keyword arg has no actual semantics,
# but the value does:
#   ga.Graph(kw=attr.XXX) == ga.Graph(_=XXX) == ga.Graph(x=XXX)
g = ga.Graph(attr.HorizontalGraph)

# `attr.Shape("<name>")` to specify the shape of nodes.
n1 = g.new(attr.Label('hey'), attr.Shape.diamond)
n2 = g.new(attr.Label('hey'), attr.Shape.hexagon)
n3 = g.new(attr.Label('you'), attr.Shape.star)

# `attr.Directed()` makes a directed edge.
directed = attr.Directed()

# `attr.Label` to specify the text that edges display
edge_label = attr.Label("passed_here")

# `attr.Penwidth` to decide the width of edge glyph.
edge_size = attr.Penwidth(2.)

# in `a < b[b_to_c_attrs...] > c`, the edge `b -> c` will have attribute `b_to_c_attrs`.
_ = n3[directed, edge_label, edge_size] > n1[directed] == n2 > n3

g.save()

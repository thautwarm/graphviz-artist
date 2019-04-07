import graphviz_artist as ga

import graphviz_artist.attr as attr

g = ga.Graph()
n1 = g.new()
n2 = g.new()
n1.update(attr.Label("Hey"))
_ = n1[attr.Label("ok")] == n2

g.save()

assert """digraph {
	0
	1
	0 [label=Hey]
	0 -> 1 [label=ok dir=none]
	1 -> 0 [label=ok dir=none]
}""" == str(g.g)
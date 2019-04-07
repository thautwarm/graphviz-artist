import graphviz_artist as ga

import graphviz_artist.attr as attr

g = ga.Graph()
n1 = g.new()
n2 = g.new()
n3 = g.new()

_ = n1 > n2[attr.Label("woundn't work")]
_ = n1 < n2[attr.Label("woundn't work")]
_ = n3 == n2[attr.Label("woundn't work")]

g.update(attrs=(attr.HorizontalGraph, ))

g.save()


assert """digraph {
	graph [rankdir=LR]
	0
	1
	2
	0 -> 1 [dir=none]
	1 -> 0 [dir=none]
	2 -> 1 [dir=none]
	1 -> 2 [dir=none]
}""" == str(g.g)
import  graphviz_artist as ga
import  graphviz_artist.attr as attr

g = ga.Graph()
Deep = g.new(attr.Direction(), attr.Label('hey'))
Dark = g.new(attr.Direction(), attr.Label('hey'))
Fantasy = g.new(attr.Direction(), attr.Label('you'))
Deep > Dark > Fantasy
g.view()




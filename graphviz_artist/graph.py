from graphviz import Digraph as _Digraph, Graph as _Graph
from graphviz.dot import Dot as _Dot
from .attr import *
from typing import *
import operator


class Graph(object):
    def __init__(self, g=None, directed=True):  # type: (_Dot, bool) -> None
        """
        g: can be `graphviz.Digraph` or `graphviz.Graph`.
        directed: denote if this graph is directed.
        """
        g = g or (_Digraph if directed else _Graph)()  # type: _Dot
        self.g = g  # type: _Dot

    def new(self, *attrs):  # type: (*Attr) -> Node
        node = Node(self, attrs)
        node.name = str(id(node))
        node.update()
        return node

    def view(self, *args, **kwargs):
        return self.g.view(*args, **kwargs)

class By:
    def __init__(self, node, attrs):  # type: (Node, Tuple[Attr, ...]) -> None
        self.node = node
        self.attrs = attrs

    def _op(self, op, other):
        return op(self.node, other, *self.attrs)

    def __eq__(self, other):  # type: (Node) -> bool
        return self._op(operator.eq, other)

    def __gt__(self, other):  # type: (Node) -> bool
        return self._op(operator.gt, other)

    def __lt__(self, other):  # type: (Node) -> bool
        return self._op(operator.lt, other)


class Node(object):
    def __init__(self, g, attrs):
        # type: (Graph, Tuple[Attr, ...]) -> None
        self.attrs = set(attrs)
        self.name = None
        self.g = g

    def update(self, *attrs):  # type: (*Attr) -> Node
        if attrs:
            t = type
            new_attrs = {t(attr): attr for attr in self.attrs}
            for new_attr in attrs:
                new_attrs[t(new_attr)] = new_attr
            self.attrs = set(new_attrs.values())

        config = {}
        for each in self.attrs:
            each.dump_(config)
        self.g.g.node(self.name, **config)
        return self

    def __getitem__(self, attrs):  # type: (Union[Attr, Tuple[Attr]]) -> By
        if not isinstance(attrs, tuple):
            attrs = (attrs, )

        return By(self, attrs)

    def __gt__(self, other,
               attrs=()):  # type: (Node, Tuple[Attr, ...]) ->  bool
        left = self.name
        right = other.name
        config = {}
        for each in attrs:
            each.dump_(config)
        self.g.g.edge(left, right, **config)
        return True

    def __lt__(self, other,
               attrs=()):  # type: ('Node', Tuple[Attr, ...]) ->  bool
        return other.__gt__(self, ())

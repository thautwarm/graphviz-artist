from graphviz import Digraph as _Digraph
from graphviz.dot import Dot as _Dot
from .attr import *
from typing import *

__all__ = ['Graph', 'By', 'Node']


class Graph(object):
    def __init__(self, *attrs, **kwargs):  # type: (*Attr, **object) -> None
        """
        e.g.:
            # all edges are default to be directed
            >> g = Graph(directed=True)

            # set custom dot graph, should be typed `graphviz.Digraph`
            >> g = Graph(dot=graphviz.Digraph(...)
        """
        directed = kwargs.get('directed', False)
        g = kwargs.get('dot')

        g = g or _Digraph()  # type: _Dot
        self.g = g  # type: _Dot

        self.count = {}
        self.attrs = attrs

        self.default_directed = Directed(directed)  # type: Attr

    def update(self, attrs=()):  # type: (*Attr) -> Graph
        if attrs:
            self.attrs = _merge_attr(self.attrs, attrs)
        config = {}
        for each in self.attrs:
            each.dump_(config)
        self.g.graph_attr.update(config)
        return self

    def new(self, *attrs, **kwds):  # type: (*Attr, **Attr) -> Node
        attrs = attrs + tuple(kwds.values())
        node = Node(self, attrs)
        count = self.count[node.token] = len(self.count)
        node.name = str(count)
        node.update()
        return node

    def view(self, *args, **kwargs):
        self.update()
        return self.g.view(*args, **kwargs)

    def save(self, filename=None, directory=None):
        self.update()
        return self.g.save(filename, directory)


class By:
    def __init__(self, node, attrs):  # type: (Node, Tuple[Attr, ...]) -> None
        self.node = node
        self.attrs = attrs

    def _op(self, op, other):
        if isinstance(other, By):
            other = other.node
        return op(self.node, other, self.attrs)

    def __eq__(self, other):  # type: (Union[Node, By]) -> bool

        return self._op(lambda a, b, attrs: a.__eq__(b, attrs), other)

    def __gt__(self, other):  # type: (Union[Node, By]) -> bool
        return self._op(lambda a, b, attrs: a.__gt__(b, attrs), other)

    def __lt__(self, other):  # type: (Union[Node, By]) -> bool
        return self._op(lambda a, b, attrs: a.__lt__(b, attrs), other)


class Node(object):
    def __init__(self, g, attrs):
        # type: (Graph, Tuple[Attr, ...]) -> None
        self.attrs = attrs
        self.name = None
        self.g = g
        self.token = object()

    def update(self, *attrs):  # type: (*Attr) -> Node

        if attrs:
            self.attrs = _merge_attr(self.attrs, attrs)

        config = {}
        for each in self.attrs:
            each.dump_(config)
        self.g.g.node(self.name, **config)
        return self

    def __getitem__(self,
                    attrs):  # type: (Union[Attr, Tuple[Attr, ...]]) -> By
        if not isinstance(attrs, tuple):
            attrs = (attrs, )

        return By(self, attrs)

    def __eq__(
            self, other,
            attrs=()):  # type: (Union['Node', By], Tuple[Attr, ...]) -> bool

        if isinstance(other, By):
            other = other.node

        self.__gt__(other, attrs)
        other.__gt__(self, attrs)
        return True

    def __gt__(self, other,
               attrs=()):  # type: (Union[Node, By], Tuple[Attr, ...]) ->  bool
        if isinstance(other, By):
            other = other.node

        left = self.name
        right = other.name

        config = {}
        self.g.default_directed.dump_(config)

        for each in attrs:
            each.dump_(config)
        self.g.g.edge(left, right, **config)
        return True

    def __lt__(
            self, other,
            attrs=()):  # type: (Union['Node', By], Tuple[Attr, ...]) ->  bool
        if isinstance(other, By):
            other = other.node

        return other.__gt__(self, attrs)


def _merge_attr(
        attrs1, attrs2
):  # type: (Tuple[Attr, ...], Tuple[Attr, ...]) -> Tuple[Attr, ...]
    if not attrs2:
        return attrs1
    if not attrs1:
        return attrs2
    t = type
    new_attrs = {t(attr): attr for attr in attrs1}
    for new_attr in attrs2:
        new_attrs[t(new_attr)] = new_attr
    return tuple(new_attrs.values())

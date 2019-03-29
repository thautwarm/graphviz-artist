import numbers


class _ClassProperty(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, _, instance_cls):
        return self.method(instance_cls)


def thunk_class_property(f):
    return _ClassProperty(lambda cls: f())


class Attr(object):
    __slots__ = ('value', )

    def __init__(self, value):  # type: (str) -> None
        self.value = value

    def dump_(self, config):
        """
        default configuration dumping method.
        """
        config[self.__class__.__name__.lower()] = self.value
        return config

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, str(self.value))


class Label(Attr):
    """
    The text to be put on the surface of a node.
    """
    pass


class Ratio(Attr):
    pass


class Width(Attr):
    def __init__(self, num):  # type: (numbers.Number) -> None
        Attr.__init__(self, str(num))


class Height(Attr):
    def __init__(self, num):  # type: (numbers.Number) -> None
        Attr.__init__(self, str(num))


class FixedSize(Attr):
    def __init__(self):
        Attr.__init__(self, 'true')


class Penwidth(Attr):
    def __init__(self, num):  # type: (float) -> None
        Attr.__init__(self, str(num))


class Directed(Attr):
    """
    check https://www.graphviz.org/doc/info/attrs.html#k:dirType
    to see available options
    """

    def __init__(self, is_directed=True):
        Attr.__init__(self, 'forward' if is_directed else 'none')

    def dump_(self, config):
        config['dir'] = self.value
        return config


class Rankdir(Attr):
    """
    Sets direction of graph layout.
    """
    LR = thunk_class_property(lambda: Rankdir('LR'))


HorizontalGraph = Rankdir.LR


class Shape(Attr):
    """ 
    check following link to see available shape options.
    https://www.graphviz.org/doc/info/shapes.html
    """

    box = thunk_class_property(lambda: Shape('box'))  # type: Shape
    polygon = thunk_class_property(lambda: Shape('polygon'))  # type: Shape
    ellipse = thunk_class_property(lambda: Shape('ellipse'))  # type: Shape

    oval = thunk_class_property(lambda: Shape("oval"))  # type: Shape
    circle = thunk_class_property(lambda: Shape("circle"))  # type: Shape
    point = thunk_class_property(lambda: Shape("point"))  # type: Shape
    egg = thunk_class_property(lambda: Shape("egg"))  # type: Shape
    triangle = thunk_class_property(lambda: Shape("triangle"))  # type: Shape
    diamond = thunk_class_property(lambda: Shape("diamond"))  # type: Shape
    trapezium = thunk_class_property(lambda: Shape("trapezium"))  # type: Shape
    parallelogram = thunk_class_property(lambda: Shape("parallelogram")
                                         )  # type: Shape
    star = thunk_class_property(lambda: Shape("star"))  # type: Shape
    pentagon = thunk_class_property(lambda: Shape("pentagon"))  # type: Shape
    hexagon = thunk_class_property(lambda: Shape("hexagon"))  # type: Shape
    cds = thunk_class_property(lambda: Shape("cds"))  # type: Shape
    box3d = thunk_class_property(lambda: Shape("box3d"))  # type: Shape


class MinLen(Attr):
    def __init__(self, num):  # type: (float) -> None
        Attr.__init__(self, str(num))


class LabelFloat(Attr):
    def __init__(self):
        Attr.__init__(self, 'true')


class LabelFontSize(Attr):
    def __init__(self, num):  # type: (numbers.Number) -> None
        Attr.__init__(self, str(num))


class XLabel(Attr):
    pass

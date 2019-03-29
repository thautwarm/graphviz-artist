import numbers


class _ClassProperty:
    def __init__(self, method):
        self.method = method

    def __get__(self, _, instance_cls):
        return self.method(instance_cls)


class Attr(object):
    __slots__ = ('value', )

    def __init__(self, value):
        self.value = value

    def dump_(self, config):
        """
        default configuration dumping method.
        """
        config[self.__class__.__name__.lower()] = self.value
        return config


class Label(Attr):
    """
    check https://www.graphviz.org/doc/info/attrs.html#k:dirType
    to get more info.
    """
    pass


class Ratio(Attr):
    pass


class Width(Attr):
    def __init__(self, num):  # type: (numbers.Number) -> None
        Attr.__init__(self, num)


class Height(Attr):
    def __init__(self, num):  # type: (numbers.Number) -> None
        Attr.__init__(self, num)


class FixedSize(Attr):
    def __init__(self):
        Attr.__init__(self, 'true')


class Direction(Attr):
    """
    check https://www.graphviz.org/doc/info/attrs.html#k:dirType
    to see available options
    """

    def __init__(self):
        Attr.__init__(self, 'forward')

    def dump_(self, config):
        config['dirType'] = self.value


class Shape(Attr):
    """ 
    check following link to see available shape options.
    https://www.graphviz.org/doc/info/shapes.html
    """

    @_ClassProperty
    def f(cls):
        return 1

print(Shape.f)

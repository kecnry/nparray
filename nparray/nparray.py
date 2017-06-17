import numpy as np
from collections import OrderedDict

class Array(object):
    def __init__(self, *args):
        """
        all subclasses MUST parse args and send in as tuples via super so that
        order is preserved.

        For example:
        def __init__(self, start, stop, step):
            super(MyClass, self).__init__(('start', start), ('stop', stop), ('step', step))

        All of these "descriptors" will then be available to get and set via
        their attribute names
        """
        self._descriptors = OrderedDict()

        for item in args:
            self._descriptors[item[0]] = item[1]

    @property
    def array(self):
        """
        all subclasses MUST define a array property method which returns a
        np.ndarray object
        """
        raise NotImplementedError

    def __getattr__(self, name):
        """
        for anything that isn't overriden here, call the method on the array itself
        """
        # print "*** __getattr__", name
        if name in ['_descriptors']:
            # then we need to actually get the attribute
            return super(Array, self).__getattr__(name)
            # return self._descriptors
        elif name in self._descriptors.keys():
            # then get the item in the dictionary
            return self._descriptors.get(name)
        else:
            # then fallback on the underlying array object
            return getattr(self.array, name)

    def __setattr__(self, name, value):
        """
        """
        # print "*** __setattr__", name, value
        if name in ['_descriptors']:
            return super(Array, self).__setattr__(name, value)
        elif name in self._descriptors.keys():
            self._descriptors[name] = value
        else:
            return setattr(self.array, name, value)

    def __getitem__(self, index):
        return self.array.__getitem__(index)

    def __setitem__(self, index, value):
        # TODO: setting an item would ruin the whole concept... but we could
        # maybe change the object to a plain array or provide a mask that
        # overrides values?
        raise NotImplementedError("setting by index not yet implemented")


    # def __dir__(self):
    #     """
    #     override the dir() functionality to also include all of the
    #     methods/attributes of self.array
    #     """

    def __repr__(self):
        descriptors = " ".join(["{}={}".format(k,v) for k,v in self._descriptors.items()])
        return "<{} {}>".format(self.__class__.__name__.lower(), descriptors)


class Arange(Array):
    def __init__(self, start, stop, step):
        super(Arange, self).__init__(('start', start), ('stop', stop), ('step', step))

    @property
    def array(self):
        return np.arange(self.start, self.stop, self.step)

    def to_linspace(self):
        """
        convert from arange to linspace
        """
        num = (self.stop-self.start)/(self.step)
        return Linspace(self.start, self.stop-self.step, num)

class Linspace(Array):
    def __init__(self, start, stop, num):
        super(Linspace, self).__init__(('start', start), ('stop', stop), ('num', num))

    @property
    def array(self):
        return np.linspace(self.start, self.stop, self.num)

    def to_arange(self):
        """
        convert from linspace to arange
        """
        step = (self.stop-self.start)/(self.num-1)
        return Arange(self.start, self.stop+step, step)

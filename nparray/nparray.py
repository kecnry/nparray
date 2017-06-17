import numpy as np
from collections import OrderedDict

################## VALIDATORS ###################

# these all must accept a single value and return a boolean if it matches the condition
# the docstring is used as the error message if the test fails

def is_float(value):
    """must be a float"""
    return isinstance(value, float) or isinstance(value, int)

def is_int(value):
    """must be an integer"""
    return isinstance(value, int)

def is_int_positive(value):
    """must be a positive integer"""
    return isinstance(value, int) and value > 0

def is_valid_shape(value):
    """must be a positive integer or a tuple/list of positive integers"""
    if is_int_positive(value):
        return True
    elif isinstance(value, tuple) or isinstance(value, list):
        for v in value:
            if not is_int_positive(v):
                return False
        return True
    else:
        return False


############# WRAPPERS ###################

class Array(object):
    def __init__(self, *args):
        """
        all subclasses MUST parse args and send in as tuples via super so that
        order is preserved.

        For example:
        def __init__(self, start, stop, step):
            super(MyClass, self).__init__(('start', start, is_float), ('stop', stop, is_float), ('step', step, is_float))

        All of these "descriptors" will then be available to get and set via
        their attribute names
        """
        self._descriptors = OrderedDict()
        self._validators = OrderedDict()

        for item in args:
            if item[2](item[1]):
                self._descriptors[item[0]] = item[1]
            else:
                raise ValueError("{} {}".format(item[0], item[2].__doc__))
            self._validators[item[0]] = item[2]

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
        if name in ['_descriptors', '_validators']:
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
        if name in ['_descriptors', '_validators']:
            return super(Array, self).__setattr__(name, value)
        elif name in self._descriptors.keys():
            validator = self._validators[name]
            if validator(value):
                self._descriptors[name] = value
            else:
                raise ValueError("{} {}".format(name, validator.__doc__))
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
        super(Arange, self).__init__(('start', start, is_float),
                                     ('stop', stop, is_float),
                                     ('step', step, is_float))

    @property
    def array(self):
        return np.arange(self.start, self.stop, self.step)

    def to_linspace(self):
        """
        convert from arange to linspace
        """
        num = int((self.stop-self.start)/(self.step))
        return Linspace(self.start, self.stop-self.step, num)

class Linspace(Array):
    def __init__(self, start, stop, num):
        super(Linspace, self).__init__(('start', start, is_float),
                                       ('stop', stop, is_float),
                                       ('num', num, is_int_positive))

    @property
    def array(self):
        return np.linspace(self.start, self.stop, self.num)

    def to_arange(self):
        """
        convert from linspace to arange
        """
        step = (self.stop-self.start)/(self.num-1)
        return Arange(self.start, self.stop+step, step)

class Zeros(Array):
    def __init__(self, shape):
        super(Zeros, self).__init__(('shape', shape, is_valid_shape))

    @property
    def array(self):
        return np.zeros(self.shape)

    def to_linspace(self):
        if hasattr(self.shape, '__len__'):
            raise NotImplementedError("can only convert flat Zeros arrays to linspace")
        return Linspace(0, 0, self.shape)

class Ones(Array):
    def __init__(self, shape):
        super(Ones, self).__init__(('shape', shape, is_valid_shape))

    @property
    def array(self):
        return np.ones(self.shape)

    def to_linspace(self):
        if hasattr(self.shape, '__len__'):
            raise NotImplementedError("can only convert flat Ones arrays to linspace")
        return Linspace(1, 1, self.shape)

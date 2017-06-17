import numpy as np
from collections import OrderedDict

try:
    from astropy import units
except ImportError:
    _has_astropy = False
else:
    _has_astropy = True

################## VALIDATORS ###################

# these all must accept a single value and return a boolean if it matches the condition
# the docstring is used as the error message if the test fails

def is_bool(value):
    """must be boolean"""
    return isinstance(value, bool)

def is_float(value):
    """must be a float"""
    return isinstance(value, float) or isinstance(value, int)

def is_int(value):
    """must be an integer"""
    return isinstance(value, int)

def is_int_positive(value):
    """must be a positive integer"""
    return isinstance(value, int) and value > 0

def is_int_positive_or_none(value):
    """must be a postive integer or None"""
    return is_int_positive or value is None

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

def is_iterable(value):
    """must be an iterable (list, array, tuple)"""
    return isinstance(value, np.ndarray) or isinstance(value, list) or isinstance(value, tuple)


############# WRAPPERS ###################

class ArrayWrapper(object):
    """
    ArrayWrapper should be subclassed by any type of array creation classes
    and the corresponding function should be added to __init__.py.  Any subclass
    MUST define the following:

    __init__ (see docs below)
    array (@property - see docs below)
    __math__(self, operator, other)
    """
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

    # @property
    # def __class__(self):
    #     """
    #     override the class so that isinstance(object, np.ndarray) returns True
    #
    #     NOTE: this is really hacky
    #     """
    #     return np.ndarray

    def __getattr__(self, name):
        """
        for anything that isn't overriden here, call the method on the array itself
        """
        # print "*** __getattr__", name
        if name in ['_descriptors', '_validators']:
            # then we need to actually get the attribute
            return super(ArrayWrapper, self).__getattr__(name)
            # return self._descriptors
        elif name in self._descriptors.keys():
            # then get the item in the dictionary
            return self._descriptors.get(name)
        # elif hasattr(self, name):
            # return super(ArrayWrapper, self).__getattr__(name)
        elif hasattr(self.array, name):
            # then fallback on the underlying array object
            return getattr(self.array, name)
        else:
            raise AttributeError("neither '{}' or '{}' have attribute '{}'".format(self.__class__.__name__.lower(), 'numpy.ndarray', name))

    def __setattr__(self, name, value):
        """
        """
        # print "*** __setattr__", name, value
        if name in ['_descriptors', '_validators', '__class__']:
            return super(ArrayWrapper, self).__setattr__(name, value)
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
        """
        setting an item in the array needs to fallback on the Array class
        """
        arrayvalue = self.array
        arrayvalue.__setitem__(index, value)
        self._convert_to_array(arrayvalue)


    # def __dir__(self):
    #     """
    #     override the dir() functionality to also include all of the
    #     methods/attributes of self.array
    #     """

    def __repr__(self):
        descriptors = " ".join(["{}={}".format(k,v) for k,v in self._descriptors.items()])
        return "<{} {}>".format(self.__class__.__name__.lower(), descriptors)

    def __str__(self):
        return self.array.__str__()

    def __copy__(self):
        return self.__class__(**self._descriptors)

    def __deepcopy__(self):
        return self.__copy__(self)

    def copy(self):
        return self.__copy__()

    def to_array(self):
        return Array(self.array)

    def _convert_to_array(self, value=None):
        if value is None:
            value = self.array
        self.__class__ = Array
        self.__init__(value)

    def __add__(self, other):
        return self.__math__('__add__', other)

    def __radd__(self, other):
        return self.__math__('__radd__', other)

    def __sub__(self, other):
        return self.__math__('__sub__', other)

    def __rsub__(self, other):
        return self.__math__('__rsub__', other)

    def __mul__(self, other):
        if _has_astropy and (isinstance(other, units.Unit) or
                             isinstance(other, units.IrreducibleUnit) or
                             isinstance(other, units.CompositeUnit)):
            # TODO: consider faking the Quantity object as well so that
            # quantity.descriptor can be changed on the fly as well
            # see issue #12
            return units.Quantity(self, other)
        else:
            return self.__math__('__mul__', other)

    def __rmul__(self, other):
        return self.__math__('__rmul__', other)

    def __div__(self, other):
        return self.__math__('__div__', other)

    def __rdiv__(self, other):
        return self.__math__('__rdiv__', other)

    def __pow__(self, other):
        return self.__math__('__pow__', other)

    def __rpow__(self, other):
        return Array(self.array.__rpow__(other))

    def __abs__(self):
        return Array(abs(self.array))

    def __len__(self):
        return len(self.array)

    def __comparison__(self, operator, other):
        """
        determine comparisons based on the underyling arrays
        """
        return getattr(self.array, operator)(other)

    def __eq__(self, other):
        return self.__comparison__('__eq__', other)

    def __ne__(self, other):
        return self.__comparison__('__ne__', other)

    def __lt__(self, other):
        return self.__comparison__('__lt__', other)

    def __lte__(self, other):
        return self.__comparison__('__le__', other)

    def __gt__(self, other):
        return self.__comparison__('__gt__', other)

    def __ge__(self, other):
        return self.__comparison__('__ge__', other)

    def __contains__(self, other):
        return self.__comparison__('__contains__', other)

class Array(ArrayWrapper):
    def __init__(self, value):
        super(Array, self).__init__(('value', value, is_iterable))

    @property
    def array(self):
        return np.array(self.value)

    def __math__(self, operator, other):
        return Array(getattr(np.asarray(self.value), operator)(other))

    def __setitem__(self, index, value):
        """
        for Arrays, we simply edit the underlying numpy array/list/tuple
        """
        # TODO: will this cause issues if value is a tuple? what is the expected behavior
        self.value.__setitem__(index, value)

class Arange(ArrayWrapper):
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

    def to_array(self):
        """
        convert from arange to array
        """
        return Array(self.array)

    def __math__(self, operator, other):
        if isinstance(other, float) or isinstance(other, int):
            return Arange(getattr(self.start, operator)(other), getattr(self.stop, operator)(other), self.step)
        elif isinstance(other, np.ndarray) or isinstance(other, list) or isinstance(other, tuple):
            value = getattr(self.array, operator)(other)
            return Array(value)
        elif isinstance(other, ArrayWrapper):
            value = getattr(self.array, operator)(other.array)
            return Array(value)
        else:
            raise ValueError("{} not supported with type {}".format(operator, type(other)))

class Linspace(ArrayWrapper):
    def __init__(self, start, stop, num, endpoint=True):
        super(Linspace, self).__init__(('start', start, is_float),
                                       ('stop', stop, is_float),
                                       ('num', num, is_int_positive),
                                       ('endpoint', endpoint, is_bool))

    @property
    def array(self):
        return np.linspace(self.start, self.stop, self.num, self.endpoint)

    def to_arange(self):
        """
        convert from linspace to arange
        """
        arr, step = np.linspace(self.start, self.stop, self.num, self.endpoint, retstep=True)
        return Arange(self.start, self.stop+step, step)

    def __math__(self, operator, other):
        if isinstance(other, float) or isinstance(other, int):
            return Linspace(getattr(self.start, operator)(other), getattr(self.stop, operator)(other), self.num)
        elif isinstance(other, np.ndarray) or isinstance(other, list) or isinstance(other, tuple):
            value = getattr(self.array, operator)(other)
            return Array(value)
        elif isinstance(other, ArrayWrapper):
            value = getattr(self.array, operator)(other.array)
            return Array(value)
        else:
            raise ValueError("{} not supported with type {}".format(operator, type(other)))

class Logspace(ArrayWrapper):
    def __init__(self, start, stop, num, endpoint=True, base=10.0):
        super(Logspace, self).__init__(('start', start, is_float),
                                       ('stop', stop, is_float),
                                       ('num', num, is_int_positive),
                                       ('endpoint', endpoint, is_bool),
                                       ('base', base, is_float))

    @property
    def array(self):
        return np.logspace(self.start, self.stop, self.num, self.endpoint, self.base)

    def _math__(self, operator, other):
        if isinstance(other, float) or isinstance(other, int):
            return Logspace(getattr(self.start, operator)(other), getattr(self.stop, operator)(other), self.num)
        elif isinstance(other, np.ndarray) or isinstance(other, list) or isinstance(other, tuple):
            value = getattr(self.array, operator)(other)
            return Array(value)
        elif isinstance(other, ArrayWrapper):
            value = getattr(self.array, operator)(other.array)
            return Array(value)
        else:
            raise ValueError("{} not supported with type {}".format(operator, type(other)))


class Geomspace(ArrayWrapper):
    def __init__(self, start, stop, num, endpoint=True):
        super(Geomspace, self).__init__(('start', start, is_float),
                                       ('stop', stop, is_float),
                                       ('num', num, is_int_positive),
                                       ('endpoint', endpoint, is_bool))

    @property
    def array(self):
        return np.geomspace(self.start, self.stop, self.num, self.endpoint)

    def __math__(self, operator, other):
        if isinstance(other, float) or isinstance(other, int):
            return Geomspace(getattr(self.start, operator)(other), getattr(self.stop, operator)(other), self.num)
        elif isinstance(other, np.ndarray) or isinstance(other, list) or isinstance(other, tuple):
            value = getattr(self.array, operator)(other)
            return Array(value)
        elif isinstance(other, ArrayWrapper):
            value = getattr(self.array, operator)(other.array)
            return Array(value)
        else:
            raise ValueError("{} not supported with type {}".format(operator, type(other)))

class Full(ArrayWrapper):
    def __init__(self, shape, fill_value):
        super(Full, self).__init__(('shape', shape, is_valid_shape),
                                    ('fill_value', fill_value, is_float))

    @property
    def array(self):
        return np.full(self.shape, self.fill_value)

    def to_linspace(self):
        if hasattr(self.shape, '__len__'):
            raise NotImplementedError("can only convert flat Full arrays to linspace")
        return Linspace(self.fill_value, self.fill_value, self.shape)

    def __math__(self, operator, other):
        if isinstance(other, float) or isinstance(other, int):
            return Full(self.shape, getattr(self.fill_value, operator)(other))
        elif isinstance(other, np.ndarray) or isinstance(other, list) or isinstance(other, tuple):
            value = getattr(self.array, operator)(other)
            return Array(value)
        elif isinstance(other, Full) or isinstance(other, Zeros) or isinstance(other, Ones):
            if self.shape==other.shape:
                if isinstance(other, Full):
                    other_fill_value = other,fill_value
                elif isinstance(other, Zeros):
                    other_fill_value = 0.0
                elif isinstance(other, Ones):
                    other_fill_value = 1.0
                return Full(self.shape, getattr(self.fill_value, operator)(other_fill_value))
            else:
                raise ValueError("cannot add with unmatching shapes")
        elif isinstance(other, ArrayWrapper):
            value = getattr(self.array, operator)(other.array)
            return Array(value)
        else:
            raise ValueError("{} not supported with type {}".format(operator, type(other)))


class Zeros(ArrayWrapper):
    def __init__(self, shape):
        super(Zeros, self).__init__(('shape', shape, is_valid_shape))

    @property
    def array(self):
        return np.zeros(self.shape)

    def to_full(self):
        return Full(self.shape, 0)

    def to_linspace(self):
        if hasattr(self.shape, '__len__'):
            raise NotImplementedError("can only convert flat Zeros arrays to linspace")
        return Linspace(0, 0, self.shape)

    def __math__(self, operator, other):
        if isinstance(other, float) or isinstance(other, int):
            return Full(self.shape, getattr(0.0, operator)(other))
        elif isinstance(other, np.ndarray) or isinstance(other, list) or isinstance(other, tuple):
            value = getattr(self.array, operator)(other)
            return Array(value)
        elif isinstance(other, Full) or isinstance(other, Zeros) or isinstance(other, Ones):
            if self.shape==other.shape:
                if isinstance(other, Full):
                    other_fill_value = other.fill_value
                elif isinstance(other, Zeros):
                    other_fill_value = 0.0
                elif isinstance(other, Ones):
                    other_fill_value = 1.0
                return Full(self.shape, getattr(0.0, operator)(other_fill_value))
            else:
                raise ValueError("cannot add with unmatching shapes")
        elif isinstance(other, ArrayWrapper):
            value = getattr(self.array, operator)(other.array)
            return Array(value)
        else:
            raise ValueError("{} not supported with type {}".format(operator, type(other)))

class Ones(ArrayWrapper):
    def __init__(self, shape):
        super(Ones, self).__init__(('shape', shape, is_valid_shape))

    @property
    def array(self):
        return np.ones(self.shape)

    def to_full(self):
        return Full(self.shape, 1)

    def to_linspace(self):
        if hasattr(self.shape, '__len__'):
            raise NotImplementedError("can only convert flat Ones arrays to linspace")
        return Linspace(1, 1, self.shape)

    def __math__(self, operator, other):
        if isinstance(other, float) or isinstance(other, int):
            return Full(self.shape, getattr(1.0, operator)(other))
        elif isinstance(other, np.ndarray) or isinstance(other, list) or isinstance(other, tuple):
            value = getattr(self.array, operator)(other)
            return Array(value)
        elif isinstance(other, Full) or isinstance(other, Zeros) or isinstance(other, Ones):
            if self.shape==other.shape:
                if isinstance(other, Full):
                    other_fill_value = other.fill_value
                elif isinstance(other, Zeros):
                    other_fill_value = 0.0
                elif isinstance(other, Ones):
                    other_fill_value = 1.0
                return Full(self.shape, getattr(1.0, operator)(other_fill_value))
            else:
                raise ValueError("cannot add with unmatching shapes")
        elif isinstance(other, ArrayWrapper):
            value = getattr(self.array, operator)(other.array)
            return Array(value)
        else:
            raise ValueError("{} not supported with type {}".format(operator, type(other)))

class Eye(ArrayWrapper):
    def __init__(self, M, N=None, k=0):
        super(Eye, self).__init__(('M', M, is_int_positive),
                                  ('N', N, is_int_positive_or_none),
                                  ('k', k, is_int_positive_or_none))

    @property
    def array(self):
        return np.eye(self.M, self.N, self.k)

    def __math__(self, operator, other):
        return getattr(self.to_array(), operator)(other)

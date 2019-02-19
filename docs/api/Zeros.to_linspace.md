### [Zeros](Zeros.md).to_linspace (method)


```py

def to_linspace(self)

```



Convert from [Zeros](Zeros.md) to [Linspace](Linspace.md) (only supported for flat arrays in
which `shape` is an integer, not a tuple).

```py
Linspace(0, 0, self.shape)
```

Returns
--------
* [Linspace](Linspace.md)

Raises
--------
* NotImplementedError: if the `shape` is not flat.


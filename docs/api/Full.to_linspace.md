### [Full](Full.md).to_linspace (method)


```py

def to_linspace(self)

```



Convert from [Full](Full.md) to [Linspace](Linspace.md) (only supported for flat arrays in
which `shape` is an integer, not a tuple).

```py
Linspace(self.fill_value, self.fill_value, self.shape)
```

Returns
--------
* [Linspace](Linspace.md)

Raises
--------
* NotImplementedError: if the `shape` is not flat.


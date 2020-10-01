### [Linspace](Linspace.md).to_arange (function)


```py

def to_arange(self)

```



Convert from [Linspace](Linspace.md) to [Arange](Arange.md)

```py
arr, step = np.linspace(self.start, self.stop, self.num, self.endpoint, retstep=True)
Arange(self.start, self.stop+step, step)
```

Returns
----------
* [Arange](Arange.md)


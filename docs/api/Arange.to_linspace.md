### [Arange](Arange.md).to_linspace (function)


```py

def to_linspace(self)

```



Convert from [Arange](Arange.md) to [Linspace](Linspace.md).

```py
num = int((self.stop - self.start)/self.step)
Linspace(self.start, self.stop-self.step, num)
```

Returns
-------
* [Linspace](Linspace.md)


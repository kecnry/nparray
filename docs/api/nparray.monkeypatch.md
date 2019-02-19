### [nparray](nparray.md).monkeypatch (function)


```py

def monkeypatch()

```



monkeypatch built-in numpy functions to call those provided by nparray instead.

```py
import nparray
import numpy as np

nparray.monkeypatch()
print(np.linspace(0,1,11))
```


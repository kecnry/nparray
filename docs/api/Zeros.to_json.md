### [Zeros](Zeros.md).to_json (function)


```py

def to_json(self, **kwargs)

```



Dump a representation of the nparray object to a json-formatted string.
The nparray object should then be able to be fully restored via
[nparray.from_json](nparray.from_json.md).

Arguments
-----------
* `**kwargs`: all keyword arguments are sent to json.dumps

Returns
---------
* (string): json formatted string.


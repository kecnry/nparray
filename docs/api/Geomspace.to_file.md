### [Geomspace](Geomspace.md).to_file (function)


```py

def to_file(self, filename, **kwargs)

```



Dump a representation of the nparray object to a json-formatted file.
The nparray object should then be able to be fully restored via
[nparray.from_file](nparray.from_file.md).

Arguments
-----------
* `filename` (string): path to the file to be created (will overwrite
    if already exists)
* `**kwargs`: additional keyword arguments are passed to
    json.dumps.

Returns
-----------
* (string): the filename


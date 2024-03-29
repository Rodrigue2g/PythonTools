# PythonTools [![Update Pip Import File](https://github.com/Dequavious6/PythonTools/actions/workflows/pipUpdate.yml/badge.svg)](https://github.com/Dequavious6/PythonTools/actions/workflows/pipUpdate.yml)

1. Import the [pipImport file](https://github.com/Dequavious6/PythonTools/blob/main/pipImport.py) in your python programm as follows:
```
import urllib
import httpimport
url = "https://raw.githubusercontent.com/Dequavious6/PythonTools/main"
with httpimport.remote_repo(["pipImport"], url):
    from pipImport import *
```
or 
```
import urllib
import httpimport
url = "https://raw.githubusercontent.com/Dequavious6/PythonTools/main"
with httpimport.remote_repo(["pipImport"], url):
    import pipImport as ø
```
2. Use the python tools from Designø following your needs from this list : 
    - CList() : Complex list that "ovverides" the append() method for more complex operations, reducing the amount of code you need to write.
    - CopyCatch : Check the resemblance percentage of several files (2-50). To do so, run copyCacth() in the directory of the files you want to check.

3. Run __help()__ to learn more about PythonTools

4. Make sure not to call your file __pipImport.py__ to avoid circular import issues 

&nbsp;

More informations on the [DESIGNØ Website](https://designø.com).

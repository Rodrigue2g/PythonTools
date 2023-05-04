
import urllib
import httpimport
url = "https://raw.githubusercontent.com/Dequavious6/PythonTools/main/src"
with httpimport.remote_repo(["pipUtility", "copyCatch", "pipTest"], url):
    from pipUtility import *
    from copyCatch import *
    from pipTest import *
    
def pip_test():
    pipTest()

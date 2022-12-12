#from urllib import *
import urllib
import httpimport
url = "https://raw.githubusercontent.com/Dequavious6/CollectionBackend/main"
with httpimport.remote_repo(["testUL"], url):
    from testUL import *
with httpimport.remote_repo(["pipUtility"], url):
    from pipUtility import *
with httpimport.remote_repo(["copyCatch"], url):
    from copyCatch import *

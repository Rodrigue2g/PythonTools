# Python Tools by DESIGNØ®
# This Software is copyright DESIGNØ®, all rights reserved.
# Copyright © 2022 DESIGNØ SASU.
"""
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
#
# Import Designø python tools as follow
"""
url = "https://raw.githubusercontent.com/Dequavious6/PythonTools/main"
with httpimport.remote_repo(["pipImport"], url):
    from pipImport import *
"""
#
"""
import urllib
import httpimport
url = "https://raw.githubusercontent.com/Dequavious6/PythonTools/main/src"
with httpimport.remote_repo(["pipUtility", "copyCatch", "pipTest"], url):
    from pipUtility import *
    from copyCatch import *
    from pipTest import *
""" 
#
import urllib
import httpimport
url = "https://raw.githubusercontent.com/Dequavious6/PythonTools/main/src"
doc = "https://raw.githubusercontent.com/Dequavious6/PythonTools/main/src/docs"
with httpimport.remote_repo(['docs'], doc):
    from docs import *
with httpimport.remote_repo(['pipUtility'], url):
    from pipUtility import *
with httpimport.remote_repo(['copyCatch'], url):
    from copyCatch import *
with httpimport.remote_repo(['pipTest'], url):
    from pipTest import *   
  

def help() -> None:
    print("Welcome to " + "\033[1m" + "Design" + "\033[5m" + "ø" + "\033[0m" + "\033[1m" + "Python Tools" + "\033[0m")
    print("To list the " +  "\033[1m" + "\033[3m" + "available modules" + "\033[0m" + ", use: " + "\033[95m" + "Modules().list()" + "\033[0m")
    print("To get the " + "\033[1m" + "\033[3m" + "documentation" + "\033[0m" + " of a certain module, use: " + "\033[95m" + "Modules().moduleName.docs()" + "\033[0m")
    
#__all__ = ['help']   
# 
# End of file
#

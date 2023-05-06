import sys
class Docs:
    def __init__(self):
        self.docs = {
                     "pipUtility": " Complex list that \"ovverides\" the append() method for more complex operations, reducing the amount of code you need to write.",
                     "copyCatch": "Check the resemblance percentage of several files (2-50). To do so, run copyCacth() in the directory of the files you want to check.",
                     "pipTest": "Hello World test module"
                    }
    
    def getModuleDoc(self, name) -> str:
        return self.docs.get(name, "No documentation available for this module.")
        
class Module:
    def __init__(self, name):
        self.name = name
    def docs(self):
        prPurple(f"Documentation of {self.name} module:")
        prIt(Docs().getModuleDoc(self.name))
        
class Modules:
    def __init__(self):
        self.__li = []
        for key, value in sys.modules.items():
            if "httpimport.HttpImporter" in str(value):
                if key != "pipImport" and key != "docs":
                    module = Module(key)
                    setattr(self, key, module)
                    self.__li.append(module)
    def list(self):
        prBoldIt("List of available PyhtonTools: ")
        for module in self.__li:
            prIt(module.name)                 
    
__all__ = ['Modules']

def prBold(txt): print("\033[1m{}\033[00m" .format(txt))
def prIt(txt): print("\033[3m{}\033[00m" .format(txt))
def prBoldIt(txt): print("\033[1m"+"\033[3m{}\033[00m" .format(txt))
def prUnderlined(txt): print("\033[4m{}\033[00m" .format(txt))
def prRed(txt): print("\033[91m{}\033[00m" .format(txt))
def prGreen(txt): print("\033[92m{}\033[00m" .format(txt))
def prPurple(txt): print("\033[94m{}\033[00m" .format(txt))
def prPink(txt): print("\033[95m{}\033[00m" .format(txt))
def prCyan(txt): print("\033[96m{}\033[00m" .format(txt))

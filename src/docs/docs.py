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
        print(f"Documentation of {self.name} module:")
        print(Docs().getModuleDoc(self.name))
        
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
        print("List of available PyhtonTools: ")
        for module in self.__li:
            print(module.name)                 
    
__all__ = ['Modules']

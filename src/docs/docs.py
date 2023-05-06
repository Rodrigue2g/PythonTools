class Docs:
    def __init__(self):
        self.docs = {
                     "pipUtility": " Complex list that \"ovverides\" the append() method for more complex operations, reducing the amount of code you need to write.",
                     "copyCatch": "Check the resemblance percentage of several files (2-50). To do so, run copyCacth() in the directory of the files you want to check.",
                     "pipTest": "Hello World test module"
                    }
    
    def getModuleDoc(self, name) -> str:
        return self.docs.get(name, "No documentation available for this module.")
        
def getModuleDoc(name) -> str:
    d = Docs()
    return d.getModuleDoc(name)
    
    
__all__ = ['getModuleDoc']

class CList(list):
    def __init__(self):
        pass
    
    def append2(self, item1, item2):  # append two diffrent items (Deprecated considering appendM)
        super(CList, self).append(item1)
        super(CList, self).append(item2)
    
    def appendS(self, item, val:int):  # append the same item several times
        for i in range(val):
            super(CList, self).append(item)
            
    def appendM(self, *args):  # append multiple items
        for item in args:
            super(CList, self).append(item)
                # (instead of extend() which works with a list of items but not several items directly in the parameters)
                # Could be replaced by appendL but doesn't require a key (simplified version)
            
    def appendL(self, **data):  # append several items of different types
        for key, item in data.items():
            if key == "li":
                for elem in item:
                    super(CList, self).append(elem)
            else:
                super(CList, self).append(item)
                # Can be seen as a blend of append() and extend()
                # (ex: in our use case, append a string and a list of string)


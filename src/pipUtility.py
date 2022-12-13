# Clist() for python by DESIGNØ®
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
# Use CList as follow: li = CList() to perform complex append() on a list
#
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

#                
# End of file
#

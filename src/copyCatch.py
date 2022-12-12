# CopyCacth by DESIGNØ®
# This Software is copyright DESIGNØ®, all rights reserved.
# Copyright © 2022 DESIGNØ SASU.
"""
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
#
# Use this software with files in the same directory
#

from difflib import SequenceMatcher
import random
import os.path
    
class _Copy:
    def __init__(self, file1, file2, copyRate):
        self.file1 = file1
        self.file2 = file2
        self.copyRate = copyRate*100
    
    def __cheatAccuracy(self) -> int:
        return randoom.randint(0,100)
    def __cheating(slef) -> bool:
        if self.copyRate > 10 :
            return true
        else:
            return false

class CopyCatch:
    def __init__(self):
        pass
    
    def copyCatch(self) -> None:
        inRange = False
        nbOfFiles = int(input("Enter the number of files\n"))
        if nbOfFiles < 2 or nbOfFiles > 50 :
            print("Please select a number of files between 2 and 50")
            while not inRange:
                nbOfFiles = int(input())
                if nbOfFiles < 2 or nbOfFiles > 50 :
                    print("Please select a number of files between 2 and 50")
                    inRange = False
                elif nbOfFiles >= 2 or nbOfFiles <= 50 :
                    inRange = True
        files = []
        for i in range(nbOfFiles):
            file = input("file name\n")
            if(not os.path.exists(file)):
                print("File doesn't exist")
            else:
                files.append(file)
        
        print("Loading...")
        texts = []
        for file in files:
            text = open(file).read()
            texts.append(text)

        higherRate = 0
        copiedFiles = []
        cheatList: Copy = []
        for i in range(len(texts)-1):
            diff = SequenceMatcher(None, texts[i], texts[i+1])
            val = diff.ratio()
            if val > higherRate:
                higherRate = val
                copiedFiles = [files[i], files[i+1]]
            if val > 0.001 :
                cheatList.append(files(files[i], files[i+1], val))
                # If two files have a similarty ratio above 1% then they are considered potentially fraudulent

        for cheat in cheatList:
            print(f"Pourcentage de ressemblance entre les fichiers: {cheat.file1} et {cheat.file2}:")
            print(f"{cheat.copyRate}%")
        
        if copiedFiles:
            print(f"Les deux fichiers avec le plus grand taux de ressemblance sont: {copiedFiles[0]} et {copiedFiles[1]};")
            print(f"Leur taux de de resseblance est de {higherRate*100}%")
        elif not copiedFiles:
            print("There are no copied files")

def main() -> None:
    c = CopyCatch()
    c.copyCatch()

if __name__ == "__main__":
    main()

import unittest
import collections
import os.path
import os
import sys
from os import path

def IsAnagram(lis):
    count = 0
    ana = collections.defaultdict(list)
    for a in lis:
        ana[tuple(sorted(a))].append(a)
    for i in range(len(list(ana.values()))):
        if  len(list(ana.values())[i]) > 1:
            count += 1

    return count

class MyAnagramTests(unittest.TestCase):
    def test_AllElementsInListAreEmpty(self):
        a = ["", ""]
        self.assertEqual(IsAnagram(a), 1)

    def test_AElementAndBElementAreDiffent(self):
        a = ["", "a"]
        self.assertEqual(IsAnagram(a), 0)

    def test_ElementAandElementBAreSameAndCIsDifferent(self):
        a=["a", "a", "b"]
        self.assertEqual(IsAnagram(a), 1)

    def test_FistAndSecondElementAreTheSameAndThirdAndFourthToo(self):
        a=["a", "a", "b", "b"]
        self.assertEqual(IsAnagram(a), 2)
    
    def test_SevenAnagrams(self):
        a=["paste", "pates", "peats" ,"septa" ,"spate","tapes", "tepas"]
        self.assertEqual(IsAnagram(a), 1)
    
    def test_Pos1Pos2AreAnagramsPost3Post4AreDifAnagramPost5Post6AreDifAnagramsPost7Post8AreDifAnagram(self):
        a=["paste", "pates", "kinship", "pinkish" ,"enlist", "inlets", "boaster" ,"boaters"]
        self.assertEqual(IsAnagram(a), 4)
    
    def test_EverythingIsDifferentThereforeNoAnagrams(self):
        a=["pas", "pes", "kinsp", "pkish" ,"nlist", "inles", "boste" ,"boater"]
        self.assertEqual(IsAnagram(a), 0)
    

path = sys.argv[1]
result = []
if os.path.exists(path):
    os.path.exists(path)
    with open(path) as fp:
        line = fp.readline()
        cnt = 0
        sortedList = []
        while line:
            result.append(line)
            line = fp.readline()
            cnt += 1
    result = [s.rstrip() for s in result]
    print(IsAnagram(result))
else: 
    print("File not specified/found")

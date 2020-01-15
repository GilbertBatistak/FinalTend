import unittest

def IsAnagram(a):
    count = 0
    if a[0] == a[1]:
        count += 1
    return count

class MyAnagramTests(unittest.TestCase):
    def test_AllElementsInListAreEmpty(self):
        a = ["", ""]
        self.assertEqual(IsAnagram(a), 1)

    def test_AElementAndBElementAreDiffent(self):
        a = ["", "a"]
        self.assertEqual(IsAnagram(a), 0)

    def test_ElementAandElementBAreNone(self):
        a=[None, None]
        self.assertEqual(IsAnagram(a), 1)
    
unittest.main()
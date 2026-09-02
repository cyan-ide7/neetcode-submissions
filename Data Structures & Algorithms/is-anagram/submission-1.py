class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict1 = collections.Counter(s)
        dict2 = collections.Counter(t)

        if dict1 == dict2:
            return True
        return False
class Solution:
    def counter(self, a):
        rec = {}
        for char in a:
            if char in rec:
                rec[char]+=1
            else:
                rec[char] = 1
        return rec

    def isAnagram(self, s: str, t: str) -> bool:
         return self.counter(s) == self.counter(t)
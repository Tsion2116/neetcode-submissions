class Solution:
    def isPalindrome(self, s: str) -> bool:
        S=''

        for char in s:
            if char.isalnum():
                S+= char.lower()
        
        l=0
        r=len(S)-1
        while l<r:
            if S[l]!=S[r]:
                return False
            l+=1
            r-=1
        return True
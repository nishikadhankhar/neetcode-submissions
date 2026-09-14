from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need=Counter(t)
        missing=len(t)
        best_len=float("inf")
        best_left,best_right=0,0
        left=0
        for right in range(len(s)):
            if need[s[right]]>0:
                missing-=1
            need[s[right]]-=1
            while missing==0:
                if right-left+1<best_len:
                 best_len=right-left+1
                 best_left,best_right=left,right 
                need[s[left]]+=1
                if need[s[left]]>0:
                    missing+=1
                left+=1
        return s[best_left:best_right+1] if best_len != float("inf") else ""



        
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=Counter(s1)
        need=Counter()
        left=0
        for right in range(len(s2)):
            need[s2[right]]+=1
            if right-left+1>len(s1):
                need[s2[left]]-=1
                if need[s2[left]]==0:
                    del need[s2[left]]
                left+=1
            while right-left+1==len(s1) and window==need:
                return True 
        return False

        
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        pairs=list(c.items())
        pairs.sort(key=lambda p:p[1],reverse=True)
        top=pairs[:k]
        result=[]
        for i, j in top:
            result.append(i)
        return result


        


        
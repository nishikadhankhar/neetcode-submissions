class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1=''.join(sorted(s))
        seen2=''.join(sorted(t))
        if seen1==seen2:
            return True
        return False
        
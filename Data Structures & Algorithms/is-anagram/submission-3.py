class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_frequency, t_frequency = {}, {}

        for i in range(len(s)):
            s_frequency.setdefault(s[i], 0)
            t_frequency.setdefault(t[i], 0)
            s_frequency[s[i]] = s_frequency.get(s[i], 0) + 1
            t_frequency[t[i]] = t_frequency.get(t[i], 0) + 1

        return s_frequency == t_frequency

        
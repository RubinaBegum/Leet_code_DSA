class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        count = defaultdict(int)
        i = 0
        j = 0
        if not s:
            return result
        while j < len(s):
            count[s[j]] += 1
            while count[s[j]] > 1:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1
            result = max(result, j - i + 1)
            j += 1
        return result
        
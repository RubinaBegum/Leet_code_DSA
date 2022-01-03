
def shortest(strs):
    short, l = "", 201
    for w in strs:
        new_l = len(w)
        if new_l < l:
            short, l = w, new_l
    return short
    
class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        short = shortest(strs)
        for c in short:
            new_prefix = prefix + c
            for w in strs:
                if not w.startswith(new_prefix):
                    return prefix
            prefix = new_prefix
        return prefix
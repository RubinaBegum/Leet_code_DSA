class Solution(object):
    def twoSum(self, l1, l2):
        dict1={}  
        for i in range(len(l1)):
            if l2-l1[i] not in dict1.keys():
                dict1[l1[i]]=i
            else:
                break
        I= [i,dict1[l2-l1[i]]]
        return I
        
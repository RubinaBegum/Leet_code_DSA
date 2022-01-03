class Solution(object):
    def removeDuplicates(self, a):
    # class Solution:
    # def removeDuplicates(self, a: List[int]) -> int:
        size = len(a)
        if size ==0 or size == 1:
                return size
        j=0
        for i in range(0,size-1):
            if a[i]!=a[i+1]:
                a[j]=a[i]
                j+=1
        a[j] = a[size-1]
        j += 1
        return j
        
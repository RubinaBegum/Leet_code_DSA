class Solution(object):
    def reverse(self, x):
    
#         while x != 0:
#             digit = x% 10
#             reversed_num = reversed_num * 10 + digit
#             x//= 10

#         return reversed_num
         # return str(x)[::-1]
        
        rev_x = int(str(abs(x))[::-1])

        if x < 0:
            if -2**31 <= -rev_x:            
                return -rev_x

        else:
            if rev_x <= 2**31 - 1:
                return rev_x

        return 0
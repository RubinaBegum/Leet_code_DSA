class Solution(object):
    def isPalindrome(self, x):
#         reverse = 0
#         n=x

#         while n != 0:
#             digit = n % 10
#             reverse = reverse * 10 + digit
#             n//= 10

#         if reverse==x:
#             return "true"
#         else:
#              return "false"
            
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1]==str(x)
        
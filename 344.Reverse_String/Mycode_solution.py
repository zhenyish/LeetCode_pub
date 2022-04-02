class Solution(object):
    "This is not a in-place solution since I create a new list call fix_size_list"
    def reverseString(self, s):
        "create the fixed size list with len(s), the default value is 0 in each index"
        fix_size_list = [0] * len(s)   
        "initialize quotient(halfsize) and remainder(mod)"
        halfsize = len(s)/2
        mod = len(s)%2
        "change the right part of the list s"
        for i in range(halfsize+mod):
            fix_size_list[i] = s[len(s)-1-i]
            s[len(s)-1-i] = s[i]
        "change the left part of the list s"
        for i  in range(halfsize):
            s[i] = fix_size_list[i]
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        

class Solution(object):
    def firstPalindrome(self, words):
        "detect if words list is an empty list"
        if(len(words) == 0):
            return ""
        "iterate the i to find whether a palindromic is existed"
        "if statement will return when find the first palindromic string"
        "words[i][::-1] will reserve the string"
        for i in range(len(words)):
            if(words[i] == words[i][::-1]):
                return words[i]
        "do not forget to return empty string if there is no palindromic string in the words"
        return ""
            
        """
        :type words: List[str]
        :rtype: str
        """
        

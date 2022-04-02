class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        i, num = 0, 0
        "use range will be efficient than use List directly"
        for j in range(len(abbr)):
            "To detect whether there is a leading zero"
            "This if statement only consider to the number of the abbreviation"
            "This else statement only consider the update of i and reset num as 0"
            "else statement will detect the current element of word is same as current abbr element or not"
            if abbr[j].isdigit():
                if num == 0 and abbr[j] == '0':
                    return False
                num = int(abbr[j]) + 10*num
            else:
                i, num = i + num, 0
                "use i >= len(word) to prevent outside of the List size"
                "This if statement is to make sure abbr expected size is not huge than word size"
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
        "This is to make sure word size is not huge than abbr expected size"
        return (i + num) == len(word)

    """
        :type word: str
        :type abbr: str
        :rtype: bool
    """
        

------------------------
26 Remove Duplicates from Sorted Array
------------------------

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

-------------------------
Custom Judge:
------------------------

The judge will test your solution with the following code:

        int[] nums = [...]; // Input array
        int[] expectedNums = [...]; // The expected answer with correct length

        int k = removeDuplicates(nums); // Calls your implementation

        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }

If all assertions pass, then your solution will be accepted.

------------------------
Example 1:
------------------------

    Input: words = ["abc","car","ada","racecar","cool"]
    Output: "ada"
    Explanation: The first string that is palindromic is "ada".
    Note that "racecar" is also palindromic, but it is not the first.

------------------------
Example 2:
------------------------

    Input: words = ["notapalindrome","racecar"]
    Output: "racecar"
    Explanation: The first and only string that is palindromic is "racecar".

------------------------
Example 3:
------------------------

    Input: words = ["def","ghi"]
    Output: ""
    Explanation: There are no palindromic strings, so the empty string is returned.

------------------------
Constraints:
------------------------

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists only of lowercase English letters.
 
--------------------
Source
--------------------

LeetCode

-------------------
Hint1
-------------------

Iterate through the elements in order. As soon as the current element is a palindrome, return it.

-------------------
Hint2
-------------------

To check if an element is a palindrome, can you reverse the string?

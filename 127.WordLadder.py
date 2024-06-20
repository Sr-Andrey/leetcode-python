"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists."""

"""Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence."""

# `collections` and `string` are already imported in LeetCode
import collections
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        transformations = collections.deque()
        # start with beginWord
        transformations.append(beginWord)

        res = 0
        while transformations:
            # start new transformation step
            res += 1
            # try all options in this transformation step
            for _ in range(len(transformations)):
                word_chars = list(transformations.popleft())
                for idx, orig_char in enumerate(word_chars):
                    for new_char in string.ascii_lowercase:
                        word_chars[idx] = new_char
                        new_word = "".join(word_chars)
                        if new_word == endWord:
                            return res + 1
                        if new_word in word_set:
                            # use this word on the next iteration
                            transformations.append(new_word)
                            # don't get back to this word ever again
                            word_set.remove(new_word)
                    word_chars[idx] = orig_char

        return 0

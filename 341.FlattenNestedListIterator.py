"""You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct."""

"""You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct."""

# `collections` is already imported in LeetCode
import collections

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """




class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        # you could fill a regular list and then reverse it at the end
        self.integers = collections.deque()
        self.flatten(nestedList)

    def flatten(self, integers: list[NestedInteger]):
        for elem in integers:
            if elem.isInteger():
                self.integers.append(elem.getInteger())
            else:
                self.flatten(elem.getList())

    def next(self) -> int:
        return self.integers.popleft()

    def hasNext(self) -> bool:
        return len(self.integers) > 0


# generators solution. does it consume more or less memory?

class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.iter = self.iterate(nestedList, top_level=True)
        self.next_value = next(self.iter)

    def iterate(self, nested_list: list[NestedInteger], top_level: bool = False):
        for nested_elem in nested_list:
            if nested_elem.isInteger():
                yield nested_elem.getInteger()
            else:
                yield from self.iterate(nested_elem.getList())

        if top_level:
            yield None

    def next(self) -> int:
        ret_val = self.next_value
        self.next_value = next(self.iter)
        return ret_val

    def hasNext(self) -> bool:
        return self.next_value is not None

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        #Let's do pythonic way
        # We can call sorted and pass a lambda that extracts the key of the Pair and sort using that. We can implement this in just one line.


        return sorted(pairs, key=lambda pair: pair.key)
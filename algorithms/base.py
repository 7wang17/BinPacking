import heapq
from typing import List
import math

def calculate_lower_bound(items: List[float]) -> int:
    return math.ceil(sum(items))

def sort_items_decreasing(items: List[float]) -> List[float]:
    return sorted(items, reverse=True)

class MaxHeap:

    def __init__(self, data=None):
        self._data = []

        if data:
            for item in data:
                self.push(item)

    def push(self, item):
        heapq.heappush(self._data, -item)
        # Take a negative number so that the 'maximum value' becomes the 'minimum value'

    # Pop up the maximum element
    def pop(self):
        return -heapq.heappop(self._data)
        # Pop up the minimum value (negative), then take the negative number to be the original value

    # View the maximum element (without popping up)
    def peek(self):
        return -self._data[0] if self._data else None

    def __len__(self):
        return len(self._data)

    def __bool__(self):
        return len(self._data) > 0
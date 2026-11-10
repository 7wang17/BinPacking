from typing import List
from algorithms.base import MaxHeap, sort_items_decreasing

def wfd_m_can_pack_optimized(items: List[float], m: int, capacity: float = 1.0) -> bool:
    sorted_items = sort_items_decreasing(items)

    # Initialize the maximum heap, storing the remaining capacity of each bin
    heap = MaxHeap([capacity] * m)

    # Traverse each item and check the bin with the highest remaining capacity at present
    for item in sorted_items:
        max_rem = heap.peek()

        if max_rem >= item:
            # Pop up this bin, put in the items, and then push it back into the heap
            heap.pop()
            heap.push(max_rem - item)
        else:
            return False

    return True


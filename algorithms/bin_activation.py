from typing import List, Optional, Tuple
from algorithms.base import calculate_lower_bound
from algorithms.wfd_m import wfd_m_can_pack_optimized
from algorithms.seqpacker_wrapper import wfd_bins_used


def wfd_m_binary_search(items: List[float], capacity: float = 1.0,
                        ub: Optional[int] = None) -> Tuple[int, int]:

    lb = calculate_lower_bound(items)

    # If no upper bound provided, run classic WFD to get one
    if ub is None:
        ub = wfd_bins_used(items, capacity)

    attempts = 0
    while lb < ub:
        mid = (lb + ub) // 2
        attempts += 1
        if wfd_m_can_pack_optimized(items, mid, capacity):
            ub = mid
        else:
            lb = mid + 1

    # Final verification
    if not wfd_m_can_pack_optimized(items, lb, capacity):
        # Fallback: try lb + 1, lb + 2, ... until a feasible m is found
        while not wfd_m_can_pack_optimized(items, lb, capacity):
            lb += 1
            attempts += 1

    return lb, attempts


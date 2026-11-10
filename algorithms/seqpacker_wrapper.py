from seqpacker import Packer
from typing import List
from algorithms.base import sort_items_decreasing

SCALE = 100000


def _pack_items(items: List[float], capacity: float, strategy: str) -> int:
    items_int = [int(x * SCALE) for x in items]
    capacity_int = int(capacity * SCALE)
    packer = Packer(capacity=capacity_int, strategy=strategy)
    result = packer.pack(items_int)
    return result.num_bins


def ff_bins_used(items: List[float], capacity: float = 1.0) -> int:
    return _pack_items(items, capacity, "ff")


def bf_bins_used(items: List[float], capacity: float = 1.0) -> int:
    return _pack_items(items, capacity, "bf")


def wf_bins_used(items: List[float], capacity: float = 1.0) -> int:
    return _pack_items(items, capacity, "wf")


def ffd_bins_used(items: List[float], capacity: float = 1.0) -> int:
    return _pack_items(items, capacity, "ffd")


def bfd_bins_used(items: List[float], capacity: float = 1.0) -> int:
    return _pack_items(items, capacity, "bfd")


def wfd_bins_used(items: List[float], capacity: float = 1.0) -> int:
    sorted_items = sort_items_decreasing(items)
    return _pack_items(sorted_items, capacity, "wf")
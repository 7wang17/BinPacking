"""
Public utility functions and constants
"""
from typing import List

INSTANCE_TYPES = ['Falkenauer_U', 'Triplet', 'Hard28', 'Scholl_1', 'Scholl_2', 'Wascher']

ALGO_COLS = ['FF_bins', 'BF_bins', 'WF_bins', 'FFD_bins', 'BFD_bins', 'WFD_bins', 'wfd_m_m']

BEST_TIME_COLS = ['FF_time_ms', 'BF_time_ms', 'FFD_time_ms', 'BFD_time_ms']


def classify_instance_type(name: str) -> str:
    if name.startswith('FU_'):
        return 'Falkenauer_U'
    elif name.startswith('Falkenauer_t'):
        return 'Triplet'
    elif name.startswith('Hard28'):
        return 'Hard28'
    elif name.startswith('Scholl1'):
        return 'Scholl_1'
    elif name.startswith('Scholl2'):
        return 'Scholl_2'
    elif name.startswith('Wascher'):
        return 'Wascher'
    else:
        return 'Other'
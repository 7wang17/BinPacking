import os
from typing import Dict, List, Tuple
import pandas as pd


def read_bpp_instance(filepath: str) -> Tuple[float, List[float]]:
    with open(filepath, 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    capacity = float(lines[1].strip())
    items = []
    for line in lines[2:2 + n]:
        items.append(float(line.strip()))

    return capacity, items


def normalize_items(items: List[float], capacity: float) -> List[float]:
    return [item / capacity for item in items]


def load_generic_instance(filepath: str) -> Tuple[List[float], float, int]:
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])
    capacity = float(lines[1])
    items = []
    for line in lines[2:2 + n]:
        items.append(float(line))

    normalized = [item / capacity for item in items]
    return normalized, capacity, n


def load_optimal_solutions_from_excel(excel_path: str) -> Dict[str, int]:
    optimal_dict = {}
    sheets = ['Falkenauer', 'Scholl', 'Schoenfield Hard28', 'Wäscher']
    xlsx = pd.ExcelFile(excel_path)

    for sheet_name in sheets:
        df = pd.read_excel(xlsx, sheet_name=sheet_name)

        for _, row in df.iterrows():
            excel_name = str(row['Name']).strip()
            best_ub = int(row['Best UB'])
            base_name = excel_name.replace('.txt', '')

            optimal_dict[base_name] = best_ub
            optimal_dict[excel_name] = best_ub

            if base_name.startswith('Falkenauer_u'):
                optimal_dict[f"FU_{base_name}"] = best_ub
                optimal_dict[f"FU_{excel_name}"] = best_ub

            elif base_name.startswith('Falkenauer_t'):
                optimal_dict[f"Falkenauer_t_{base_name}"] = best_ub
                optimal_dict[f"Falkenauer_t_{excel_name}"] = best_ub

            elif sheet_name == 'Scholl':
                optimal_dict[f"Scholl1_{base_name}"] = best_ub
                optimal_dict[f"Scholl2_{base_name}"] = best_ub

            elif sheet_name == 'Schoenfield Hard28':
                optimal_dict[f"Hard28_{base_name}"] = best_ub
                optimal_dict[f"Hard28_{excel_name}"] = best_ub

            elif sheet_name == 'Wäscher':
                optimal_dict[f"Wascher_{base_name}"] = best_ub

    return optimal_dict
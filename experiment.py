import os
import time
import csv
from typing import List, Dict, Any, Tuple
from utils.instance_reader import (
    load_generic_instance,
    load_optimal_solutions_from_excel,
)
from algorithms.base import calculate_lower_bound
from algorithms.seqpacker_wrapper import (
    ff_bins_used,
    bf_bins_used,
    wf_bins_used,
    ffd_bins_used,
    bfd_bins_used,
    wfd_bins_used,
)
from algorithms.bin_activation import wfd_m_binary_search


def load_instances_with_optimal(
        folder_path: str,
        prefix: str,
        optimal_dict: Dict[str, int],
        max_files: int = None
) -> List[Tuple[List[float], str, int]]:
    instances = []
    if not os.path.exists(folder_path):
        print(f"  Path does not exist: {folder_path}")
        return instances

    files = sorted([f for f in os.listdir(folder_path) if f.endswith('.txt')])
    if max_files:
        files = files[:max_files]

    for filename in files:
        filepath = os.path.join(folder_path, filename)
        items, _, n = load_generic_instance(filepath)
        base_name = filename.replace('.txt', '')
        instance_name = f"{prefix}_{base_name}"

        optimal = optimal_dict.get(instance_name)
        print(f"  Loading {instance_name}: optimal = {optimal}")

        instances.append((items, instance_name, optimal))

    return instances


def run_single_instance(items: List[float], instance_name: str,
                        optimal: int = None) -> Dict[str, Any]:
    lb = calculate_lower_bound(items)
    row = {
        'instance': instance_name,
        'n': len(items),
        'lower_bound': lb,
        'optimal': optimal
    }

    algorithms = {
        'FF': ff_bins_used,
        'BF': bf_bins_used,
        'WF': wf_bins_used,
        'FFD': ffd_bins_used,
        'BFD': bfd_bins_used,
        'WFD': wfd_bins_used,
    }

    for name, func in algorithms.items():
        start = time.perf_counter()
        bins = func(items)
        elapsed = (time.perf_counter() - start) * 1000
        row[f'{name}_bins'] = bins
        row[f'{name}_time_ms'] = round(elapsed, 3)

    start = time.perf_counter()
    m_bin, attempts_bin = wfd_m_binary_search(items)
    time_bin = (time.perf_counter() - start) * 1000
    row['wfd_m_m'] = m_bin
    row['wfd_m_attempts'] = attempts_bin
    row['wfd_m_time_ms'] = round(time_bin, 3)

    return row


def run_experiment(instance_list, output_file='experiment_results.csv'):
    all_results = []
    for items, name, optimal in instance_list:
        print(f"  Running {name}...")
        row = run_single_instance(items, name, optimal)
        all_results.append(row)

    if all_results:
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=all_results[0].keys())
            writer.writeheader()
            writer.writerows(all_results)
        print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
    base_dir = "D:/UoL/MScProject/BPPLIB-main"
    excel_path = os.path.join(base_dir, "Instances", "Solutions", "Solutions.xlsx")

    optimal_dict = load_optimal_solutions_from_excel(excel_path)
    print(f"Loaded {len(optimal_dict)} optimal solutions from BPPLIB\n")

    all_instances = []
    base = os.path.join(base_dir, "Instances", "Benchmarks")

    fu_dir = os.path.join(base, "1_Falkenauer", "Falkenauer", "Falkenauer U")
    if os.path.exists(fu_dir):
        all_instances.extend(load_instances_with_optimal(fu_dir, "FU", optimal_dict, max_files=30))
        print(f"Loaded {len([x for x in all_instances if x[1].startswith('FU_')])} Falkenauer_U instances\n")

    triplet_dir = os.path.join(base, "1_Falkenauer", "Falkenauer", "Falkenauer_T")
    if os.path.exists(triplet_dir):
        all_instances.extend(load_instances_with_optimal(triplet_dir, "Falkenauer_t", optimal_dict))
        print(f"Loaded {len([x for x in all_instances if x[1].startswith('Falkenauer_t')])} Falkenauer_T instances\n")

    hard28_dir = os.path.join(base, "5_Hard28", "Hard28")
    if os.path.exists(hard28_dir):
        all_instances.extend(load_instances_with_optimal(hard28_dir, "Hard28", optimal_dict))
        print(f"Loaded {len([x for x in all_instances if x[1].startswith('Hard28')])} Hard28 instances\n")

    scholl1_dir = os.path.join(base, "2_Scholl", "Scholl", "Scholl_1")
    if os.path.exists(scholl1_dir):
        all_instances.extend(load_instances_with_optimal(scholl1_dir, "Scholl1", optimal_dict, max_files=30))
        print(f"Loaded {len([x for x in all_instances if x[1].startswith('Scholl1')])} Scholl_1 instances\n")

    scholl2_dir = os.path.join(base, "2_Scholl", "Scholl", "Scholl_2")
    if os.path.exists(scholl2_dir):
        all_instances.extend(load_instances_with_optimal(scholl2_dir, "Scholl2", optimal_dict, max_files=30))
        print(f"Loaded {len([x for x in all_instances if x[1].startswith('Scholl2')])} Scholl_2 instances\n")

    washer_dir = os.path.join(base, "3_Wäscher", "Wäscher")
    if os.path.exists(washer_dir):
        all_instances.extend(load_instances_with_optimal(washer_dir, "Wascher", optimal_dict, max_files=30))
        print(f"Loaded {len([x for x in all_instances if x[1].startswith('Wascher')])} Wäscher instances\n")

    print(f"\nTotal instances to run: {len(all_instances)}")
    run_experiment(all_instances, output_file="experiment_results.csv")
This repository contains the source code, experimental framework, and result analysis scripts.

The project systematically evaluates six classic item-centric heuristics (FF, BF, WF, FFD, BFD, WFD) against a recently proposed multi-bin activation algorithm (WFD(m)) on 215 benchmark instances from BPPLIB, measuring both solution quality and computational efficiency.

## Project Structure

* **algorithms/**
  * `base.py` - Base classes (MaxHeap, Bin)
  * `bin_activation.py` - Binary search strategy for WFD(m)
  * `seqpacker_wrapper.py` - Python wrapper for the seqpacker library
  * `wfd_m.py` - WFD(m) core packing logic
* **scripts/**
  * `compute_avg_bins.py` - Computes average bin usage
  * `compute_time.py` - Computes average runtime
* **utils/**
  * `common.py` - Shared constants and helper functions
  * `error_analyzer.py` - Error calculation and table generation
  * `instance_reader.py` - BPPLIB instance reading and optimal loading
* **.gitignore** - Git ignore rules
* **experiment.py** - Main entry point for running the experiments

## Requirements

* Python 3.13 (or higher)
* pandas (for data processing and CSV/Excel handling)
* seqpacker (Rust-based library for classic bin packing heuristics)

You can install the required Python packages by running:

    pip install pandas
    pip install seqpacker

## Usage

To run all seven algorithms on the benchmark instances and generate the raw results, execute:

    python experiment.py

This will output `experiment_results.csv` containing the number of bins used and runtime for each algorithm.

To calculate relative errors against optimal solutions and generate summary tables, execute:

    python utils/error_analyzer.py

This will output `experiment_results_with_error.csv` with error columns and print the formatted tables to the console.

## Datasets

All benchmark instances are obtained from BPPLIB (Delorme et al., 2018). The study uses 215 instances across six categories: Falkenauer_U, Falkenauer_T, Hard28, Scholl_1, Scholl_2, and Wäscher.

## Reproducibility

All algorithms used in this study are deterministic. Given the same input instances, the code will always produce the exact same bin counts. All raw data, experimental logs, and analysis scripts are provided in this repository to ensure full reproducibility of the results.

## References

* Delorme, M., Iori, M. and Martello, S. (2018). BPPLIB: a library for bin packing and cutting stock problems. *Optimization Letters*, 12(2), pp.235-250.
* Mommessin, C., Erlebach, T. and Shakhlevich, N.V. (2025). Classification and evaluation of the algorithms for vector bin packing. *Computers & Operations Research*, 173, 106860.

---
Developed as part of the MSc Computer Science Project at the University of Leeds.
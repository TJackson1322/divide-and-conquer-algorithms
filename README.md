# Divide-and-Conquer Algorithms: Merge Sort vs. Quicksort

## Project Overview
This project was completed for my Algorithms and Data Structures course at the University of the Cumberlands.

I implemented Merge Sort and Quicksort in Python to compare their efficiency when sorting simulated student assignment scores. I chose this example because it connects to my experience working in education and my interest in software development.

## Algorithms
- **Merge Sort:** Divides data into smaller groups, sorts them, and merges the results.
- **Quicksort:** Selects a pivot and partitions the data into smaller groups before recursively sorting them.

## Testing and Results
Both algorithms were designed to be tested with sorted, reverse-sorted, and random datasets containing 100, 1,000, and 5,000 scores.

The repository includes recorded results for the 5,000-score tests. In these measurements, Quicksort was faster, while Merge Sort used less peak traced memory.

## Running the Program
Python 3 is required. Run:

`python3 sorting_comparison.py`

The program will generate a new `performance_results.csv` containing results for all three dataset sizes.

## Project Files
- `sorting_comparison.py` — Python implementation and benchmarking code.
- `performance_results.csv` — Recorded execution-time and memory-usage measurements.

## Conclusion
This project demonstrates why developers must consider theoretical time complexity, execution time, memory usage, and dataset characteristics when choosing a sorting algorithm.

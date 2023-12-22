# Testing parallelization with nested loops in Python
import multiprocessing
from joblib import Parallel, delayed

# Define any function and inputs
column_list = [1, 3, 5, 7]
row_list = [2, 4, 8, 12]


def print_sum(i, j):
    print(i, j, i + j)


# Find the number of cores (or input the number you want)
num_cores = multiprocessing.cpu_count()

"""""# Method 1 of parallelization
Parallel(n_jobs=num_cores)(delayed(print_sum)(i, j) for j in column_list for i in row_list)"""


# Method 2 of parallelization (with a generator function)
def compute_pairs(row_list, column_list):
    for i in row_list:
        for j in column_list:
            yield j, i


Parallel(n_jobs=num_cores)(delayed(print_sum)(j, i) for j, i in compute_pairs(row_list, column_list))

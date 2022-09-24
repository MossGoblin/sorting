import numpy as np
import pandas as pd
from timeit import timeit
from progress.bar import PixelBar
import os
from toolbox import lists as ls
# Path fix
import sys
sys.path.append('../')

runs = 100
min = 0
max = 100
size = 1000
reset_output_folder = False

algorithm_stmts = ls.algorithm_stmts


def _get_rand_set(min: int, max: int, size: int):
    set = np.random.randint(min, max, size=size)
    set = set.tolist()
    return set


def _prep_output_folder(folder_name: str, reset_output_data: bool):
    '''
    Prepare folder for output csv files
    '''
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    else:
        if reset_output_data:
            for root, directories, files in os.walk(folder_name):
                for file in files:
                    file_path = root + '/' + file
                    os.remove(file_path)


def _get_max_algorithm_name_length(algorithm_stmts):
    max_length = 0
    for algorithm_name, algorithm_stmt in algorithm_stmts:
        if len(algorithm_name) > max_length:
            max_length = len(algorithm_name)

    return max_length


def main():
    buckets = []
    time_field_name = 'time (us)'
    results = {}

    for run in range(runs):
        bucket = _get_rand_set(min, max, size)
        # bucket = [1] * 1000
        buckets.append(bucket)

    for algorithm_name, algorithm_stmt in algorithm_stmts:
        results[algorithm_name] = {}
        results[algorithm_name][time_field_name] = 0
        run_measurements = 0.0
        max_algorithm_name_length = _get_max_algorithm_name_length(
            algorithm_stmts)
        bucket_bar = PixelBar(algorithm_name.ljust(
            max_algorithm_name_length, ' '), max=len(buckets))
        for bucket in buckets:
            measurement = timeit(
                algorithm_stmt,
                setup="""from algorithms import sort_collection as sc
from algorithms import test_collection as tc""",
                globals={"bucket": bucket},
                number=1)
            run_measurements += measurement
            bucket_bar.next()
        bucket_bar.finish()

        results[algorithm_name][time_field_name] = run_measurements / runs
    print('\n')

    df_by_name = pd.DataFrame().from_dict(results, orient='index')
    df_by_value = df_by_name.sort_values(by='time (us)', axis=0)
    print('Results (by name)')
    print(df_by_name)
    print('\n')
    print('Results (by value)')
    print(df_by_value)
    _prep_output_folder('results', reset_output_folder)
    file_name_by_name = f'results/results_{runs:02}_runs__size_{size}__max_{max}_by_name.csv'
    file_name_by_value = f'results/results_{runs:02}_runs__size_{size}__max_{max}_by_value.csv'
    df_by_name.to_csv(file_name_by_name)
    df_by_value.to_csv(file_name_by_value)


if __name__ == "__main__":
    main()

from test_pile.push_sort import __version__
from test_pile.push_sort import push_sort


def test_version():
    assert __version__ == '1.0.0'

def test_sort_flag_false():
    bucket = [3, 5, 7, 1, 5, 9, 8, 4, 6, 2]
    ordered_bucket = push_sort.sort(bucket)
    assert ordered_bucket == sorted(bucket)

def test_sort_flag_true():
    bucket = [3, 5, 7, 1, 5, 9, 8, 4, 6, 2]
    ordered_bucket = push_sort.sort(bucket)
    assert ordered_bucket == sorted(bucket)

def test_sort_flag_floating_false():
    bucket = [3.0, 5.1, 7.2, 1.3, 5.4, 9.5, 8.6, 4.7, 6.8, 2.9]
    ordered_bucket = push_sort.sort(bucket)
    assert ordered_bucket == sorted(bucket)

def test_sort_flag_floating_true():
    bucket = [3.0, 5.1, 7.2, 1.3, 5.4, 9.5, 8.6, 4.7, 6.8, 2.9]
    ordered_bucket = push_sort.sort(bucket)
    assert ordered_bucket == sorted(bucket)
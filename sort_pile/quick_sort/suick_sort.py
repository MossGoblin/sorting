def _partition(bucket, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = bucket[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while bucket[i] < pivot:
            i += 1

        j -= 1
        while bucket[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        bucket[i], bucket[j] = bucket[j], bucket[i]


def sort(bucket):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = _partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(bucket, 0, len(bucket) - 1)
    
    return bucket

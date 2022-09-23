def _heapify(bucket, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and bucket[left_child] > bucket[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and bucket[right_child] > bucket[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        bucket[root_index], bucket[largest] = bucket[largest], bucket[root_index]
        # Heapify the new root element to ensure it's the largest
        _heapify(bucket, heap_size, largest)

    return bucket


def sort(bucket):
    n = len(bucket)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        bucket = _heapify(bucket, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        bucket[i], bucket[0] = bucket[0], bucket[i]
        _heapify(bucket, i, 0)

    return bucket
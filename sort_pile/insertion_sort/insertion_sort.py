def sort(bucket):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(bucket)):
        item_to_insert = bucket[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and bucket[j] > item_to_insert:
            bucket[j + 1] = bucket[j]
            j -= 1
        # Insert the item
        bucket[j + 1] = item_to_insert

    return bucket
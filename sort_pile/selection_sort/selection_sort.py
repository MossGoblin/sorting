def sort(bucket):
    # This value of i corresponds to how many values were sorted
    for i in range(len(bucket)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(bucket)):
            if bucket[j] < bucket[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        bucket[i], bucket[lowest_value_index] = bucket[lowest_value_index], bucket[i]

    return bucket
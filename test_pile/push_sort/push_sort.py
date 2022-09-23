def sort(incoming_bucket):
    result = []
    for item in incoming_bucket:
        placed = False
        if len(result) == 0:
            result.append(item)
            continue
        for placed_item in result:
            if item <= placed_item:
                result.insert(result.index(placed_item), item)
                placed = True
                break
        if not placed:
            result.insert(len(result), item)

    return result

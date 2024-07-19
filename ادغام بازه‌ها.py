def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged

input_data = input("Enter the list of intervals in the format [(1, 3), (2, 6), (8, 10)]: ")

intervals = eval(input_data)

output = merge_intervals(intervals)

print(output)

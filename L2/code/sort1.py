def stupid_sort(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] > data[i]:
            data[i - 1], data[i] = data[i], data[i - 1]
            i = 1
        else:
            i += 1
    return data

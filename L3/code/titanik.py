def read_csv(file_name, sep=","):
    file = open(file_name)

    text = file.readlines()
    columns = text[0].strip().replace(", ", " ").split(sep)

    data = {column_name: [] for column_name in columns}

    for line in text[1:]:
        line = line.strip().split(sep)
        for idx in range(len(columns)):
            column_name = columns[idx]
            elem = line[idx]
            data[column_name].append(elem)
    return data


def print_data(data, sep=","):
    columns = list(data.keys())
    for column_name in columns:
        print(column_name, end=sep)
    print()
    elems_0 = list(data.keys())[0]
    for idx in range(len(data[elems_0])):
        for column_name in columns:
            print(data[column_name][idx], end=sep)
        print()
        break


train_data = read_csv("L3/code/data.txt", sep="\t")
print_data(train_data, sep="\t")

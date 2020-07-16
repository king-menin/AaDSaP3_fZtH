import random
import string


random.seed(1234)


def get_random_string(length=5):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_line(min_str_len, max_str_len, num_columns):
    return [
        get_random_string(random.randint(min_str_len, max_str_len))
        for _ in range(num_columns)
    ]


def get_random_dataset(count=100, min_columns=2, max_columns=5, min_str_len=1, max_str_len=10):
    res = []
    num_columns = random.randint(min_columns, max_columns)
    res.append(get_random_line(min_str_len, max_str_len, num_columns))
    for _ in range(count):
        res.append(get_random_line(min_str_len, max_str_len, num_columns))
    return res


if __name__ == "__main__":
    with open("L3/code/data.txt", "w") as file:
        for line in get_random_dataset():
            file.write("\t".join(line) + "\n")

from collections import Counter


def most_frequent(data: list) -> str:
    res = (Counter(data).most_common(1))
    return res[0][0]


















most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ])
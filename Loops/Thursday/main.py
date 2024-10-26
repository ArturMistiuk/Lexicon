import re


def sequence_check(l: list) -> bool:
    str_converted = str(l)
    pattern = r"(1, 2, 3)"
    match = re.search(pattern, str_converted)
    if match:
        return True
    else:
        return False


def in_one_string(s: str):
    return s[::2]


def double_chars(s: str):
    return str(''.join([l*2 for l in s]))


def even_counter(numbers: list):
    return len([num for num in numbers if num % 2 == 0])


if __name__ == "__main__":
    tests = [
        [1, 1, 2, 3, 3, 1],
        [1, 1, 2, 2, 3, 3, 1]
    ]
    for test in tests:
        print(sequence_check(test))

    print(in_one_string("Hello"))

    print(double_chars("The"))

    print(even_counter([2, 1, 2, 3, 4, 1, 1, 6]))

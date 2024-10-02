# 1. Calculate power with loops
def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    if exponent < 0:
        result = 1 / result
    return result


# 2. Calculate the sum of tuple
def sum_of_tuple_elements(input_tuple):
    return sum(input_tuple)


# 3. Create a new tuple with evens
def filter_even_numbers(input_tuple):
    return tuple(number for number in input_tuple if number % 2 == 0)


# 4. Create a merged dict
def merge_dicts(dict_1, dict_2):
    res = {**dict_1, **dict_2}
    return res


# 5. list -> list of evens
def evens_list(l: list):
    return [num for num in l if num % 2 == 0]



if __name__ == "__main__":
    # Exercise 1: Power calculation
    base = 5
    exponent = 2
    print("Powered: ", power(base, exponent))

    # Exercise 2: Sum of tuple elements
    sample_tuple = (1, 2, 3, 4, 5)
    print(f"Sum of elements is: {sum_of_tuple_elements(sample_tuple)}")

    # Exercise 3: Filter even numbers from tuple
    sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f"Even numbers: {filter_even_numbers(sample_tuple)}")

    # Exercise 4: two dictionaries into a single dictionary
    a = {"x": 30, "y": 50, "z": 100, "h": 150}
    b = {"h": 200, "u": 30, "v": 300}
    print(merge_dicts(a, b))

    # Exercise 5: list to list of evens
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50]
    print(evens_list(l))

    # Exercise 6: reversed string
    s = "I want to be reversed"
    print(s[::-1])

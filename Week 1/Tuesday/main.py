def exercise_1():
    s = "Python"
    print(s[-2], s[:4], s[1:4], s[::-1])


def exercise_2():
    l = [3, 7, [1, 4, "hello"]]
    l[2][-1] = "goodbye"
    print(l)


def exercise_3():
    d1 = {'simple_key': 'hello'}
    d2 = {'k1': {'k2': 'hello'}}
    d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
    print(d1["simple_key"], d2["k1"]["k2"], d3["k1"][0]["nest_key"][1][0])


def exercise_4():
    mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    print(set(mylist))


def exercise_5():
    age = 4
    name = "Sammy"
    print(f"Hello my dog's name is {name} and he is {age} years old")


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    
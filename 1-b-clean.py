"""
A module of mass 14 requires 2 fuel.
This fuel requires no further fuel
(2 divided by 3 and rounded down is 0, which would call for a negative fuel),
so the total fuel required is still just 2.

At first, a module of mass 1969 requires 654 fuel.
Then, this fuel requires 216 more fuel (654 / 3 - 2).
216 then requires 70 more fuel,
which requires 21 fuel,
which requires 5 fuel,
which requires no further fuel.
So, the total fuel required for a module of mass
1969 is 654 + 216 + 70 + 21 + 5 = 966.

The fuel required by a module of mass 100756 and its fuel is:
33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
(33583, 11192, 3728, 1240, 411, 135, 43, 12, 2)

What is the sum of the fuel requirements
for all of the modules on your spacecraft
when also taking into account the mass of the
added fuel? (Calculate the fuel requirements for each module separately,
then add them all up at the end.)
"""

test_items = (
        (12, 2),
        (14, 2),
        (1969, 966),
        (100756, 50346),
    )


def main():
    test(test_items)
    total = calc_sum(get_content('fuel.txt'))
    print(f"result: {total}")

def test(items):
    for i, (a, b) in enumerate(items):
        v = calc(a, b)
        assert v == b, f"fuel #{i} {a:,} calc >> {v:,} != {b:,}"
    print('All good.')


def get_content(filename):
    """Return a tuple of ints from a given file.
    """
    with open(filename) as stream:
        return tuple(map(int, stream.readlines()))


def calc_sum(items):
    """given a tuple of items, calc and return the sum of all fuels.
    """
    return sum(calc(x) for x in items)


def calc(given, default=0):
    fuel = given // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + calc(fuel)


if __name__ == '__main__':
    main()

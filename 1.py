"""
For a mass of 12,
divide by 3 and
round down to get 4,
then subtract 2
to get 2.

For a mass of 14,
dividing by 3
and rounding down still yields 4,
so the fuel required is also 2.

For a mass of 1969,
the fuel required is 654.

For a mass of 100756, the fuel required is 33583.
"""

items = (
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583),
    )


def main():
    test()
    items = get_content('fuel.txt')
    total = calc_all(items)
    print(f"result: {total}")


def get_content(filename):
    """Return a tuple of ints from a given file.
    """
    res = ()

    with open(filename) as stream:
        for line in stream:
            res += ( int(line.strip()), )
    return res


def calc_all(items):
    """given a tuple of items, calc and return the sum of all fuels.
    """
    res = ()
    for val in items:
        res += ( calc(val), )

    total = sum(res)
    print(f"Fuel total: {total:,} on {len(items)} items")
    return total


def test():

    for i, (a, b) in enumerate(items):
        v = calc(a,b)
        assert v == b, f"fuel #{i} {a:,} calc >> {v:,} != {b:,}"

    print('All good.')

from math import floor

def calc(given, default=0):
    ##print(given)
    return floor(given/3) - 2
    return default



if __name__ == '__main__':
    main()

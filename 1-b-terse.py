def calc_file(filename='fuel.txt'):
    with open(filename) as stream:
        items = tuple(map(int, stream.readlines()))
    return sum(calc(x) for x in items)


def calc(given):
    fuel = given // 3 - 2
    if fuel < 1: return 0
    return fuel + calc(fuel)


if __name__ == '__main__':
    total = calc_file()
    print(f"result: {total}")

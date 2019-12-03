import operator as _op

HALT = 'halt'
OPS = { 1: _op.add, 2: _op.mul, 99: HALT }

tests = (
   ( [1,0,0,0,99], [2,0,0,0,99 ], ), # (1 + 1 = 2)
   ( [2,3,0,3,99], [2,3,0,6,99 ], ), # (3 * 2 = 6)
   ( [2,4,4,5,99,0], [2,4,4,5,99,9801 ], ), # (99 * 99 = 9801)
   ( [1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99], ),
)


def get_file(filename='program.txt'):
    with open(filename) as stream:
       return list(map(int, stream.readline().split(",")))


def main():

    for tape, result in tests:
        v = calc(tape)
        assert v == result, f"{v} != {result}"

    tape = get_file()
    tape[1] = 12
    tape[2] = 2
    result = calc(tape)
    print(result[0])

    result = find_pair_100(get_file(), 19690720)
    result_2 = find_pair_100_2(get_file())
    print(result, result_2)

def find_pair_100(tape, target):
    # if noun=12 and verb=2, the answer would be 1202
    for i in range(0, 99):
        for j in range(0, 99):
            tape_c = tape[:]
            tape_c[1], tape_c[2] = i, j
            result = calc(tape_c)[0]
            if result == target:
                return 100 * i + j


def find_pair_100_2(tape):
    for noun in range(54):
        for verb in range(99):
            sub_tape = tape.copy()
            sub_tape[1], sub_tape[2] = noun, verb
            calc(sub_tape)
            if sub_tape[0] == 19690720:
                result = 100 * noun + verb
                print(f"Found: {noun}, {verb} {result}")
                return result


def calc(tape):
    for i in range(0, len(tape), 4):
        op = OPS.get(tape[i])
        if op is None:
            print('Received bad operator int: {i}, {tape[i]}')
            continue

        if op is HALT:
            return tape

        res = op(get(tape, i, 1), get(tape, i, 2))
        tape[tape[i+3]] = res



def get(tape, i, pos):
    return tape[tape[i+pos]]

    # 1, is add
    # 0, value at 0 == 1
    # 0, + value at 0 == 1
    # == 2
    # 0, output at 0 == 2
    # 99, halt
    # 2, 0,0,0,99

    # 2, is *
    # 3, v at #3 == 3
    # 0, v at #0 == 2
    # == 6
    # 3, output at #3 == 6
    # 99 halt
    # 2, 3, 0, 6, 99

    # 2  *
    # 4  #4 == 99
    # 4  #4 == 99
    # 5  @5 == 9801
    # 99 halt
    # 1

    # (2) *
    # (4) == 99
    # (9) == 99
    # (5) @5
    # (@0 ==  == 9801)
    # 9801, 99, 99, 5


    # (1) +       == 30
    # (1) #1 == 1
    # (1) #1 == 1
    # (4) @4 == 2
    # (99) == 2   ==  *
    # (5) #5 == 5
    # (6) #6 == 6
    # (0) @0 == 30
    # (99) halt.
    # == 30, 1, 1, 4, 2, 5, 6, 0, 99

if __name__ == '__main__':
    main()

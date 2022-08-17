import math
import re


def gap_binary(n):
    # conversion to binary
    n_1 = n
    binary = []
    while n_1 > 1:
        if (n_1 % 2) == 0:
            binary.append(0)
        else:
            binary.append(1)
        n_1 = math.floor(n_1 / 2)

    if n_1 == 1:
        binary.append(1)
    binary.reverse()

    string_binary = ''.join(str(x) for x in binary)
    splits = re.split('(1)', string_binary)
    splits = [x for x in splits if len(x) != 0]

    # Final
    no_1s = 0
    for num in splits:
        if num == '1':
            no_1s += 1

    if (no_1s == 1) | (no_1s == len(splits)):
        num = 0
    else:
        clean = []
        indexes_0 = []
        for i, num in enumerate(splits):
            if num != '1':
                indexes_0.append((num, i))

        for part in indexes_0:
            try:
                if (splits[part[1] - 1] == str(1)) & (splits[part[1] + 1] == str(1)):
                    clean.append(part[0])
            except IndexError:
                clean = []

        len_clean = []
        for each in clean:
            len_clean.append(len(each))
        try:
            num = max(len_clean)
        except ValueError:
            num = 0

    return num


print(gap_binary(20))

import sys
import re
from itertools import groupby


def check_word(characters, word):
    groups = [(k, len(list(g))) for k, g in groupby(word)]
    lengths = [group[1] for group in groups]
    if not all(x == lengths[0] for x in lengths):
        return False

    keys = [group[0] for group in groups]
    if len(keys) != len(characters):  # only compare if there are same number of keys
        return False

    return True


def read_striped_line():
    return sys.stdin.readline().strip()


def main():
    pattern = read_striped_line()
    characters = filter(lambda x: len(x) == 1, re.split(r'\^n', pattern))
    word = read_striped_line()

    print ('yes' if check_word(characters, word) else 'no')

if __name__ == '__main__':
    main()
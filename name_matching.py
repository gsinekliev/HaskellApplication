__author__ = 'Admin'

import sys
import re


def get_percentage(known_names, total_names):
    diff = total_names - known_names
    if diff <= 0:
        return 100

    return (1.0 / diff) * 100


def main():
    known_male, known_female = sys.stdin.readline().split()
    names = sys.stdin.readline().split()
    female_names = len([name for name in names if re.match('(\w+)tta', name)])
    male_names = len([name for name in names if re.match('(\w+)ess', name)])

    female_percentage = get_percentage(int(known_female), female_names)
    male_percentage = get_percentage(int(known_male), male_names)

    print('{0}%'.format(min(male_percentage, female_percentage)))


if __name__ == '__main__':
    main()

#!/usr/bin/python3

import sys


def print_stats(dict_sc, total_file_size):
    """Prints the statistics

    Args:
        dict_sc (Dict): A dictionary containing the counts of
        each status code

        total_file_size (Int): The total file size
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size_total = 0
code = 0
count = 0
dict_status_code = {"200": 0,
                    "301": 0,
                    "400": 0,
                    "401": 0,
                    "403": 0,
                    "404": 0,
                    "405": 0,
                    "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count += 1

            if count <= 10:
                file_size_total += int(parsed_line[0])
                code = parsed_line[1]

                if (code in dict_status_code.keys()):
                    dict_status_code[code] += 1

            if (count == 10):
                print_stats(dict_status_code, file_size_total)
                count = 0

finally:
    print_stats(dict_status_code, file_size_total)

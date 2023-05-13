#!/usr/bin/python3
"""
Metrics Computation Module

This module reads log lines from stdin, computes various metrics,
and prints the statistics based on the log lines.

The log lines are expected to have the following format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

"""
import sys
import re
from typing import TextIO


def compute_metrics(input_stream: TextIO) -> None:  # noqa
    """ Compute Metrics

    Reads log lines from stdin, computes the total file size,
    and counts the occurrences of each status code.

    Prints the statistics after every 10 lines and the final statistics
    when the program stops or encounters an exception.

    Args:
        input_stream (log): logs generated
    """

    # Initialize variables
    total_size = 0
    status_counts = {}
    line_number = 0

    # Regular expression pattern for matching the desired input format
    reg = r'^(\S+) - \[(.+)\] "GET \/projects\/\d+ HTTP\/\d.\d" (\d+) (\d+)$'

    try:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        # Process each line from stdin
        for line in input_stream:
            line = line.strip()

            # Check if the line matches the desired format
            match = re.match(reg, line)
            if not match:
                continue

            # Parse the matched groups from the line
            ip_address, date, stat_code, file_size = match.groups()

            # Update total file size
            try:
                """_summary_
    """
                file_size = int(file_size)
                total_size += file_size
            except ValueError:
                """_summary_
    """
                continue

            # Update status code counts
            try:
                """_summary_
    """
                stat_code = int(stat_code)
                status_counts[stat_code] = status_counts.get(stat_code, 0) + 1
            except ValueError:
                """_summary_
    """
                continue

            line_number += 1

            # Print statistics after every 10 lines
            if line_number % 10 == 0:
                print("File size:", total_size)
                for code in sorted(status_counts.keys()):
                    print(f"{code}: {status_counts[code]}")
                # print()

    except KeyboardInterrupt:
        """_summary_
    """
        #   Handle keyboard interruption (CTRL + C)
        #  print("File size:", total_size)
        #  for code in sorted(status_counts.keys()):
        #     print(f"{code}: {status_counts[code]}")
        sys.exit(0)


# Check if the module is run as a standalone script
if __name__ == '__main__':
    """_summary_
    """
    # Call the function to start computing metrics
    compute_metrics(sys.stdin)

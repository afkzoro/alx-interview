#!/usr/bin/python3
""" A python log parser that reads stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
<file size> (if the format is not this one, the line must be skipped)
"""
import sys
import re


def compute_metrics():
    """
    A python log parser that reads stdin line by line and computes metrics
    """

    # Initialize variables
    total_size = 0
    status_counts = {}
    line_number = 0

    # Regular expression pattern for matching the desired input format
    reg = r'^(\S+) - \[(.+)\] "GET \/projects\/\d+ HTTP\/\d.\d" (\d+) (\d+)$'

    try:
        # Process each line from stdin
        for line in sys.stdin:
            line = line.strip()

            # Check if the line matches the desired format
            match = re.match(reg, line)
            if not match:
                continue

            # Parse the matched groups from the line
            ip_address, date, stat_code, file_size = match.groups()

            # Update total file size
            try:
                file_size = int(file_size)
                total_size += file_size
            except ValueError:
                continue

            # Update status code counts
            try:
                stat_code = int(stat_code)
                status_counts[stat_code] = status_counts.get(stat_code, 0) + 1
            except ValueError:
                continue

            line_number += 1

            # Print statistics after every 10 lines
            if line_number % 10 == 0:
                print("File size:", total_size)
                for code in sorted(status_counts.keys()):
                    print(f"{code}: {status_counts[code]}")
                print()

    except KeyboardInterrupt:
        #   Handle keyboard interruption (CTRL + C)
        #  print("File size:", total_size)
        #  for code in sorted(status_counts.keys()):
        #     print(f"{code}: {status_counts[code]}")
        sys.exit(0)


compute_metrics()

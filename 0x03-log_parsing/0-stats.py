#!/usr/bin/python3
import sys
import re

# Initialize variables
total_size = 0
status_counts = {}
line_number = 0

# Regular expression pattern for matching the desired input format
pattern = r'^(\S+) - \[(.+)\] "GET \/projects\/\d+ HTTP\/\d.\d" (\d+) (\d+)$'

try:
    # Process each line from stdin
    for line in sys.stdin:
        line = line.strip()

        # Check if the line matches the desired format
        match = re.match(pattern, line)
        if not match:
            continue

        # Parse the matched groups from the line
        ip_address, date, status_code, file_size = match.groups()

        # Update total file size
        try:
            file_size = int(file_size)
            total_size += file_size
        except ValueError:
            continue

        # Update status code counts
        try:
            status_code = int(status_code)
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
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
    # Handle keyboard interruption (CTRL + C)
    # print("File size:", total_size)
    # for code in sorted(status_counts.keys()):
    #    print(f"{code}: {status_counts[code]}")
    sys.exit(0)

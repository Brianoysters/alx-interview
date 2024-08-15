#!/usr/bin/python3

'''
This script reads log entries from
standard input line by line and computes
specific metrics based on the input data.
Author: Brian Otieno <brianoysters@gmail.com>
'''

import sys
import signal
import re

# Initializes file size and dictionary for status code counts
tot_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
_line_count = 0

# Regex pattern to match the log format
log_pattern = re.compile(
    r'(?P<ip>[\d\.]+) - \[(?P<date>.*?)\] "(GET /projects/260 HTTP/1.1)" (?P<status>\d{3}) (?P<size>\d+)'
)

def print_metrics():
    '''
    Prints the current metrics including total file size and
    the count of each status code that has been recorded.
    '''
    print(f"File size: {tot_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    '''
    Handles the SIGINT signal (e.g., CTRL + C) to print metrics
    before the script exits.

    Arguments:
        sig : Signal number.
        frame : Current stack frame.
    '''
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    match = log_pattern.match(line)
    if match:
        status_code = match.group("status")
        file_size = int(match.group("size"))

        tot_file_size += file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        _line_count += 1

        if _line_count % 10 == 0:
            print_metrics()

print_metrics()


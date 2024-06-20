#!/usr/bin/python3
"""
A script: Reads standard input line by line and computes metrics
"""

import sys
import signal


import signal

# Initialize variables to hold the metrics
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def print_statistics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        
        # Validate format
        if len(parts) < 9:
            continue
        
        ip = parts[0]
        date = parts[3] + parts[4]
        request = parts[5] + ' ' + parts[6] + ' ' + parts[7]
        status_code = parts[-2]
        file_size = parts[-1]
        
        if not request.startswith('"GET /projects/260 HTTP/1.1"'):
            continue
        
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue
        
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        
        line_count += 1
        
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

# Final statistics after reading all lines
print_statistics()

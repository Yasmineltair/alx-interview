#!/usr/bin/python3
"""reads stdin line by line and computes metrics:"""

import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        line_lst = line.split(" ")
        if len(line_lst) > 4:
            code = line_lst[-2]
            size = int(line_lst[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            count += 1

        if count == 10:
            count = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
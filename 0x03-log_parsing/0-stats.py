#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics: """


import sys


def print_statistics(total_size, status_codes):
    """
    Implementation of statistics
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def main():
    """
    reads stdin line by line
    """
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) >= 10 and parts[-2].isdigit():
                total_size += int(parts[-1])
                status_code = parts[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    finally:
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()


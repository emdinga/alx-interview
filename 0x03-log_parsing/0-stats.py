#!/usr/bin/python3
""" Log parsing """


import sys



file_size_total = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            _, _, _, status_code_str, file_size_str = line.split()[-5:]
            status_code = int(status_code_str)
            file_size = int(file_size_str)
            file_size_total += file_size
            status_code_counts[status_code] += 1
        except (ValueError, IndexError):
            print(f"Skipping line {i}: Invalid format - {line.strip()}")
            continue

        if i % 10 == 0:
            print(f"File size: {file_size_total}")
            for code in sorted(status_code_counts):
                if status_code_counts[code] > 0:
                    print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    print(f"\nFile size: {file_size_total}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
    print("KeyboardInterrupt")



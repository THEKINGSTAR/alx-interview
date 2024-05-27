import re
import sys

status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0

std_in_line_re = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) - \[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+)\] "(GET \/projects\/260 HTTP\/1\.1)" (\d{3}) (\d+)')


def print_statistics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def output_metrics(line):
    global total_file_size, line_count
    match = std_in_line_re.match(line)
    if match:
        status_code = int(match.group(4))
        file_size = int(match.group(5))

        total_file_size += file_size
        status_counts[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_statistics()


try:
    for line in sys.stdin:
        output_metrics(line)

    if line_count % 10 != 0:
        print_statistics()
except KeyboardInterrupt:
    print_statistics()

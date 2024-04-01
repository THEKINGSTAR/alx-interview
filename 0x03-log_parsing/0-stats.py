#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C)
print these statistics from the beginning:
Number of lines by status code:
format: <status code>: <number>
status codes should be printed in ascending order
"""


import re
import sys


stus_cunt = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0

IP_Address_re = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
date_re = r'\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+\]'
status_code_re = r'\b(200|301|400|401|403|404|405|500)\b'
# file_size_re = r'[0-9]{3}$'
file_size_re = r'\d+$'
get = " \"GET /projects/260 HTTP/1.1\" "
get_re = r' "GET \/projects\/260 HTTP\/1\.1" '

std_in_line_re = re.compile(IP_Address_re + r' - ' +
                            date_re + get_re + status_code_re +
                            r' ' + file_size_re)


def if_match(input: str, regexp: str) -> str:
    """
    FUNCTION TO CHECK IF THE INPUT IS FOUND IN LINE OR NOT
    """
    match = re.search(regexp, input)
    if match:
        # print(f"Found: {match.group()}")
        return match.group()
    else:
        # print("Pattern not found.")
        return ""


def print_statistics() -> None:
    """
    FUNCTION TO PRINT LINES
    """
    print(f"File size: {total_file_size}")
    for code in sorted(stus_cunt.keys()):
        if stus_cunt[code] > 0:
            print(f"{code}: {stus_cunt[code]}")


def output_metrics(line: str) -> None:
    """
    FUNCTION TO GET THE STD_IN AS INPUT
    AND
    SEPERATE IT
    CALCULATE
    AND PRINT THE RESULTS
    """
    global total_file_size, line_count
    line = line.rstrip()
    match = std_in_line_re.match(line)
    if match:
        IP_Address = if_match(line, IP_Address_re)
        date = if_match(line, date_re)
        status_code = if_match(line, status_code_re)
        status_code = int(status_code)
        file_size = if_match(line, file_size_re)
        file_size = int(file_size)

        total_file_size += file_size
        stus_cunt[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_statistics()
    else:
        status_code = if_match(line, status_code_re)
        file_size = if_match(line, file_size_re)
        if file_size:
            if status_code:
                status_code = int(status_code)
                stus_cunt[status_code] += 1

            file_size = int(file_size)
            total_file_size += file_size
            line_count += 1

        if line_count % 10 == 0:
            print_statistics()


try:
    if sys.stdin.isatty():
        print(f"File size: {total_file_size}")
        print_statistics()
    else:
        for line in sys.stdin:
            output_metrics(line)

    if line_count % 10 != 0:
        print_statistics()
except KeyboardInterrupt:
    print_statistics()

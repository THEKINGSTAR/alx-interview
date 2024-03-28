#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
"""
file_size = 0
status_code =[200, 301, 400, 401, 403, 404, 405, 500]
date = ''
IP_Address = ''
total_size = 0

# Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>


import sys
print('Write a message and press Enter: ')
for line in sys.stdin:
    line = line.rstrip()
    print(f'Message from stdin: {line}')
    break
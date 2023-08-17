# Usage: write_to_file.py FILENAME message

import sys

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as file:
    file.write(message)
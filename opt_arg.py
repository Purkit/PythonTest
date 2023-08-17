# Demonstrating Optional CLI Arguments:

import sys
import getopt

filename = "test.txt" # Default file name
message  = "Hello"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as file:
    file.write(message)
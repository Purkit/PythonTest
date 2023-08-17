# Parsing command line parameters

def myFunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEY_ONE'])
    print(kwargs['KEY_TWO'])

myFunction('hey', 19, True, 'wow', KEY_ONE=2, KEY_TWO=5)
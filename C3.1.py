def right_justify(s):
    length = len(s)
    space = ' ' * (70 - length)
    print space + s
    return

right_justify('monty')

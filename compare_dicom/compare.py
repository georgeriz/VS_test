with open('example') as f:
    d = {line.split()[0]: line.split('[')[1].split(']')[0] for line in f}

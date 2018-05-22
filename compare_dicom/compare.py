def get_dict(filename):
    with open(filename) as f:
        return {line.split()[0]: line.split('[')[1].split(']')[0] for line in f}

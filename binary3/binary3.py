import re

def is_binary3(s):
    PATTERN = re.compile(r'^(0+|(1(01*0)*1)+)+$')
    return bool(PATTERN.match(s))
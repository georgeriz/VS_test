import re

def foo(msg):
    return re.findall(r'bug-\d+', msg)
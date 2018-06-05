import re

def foo(msg):
    return re.findall(r'bug-\d+', msg)

def bar(msg):
    return "Did you mean {} ?".format(" and ".join(map(lambda x: "http://jira.com/" + x, foo(msg))))
import re

def get_match(msg, pattern):
    return re.findall(pattern + r'\d+', msg, re.IGNORECASE)

def get_links(msg):
    return ["http://jira.com/" + match.upper() for match in get_match(msg, "BUG-")]

def get_links2(msg):
    links = []
    for word in msg.split():
        if word.startswith("BUG-"):
            links.append("http://jira.com/" + word.strip(".,!?:"))
        elif word.startswith("CR-"):
            links.append("goto.com/" + word.strip(".,!?:"))
    return links
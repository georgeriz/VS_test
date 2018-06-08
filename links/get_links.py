import re

def get_links(msg):
    links = ["http://jira.com/" + match.upper() for match in re.findall(r'BUG-\d+', msg, re.IGNORECASE)]
    links.extend(["goto.com/" + match.upper() for match in re.findall(r'CR(?:-[a-z0-9]{4}){2}', msg, re.IGNORECASE)])
    return filter(lambda link: link.upper() not in msg.upper(), links)

def get_links2(msg):
    links = []
    for word in msg.split():
        if word.startswith("BUG-"):
            links.append("http://jira.com/" + word.strip(".,!?:"))
        elif word.startswith("CR-"):
            links.append("goto.com/" + word.strip(".,!?:"))
    return links
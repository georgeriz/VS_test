def get_links(msg):
    links = []
    for word in msg.split():
        if word.startswith("BUG-"):
            links.append("http://jira.com/" + word.strip(".,!?:"))
        elif word.startswith("CR-"):
            links.append("goto.com/" + word.strip(".,!?:"))
    return links
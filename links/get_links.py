def get_links(msg):
    links = []
    for word in msg.split():
        if word.startswith("bug-"):
            links.append("http://jira.com/" + word)
        elif word.startswith("cr-"):
            links.append("goto.com/" + word)
    return links
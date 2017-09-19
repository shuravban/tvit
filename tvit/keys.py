import re
import os

RCFILE=os.path.join(os.environ['HOME'], '.trc')


def keys(user=None, rcfile=None):
    if not rcfile:
        rcfile = RCFILE
    rc = open(rcfile).read()

    if not user:
        user = re.findall(r'default_profile:\n\s+-\s+(\w+?)\n', rc)[0]

    keys = {}
    for s in re.findall(r'username:.*?\n(?:.*?\n){4}', rc):
        v = re.split(r'[:\s]+', s)
        keys[v[1]] = [v[3], v[5], v[7], v[9]]

    return keys[user]

import re

def solution(new_id):
    new_id = new_id.lower()

    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)

    new_id = re.sub(r'\.{2,}', '.', new_id)

    new_id = new_id.strip('.')

    if new_id == '':
        new_id = 'a'

    new_id = new_id[:15]
    new_id = new_id.rstrip('.')

    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
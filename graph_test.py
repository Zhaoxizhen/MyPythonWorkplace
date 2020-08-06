from collections import deque

graph = dict()
graph['you'] = ['bob', 'alice', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['thom'] = []
graph['jonny'] = []
graph['peggy'] = []


def is_mango_seller(person):
    if person[-1] == 'm':
        return True
    else:
        return False


def graph_search(name):
    que = deque()
    que += graph[name]
    checked = []
    while que:
        person = deque.popleft(que)
        if person not in checked:
            if is_mango_seller(person):
                return True
            else:
                checked.append(person)
                que += graph[person]
    return False


print(graph_search('you'))

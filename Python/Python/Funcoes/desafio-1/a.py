from lib import get_data
from typing import List, Dict


def is_connected(relations: Dict[str,List[str]] , a : str, b : str):
    route = [a]
    
    while not(b in route) and route != []:
        if relations[route[-1]] == []:
            route.pop()
            continue
        route.append(relations[route[-1]].pop(0))
    
    return route

entidades : Dict[str, List[str]]= get_data('./data.txt')
r = is_connected(entidades, '23', '5')
print(r)
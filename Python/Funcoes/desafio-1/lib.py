import random as rd
from typing import List, Dict

def get_data(path : str) -> Dict[str,List[str]]:
    e : Dict[str,List[str]] = {}
    with open(path, 'r') as file:
        for line in file.readlines():
            data = line.split(':')

            name      = data[0].strip()
            relations = data[1].strip()

            relations = relations.strip('[')
            relations = relations.strip(']')
            relations = relations.split(',')
            for i in range(len(relations)):
                relations[i] = relations[i].strip()
                if relations[i] == '':
                    relations.remove('')
            e[name] = relations
    return e


def generate(length : int) -> None:
    e : Dict[int,List[int]] = {i : [] for i in range(length)}

    for i in range(length):
        relations = rd.randint(0,3)
        for _ in range(relations):
            e[i].append(rd.randint(1,length))
    with open('data.txt', 'w') as file:
        file.writelines('')
    with open('data.txt', 'a') as file:
        for name in e:
            file.write(f'{name+1} : {e[name]}\n')
        
import os

root = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Python/Bibliotecas Python/OS/Challenge/Bagunça"
root_list = os.listdir(root)
        
for arq in root_list:
    folder = arq[arq.rfind('.') + 1:]
    
    if len(folder) <= 1:
        continue
    
    if not folder in root_list:
        os.mkdir(os.path.join(root, folder))
        root_list.append(folder)
    
    new_dir = os.path.join(root, folder, arq)
    aux = os.path.join(root, arq)

    os.rename(aux, new_dir)
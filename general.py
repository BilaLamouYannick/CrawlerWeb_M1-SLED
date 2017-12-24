import os


# Chaque website est un projet séparé (chemise) 
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Créez la file d'attente et les fichiers crawler (si non créé) 
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Créez un nouveau fichier
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Ajoutez les données sur un fichier existant 
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Effacez le contenu d'un fichier 
def delete_file_contents(path):
    open(path, 'w').close()


# Lire un fichier et convertissez chaque ligne en éléments de positionnement 
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Réitérez par un positionnement, chaque élément sera une ligne dans un fichier 
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")

from urllib.parse import urlparse


# Obtenir le nom de domaine (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# Rester dans le domaine de recherche
def stay_domaine_search(url):
    try:
        path = urlparse(url).path
        query = urlparse(url).query
        return (path, query)
    except:
        return ('', '')

# Obtenir le nom de domaine supérieur (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

# Vérifier si le chemin reference l'aplication
def get_path_name(url):
    try:
        return urlparse(url).path
    except:
        return '' 

# Obtenir juste l'adresse des applications (?id = manger.dormir.crieer)
def get_app_name(url):
    try:
        return urlparse(url).query
    except:
        return ''
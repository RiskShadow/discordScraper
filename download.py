import requests

def download(list, i):
    for link in list:
        open('Output/' + str(i) + '.' + link.split("/")[-1].split('.')[-1], 'wb').write(requests.get(link, allow_redirects=True).content)
        i = i + 1

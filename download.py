import requests


def download(url, file_name):

    with open(file_name, "wb") as file:

        response = requests.get(url)

        file.write(response.content)
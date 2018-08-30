import requests
from bs4 import BeautifulSoup
import re
# Unica super clase de la aplicación. Sirve como estructura para las siguientes clases
class Scraping(object):
    # Recibe una URL
    def __init__(self,url):
        # Obtener la URL
        self.__url = url
        # Realizamos una petición y la respuesta la convertimos en texto.
        self.__request = requests.get(self.__url).text
        # Creamos un objeto de soup para realizar el web scraping formateando lo resultante como un fichero HTML.
        self.__soup = BeautifulSoup(self.__request, 'html.parser')

    # GETTER'S
    @property
    def url(self):
        return self.__url

    @property
    def soup(self):
        return self.__soup
        
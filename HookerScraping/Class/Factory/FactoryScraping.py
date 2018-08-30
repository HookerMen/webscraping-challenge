from HookerScraping.Class.ScrapingBook import ScrapingBook
from HookerScraping.Class.ScrapingPage import ScrapingPage
from HookerScraping.Class.ScrapingList import ScrapingList
from HookerScraping.Class.Scraping import Scraping
# Esta clase cumple el rol de Fabrica(Factory), con el objetivo de crear clases según la necesidad en el instante.
class FactoryScraping():
    # Metodo statico
    @staticmethod
    # funcion encargada de crear y retornar un objeto segun necesidad, definida en la variable tipo, ademas enviando la url a filtrar.
    def get_soup(tipo,url):
        # Si el tipo es book, se creara un objeto de la clase ScrapingBook.
        if tipo == "book":
            return ScrapingBook(url)
        # Si el tipo es page, se creara un objeto de la clase ScrapingPage.
        elif tipo == "page":
            return ScrapingPage(url)
        # De lo contrario, se creara un objeto de la clase ScrapingList.
        else:
            return ScrapingList(url)
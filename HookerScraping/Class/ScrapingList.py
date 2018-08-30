
from HookerScraping.Class.Scraping import Scraping
# Esta clase extiende de Scraping, permitiendonos extraer las listas por pagina.
class ScrapingList(Scraping):
    def __init__(self,url):
        super(ScrapingList,self).__init__(url)
    
    # FUNCIONES Y PROCEDIMIENTOS
    # Encargado de retornar las filas en una pagina.
    def list_book(self):
        return self.soup.find('ol').find_all('li')
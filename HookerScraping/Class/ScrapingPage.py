from HookerScraping.Class.Scraping import Scraping
import re
# Esta clase extiende de Scraping, permitiendonos extraer Paginas del sitio web, ademas de saber el total de paginas.
class ScrapingPage(Scraping):
    def __init__(self,url):
        super(ScrapingPage,self).__init__(url)
    # FUNCIONES Y PROCEDIMIENTOS
    # Funcion encargada de obtener el maximo número de paginas del sitio web.
    def max_pages(self):
        # Definimos el patron encargado de obtener el numero maximo de paginas (of ##).
        pattern = "(of\s[0-9]{1,}){1}"
        # Obtenemos el fragmento de codigo donde se cuentra el numero maximo.
        li_current = self.soup.find('li', class_="current").string
        # Aplicamos el patron y separamos el contenido cortando el caracter " " que se encuentra en medio del numero y la palabra.
        #[0]-> "of", [1] -> 50
        pages = re.search(pattern,li_current).group().split(" ")[1]
        # Finalmente retornamos el numero maximo.
        return int(pages)

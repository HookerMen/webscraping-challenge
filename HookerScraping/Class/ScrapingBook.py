from HookerScraping.Class.Scraping import Scraping
from HookerScraping.Class.Book import Book
import re
# Esta clase extiende de Scraping, permitiendonos extraer un libro.
class ScrapingBook(Scraping):
    def __init__(self,url):
        super(ScrapingBook,self).__init__(url)
    # FUNCIONES Y PROCEDIMIENTOS
    # Nos permite obtener un libro.
    def get_book(self):
        # Este variable necesita pasar por alguna validaciones.
        description = {}
        # Nos dirigimos a la tabla de descripcion del libro.
        for desc in self.soup.find('table', class_="table table-striped").find_all('tr'):
            # Luego obtenemos y definimos una variable para la clave y el valor.
            key = desc.find('th').string; value = desc.find('td').string
            # Seguidamente validamos el key pertenece a dinero, logrando con esto a que por defecto sea numerico
            if key == "Price (excl. tax)" or key == "Price (incl. tax)" or key == "Tax":
                value = value[2:]
            # En este caso necesitamos realizar una expresion regular, con el objetivo de obtener los numeros del objeto
            elif key == "Availability":
                value = re.search(r'(\d)+', value).group()
            # Finalmente creamos el diccionario.
            description[key]=value
        # Cuando el paso anterior fue llevado a caso, pasamos a la etapa de crear el objeto libro.
        return Book(
            # Obtenemos el titulo del libro.
            self.soup.find('h1').string,
            # Obtenemos el precio del libro.
            self.soup.find('p', class_="price_color").string[2:],
            # Obtenemos la disponibilidad.
            re.search(r"(\d)+", str(self.soup.find('div', class_='product_main').find('p', class_="instock availability")) ).group(),
            # Obtenemos la Categoria.
            self.soup.find('ul', class_='breadcrumb').find_all('li')[2].find('a').string,
            # Obtenemos el Cover.
            self.soup.find('div',class_="item active").find('img')['src'],
            # Asignamos la descripción.
            description
        )

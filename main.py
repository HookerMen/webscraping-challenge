# -*- coding: utf-8 -*-
import datetime
from HookerScraping.Class.Factory.FactoryScraping import FactoryScraping
from HookerScraping.Class.Reports import Reports


def main():
    # Dirección URL principal del sitio web.
    url = "http://books.toscrape.com/"
    print(f"\nBienvenidos a el programa de Web Scraping, Realizado por @HookerMen.\n")
    print(f"Procederemos a realizar Web Scraping a {url} .")
    # Lista de los libros totales del sitio web.
    books = []
    # Cantidad totalde paginas del sitio web.
    pages = FactoryScraping.get_soup('page',url)
    print(f"El sitio web {url} tiene un paginator volumen {pages.max_pages()}.\n")
    print(f"Procediendo a recorrer paginator...\n")
    # Recorremos cada pagina en busca de los listados de libros, pertenecientes a cada pagina.
    for page in range(1,pages.max_pages()+1):
        # Obtenemos el listado de libros de la pagina.
        list_book = FactoryScraping.get_soup("list",f"{url}catalogue/page-{page}.html").list_book()
        # Recorremos la lista de libros, Con el objetivo de obtener la ruta perteneciente a cada libro.
        for link_book in list_book:
            # Cuando ya tenemos la ruta del libro, procedemos a capturarlo.
            book = FactoryScraping.get_soup("book",f"{url}catalogue/{link_book.find('a')['href']}").get_book()
            # Para posteriormente agregarlo a la lista de libros.
            books.append(book)
        else:
            # Comentario para indicar en que numero de pagina estamos trabajando.
            print(f"Pagina {page}/{pages.max_pages()}")
    else:
        # Definimos la estructura de columnas a mostrar en el reporte.
        columns = [
            "Title",
            "Price",
            "Stock",
            "Category",
            "Cover",
            "UPC",
            "Product Type",
            "Price (excl. tax)",
            "Price (incl. tax)",
            "Tax",
            "Availability",
            "Number of reviews"
        ]
        # Ademas del nombre del fichero, el cual tendra la fecha y hora del reporte.
        name_file = f"R_{datetime.datetime.now()}.csv"
        # Seguidamente creamos el reporte, enviando como parametro las columnas, los libros y el nombre del reporte.
        Reports().create_csv(columns,books,name_file)
        # Para terminar enviamos el mensaje que se ha generado correctamente el reporte.
        print(f"Se ha generado el reporte de manera correcta con el nombre: {name_file}, ubicado en /Report.")

if __name__ == "__main__":
    main()

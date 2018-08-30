import pandas as pd
# Clase encargada de generar los reportes.
class Reports():
    # metodo estatico, no se necesita instanciar la clase.
    @staticmethod
    # metodo crear csv, el cual recibe(columnas, libros, nombre_reporte)
    def create_csv( columns, list_data, name):
        # Creamos una lista de libro para darle el formato correcto.
        books=[]
        # Recorremos los libros(los que recibimos como parametro) sin formato.
        for data in list_data:
            # Definimos la variable book para asignarle el valor del libro en este momento, dandole formato deseado.
            book = {
                "Title": data.title,
                "Price": data.price,
                "Stock": data.stock,
                "Category": data.category,
                "Cover": data.cover,
                "UPC": str(data.description["UPC"]),
                "Product Type": str(data.description["Product Type"]),
                "Price (excl. tax)": str(data.description["Price (excl. tax)"]),
                "Price (incl. tax)": str(data.description["Price (incl. tax)"]),
                "Tax": str(data.description["Tax"]),
                "Availability": str(data.description["Availability"]),
                "Number of reviews": int(data.description["Number of reviews"])
            }
            # Añadimos el libro a la lista de libros formateados
            books.append(book)
        # Creamos un DataFrame para tener nuestros datos mas ordenados, incluyendo(libros formateados y las columnas)
        df = pd.DataFrame(books, columns = columns)
        # Finalmente creamos el reporte con nombre y formato.
        return df.to_csv(f"HookerScraping/Report/{name}",sep=",",encoding="utf-8")

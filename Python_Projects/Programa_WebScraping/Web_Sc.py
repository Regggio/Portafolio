import bs4
import requests

url = "https://books.toscrape.com/catalogue/page-{}.html" #Se ponen llaves para despues poder ir pasando de pagina
lista_libros_altos = []

for n in range(1,51):
    "Creo mi sopa para cada pagina"
    url_pag = url.format(n) #Me permite ir poniendo el numero de pagina
    pagina_actual = requests.get(url_pag) #Guardo el codigo fuente de la pagina actual
    sopa_act = bs4.BeautifulSoup(pagina_actual.text,"html.parser")

    "Selecciono datos de los libros"
    libros = sopa_act.select(".product_pod") #Me devuelve la contencion de cada libro en la pagina

    "Iterar Libros"
    for libro in libros:
        "Chequear que tiene 4 o 5 estrellas"
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) !=0 : #Se pone un punto entre la clase y el numero porque en el codigo tienen un espacio
            "Guardar titulo del libro"
            titulo = libro.select('a')[1]['title']
            lista_libros_altos.append(titulo)

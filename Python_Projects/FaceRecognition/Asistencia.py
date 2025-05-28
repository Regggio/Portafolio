import cv2
import face_recognition as fr
import os
import numpy
from _datetime import datetime

"Crear Base de datos"
ruta  = 'Empleados'
lista_img_empleados = []
lista_nombres_empleados = []
empleados_act = os.listdir(ruta) #Obtengo un listado con todas los nombres de las fotos de los empelados

for empleado in empleados_act:
    img_act = cv2.imread(f'{ruta}\{empleado}') #cv2.imread lee la imagen en cuestion
    lista_img_empleados.append(img_act)
    lista_nombres_empleados.append(os.path.splitext(empleado)[0]) #Splitext divide al archivo en una tupla con su nombre y su ruta

"Codificar Img"
def codificar(imgs):
    lista_codificada = [] #Se crea una lista codificada para poder trabajar con FaceRecognition

    for img in imgs: #paso todos las img de la lista a RGB
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        codificado = fr.face_encodings(img)[0] #Ayuda a que el sistema nos diga en que ubicacion esta la cara en los bits de la foto

        lista_codificada.append(codificado) #Agregamos a la lista la imagen ya codificada

    return lista_codificada #Se devuevle la lista codificada

"Registrar Ingresos"
def registrar_ingresos(persona):
    f = open("registro.csv","r+")
    lista_datos = f.readlines() #Creo una lista con todo el contenido de mi archivo
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(",") #Separo los campos por su delimitante que es la coma
        nombres_registro.append(ingreso[0]) #En el indice 0 esta el nombre del empleado

    if persona not in nombres_registro: #Nos fijamos si la persona se encuentra ya dentro del trabajo
        ahora = datetime.now() #Guardamos la hora del ingreso
        str_ahora = ahora.strftime("%H:%M:%S") #Convertimos nuestra variable time en una variable de tipo string
        f.writelines(f'\n{persona}, {str_ahora}') #Escribimos en el registro la persona y el horario de ingreso


lista_cod = codificar(lista_img_empleados)

"Tomo una imagen de CamaraWeb"
captura = cv2.VideoCapture(0,cv2.CAP_DSHOW) #Se toma una imagen de la camara Web en cuestion

"Verificacion de la captura de la camara"
exito, img_cw = captura.read() #Este metodo devuelve  dos elementos, si se pudo tomar la captura y la captura en cuestion

if not exito:
    print("No se pudo tomar un captura con la camara del ordenador")
else:
    "Reconocer la cara"
    cara_captura = fr.face_locations(img_cw) #Devuelve las cuatro coordenadas que encuadran nuestra cara

    "Codificar la cara"
    cara_capturada_codificada = fr.face_encodings(img_cw, cara_captura)

    "Buscar Coincidencias en la BBDD"
    for caracodif, caraubic in zip(cara_capturada_codificada,cara_captura): #Usamos un zip ya que queremos comparar ambos elementos en un mismo loop
        coincidecnia = fr.compare_faces(lista_cod, caracodif) #Tira el resultado si hubo coincidencia o no
        distancaias = fr.face_distance(lista_cod,caracodif) #Tira informacion de la distancia que hay entre ellas

        indice_coincidencia = numpy.argmin(distancaias) #Me devuelve el valor menor dentro de una lista

        "Mostrar coincdiencias si las hay"
        if distancaias[indice_coincidencia] > 0.6:
            print("No hay coincidencia con ninguno de nuestros empleados")
        else:
            "Buscamos el nombre del empleado encontrados"
            nombre = lista_nombres_empleados[indice_coincidencia] #Almaceno el nombre correspondiente a la imagen que tuvo coincidencia

            "Genero reacurador de la cara"
            y1, x2, y2, x1 = caraubic #Devuelve cuatro ubicaciones siendo pixeles del recuadro de la cara en la imagen
            cv2.rectangle(img_cw,
                          (x1,y1), #Esta tupla nos da el vertice superior izquierdo
                          (x2,y2), #Esta tupla nos da el vertice inferior derecho
                          (0,255,0), #Color en RGB
                          2) #Grosor
            cv2.putText(img_cw, nombre, (50,50), cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0))

            registrar_ingresos(nombre)

            "Muestro la img obtenida"
            cv2.imshow('Img Camara Web',img_cw)

            "Mantener ventana abierta"
            cv2.waitKey(0)


import pyttsx3 #Es la libreria que nos permite que la maquina hable con nosotros
import speech_recognition as sr #Es la libreria que nos permite traducir nuestra voz a texto
import pywhatkit #Es la liberaria que permite a nuestro programa acceder a paginas web
import webbrowser #Es la libreria que nos permite navegar en el internet
import datetime
import wikipedia

"Traducir audio a texto"
def trasnfromar_audio_to_txt():
    #Almacear variable recognizer
    r = sr.Recognizer() #Recognizer se utiliza para variables que puedan comprender audio

    "Configuramos el microfono"
    with sr.Microphone() as origen: #sr.Microphone() nos permite trabajar con los elemntos de nuestro microfono

        "Espera previa a comenzar grabacion"
        r.pause_threshold = 0.8 #Tiempo que retrasa el programa antes de empezar a recibir audio

        print("ya puedes hablar")

        "Guardar lo que se escuche como audio"
        audio = r.listen(origen) #Almacena en una variable lo producido por el microfono

        try:
            #Verificamos si la grabacion es lo suficientemente nitida como para buscar lo pedido en google
            pedido = r.recognize_google(audio, language = "es-ar") #Pedido tiene en formato texto lo que dijimos por el audio

            print(f"Dijiste: {pedido}")

            "Devuelvo lo que dije en formato string"
            return pedido

        except sr.UnknownValueError or sr.RequestError: #En caso de que falle el entendimiento del audio
            print("Ups no entendi el audio")
            return "sigo esperando"

        except: #Cualquier otro error
            print("Ups, un error inesperado ah ocurrido")
            return "sigo esperando"

"Funcion para que el asisntete hable"
def hablar(msj):
    engine = pyttsx3.init() #Arranco el funcionamiento de pyttsx3

    engine.say(msj) #El asistente dice lo transmitido por mensaje
    engine.runAndWait() #Espera a la siguiente instruccion

"informar dia de la semana"
def pedir_dia():
    dia_act = datetime.date.today()
    dicc_dia_semana = {0: 'Lunes',
                       1: 'Martes',
                       2: 'Miércoles',
                       3: 'Jueves',
                       4: 'Viernes',
                       5: 'Sábado',
                       6: 'Domingo'}
    hablar(f'Hoy es el día {dicc_dia_semana[dia_act.weekday()]}') #Obtiene el dia de la semana actual en base a la clave del diccionario

"informar hora"
def pedir_hora():
    hora = datetime.datetime.now()
    if hora.hour <= 12:
        hablar(f'Actualmente son las {hora.hour} AM')
    else:
        hablar(f'Actualmente son las {hora.hour-12} PM')

"Funcion inicial del asistente"
def saludo_ini():
    hablar(f"Hola soy tu asistente virtual. Dime en que te puedo ayudar")


"Funcion para recibir pedidos"
def pedidos():
    saludo_ini()
    comenzar = True
    "Loop para que el programa sigue en ejecucion hasta que se pida salir"
    while comenzar:

        "Guardar el pedido en un string a travez del micro"
        pedido = trasnfromar_audio_to_txt().lower()

        if "abrir youtube" in pedido:
            hablar("Ok, estoy abriendo youtube")
            webbrowser.open('https://www.youtube.com/') #sirve para abrir un navegador en la pagina indicada

        elif "abrir internet" in pedido:
            hablar("Ok, estoy abriendo un navegador ahora mismo")
            webbrowser.open("https://www.google.com.ar")

        elif "qué día es hoy" in pedido:
            pedir_dia()

        elif "qué hora es" in pedido:
            pedir_hora()

        elif "busca en wikipedia" in pedido:
            hablar("Muy bien, buscando tu pedido en wikipedia")
            pedido = pedido.replace("busca en wikipedia",'')#Limpio para que solo me busque le pido y no toda mi oracion
            wikipedia.set_lang('es') #Le digo que busque en wikipedia en espaniol
            resultado = wikipedia.summary(pedido, sentences = 1) #Le digo que me devuelva el primer parrafo de lo buscado
            hablar("Wikipedia nos dice:")
            hablar(resultado)

        elif "busca en internet" in pedido:
            hablar("ok, buscando")
            pedido = pedido.replace("busca en internet", '')
            pywhatkit.search(pedido) #Busca en el navegador de google lo pedido
            hablar("Muy bien, esto es lo que eh encontrado")

        elif 'reproducir' in pedido:
            hablar("Buscando video")
            pywhatkit.playonyt(pedido) #Empieza a reproducir un video en youtube

        elif "quiero salir" in pedido:
            hablar("Muy bien, nos vemos la próxima")
            comenzar = False

pedidos()
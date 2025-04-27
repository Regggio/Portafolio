import math
import pygame
import random
from pygame import mixer
import io

"Necesario para que sea un ejecutable"
def fuente_bytes(fuente_juego):
    # Abre el archivo TTF en modo lectura binaria
    with open(fuente_juego, 'rb') as f:
        # Lee todos los bytes del arch y los almacena en una variable
        ttf_bytes = f.read()
        # Crea un objeto BytesIO a partir de los bytes del archivo TTF
        return io.BytesIO(ttf_bytes)

pygame.init() #Incializar pygame

pantalla = pygame.display.set_mode((800,600)) #Establezco el tamanio de la pantalla

"Titulo e Icono"
pygame.display.set_caption("Space Invaders") #Pongo un titulo a mi ventana
icono  = pygame.image.load("astronave.png") #Cargo la imagen de mi icono en una variable
pygame.display.set_icon(icono) #Establezco el icono de mi ventana a la imagen correspondiente
fondo = pygame.image.load("fondo_img.jpg")

"Agregar musica"
mixer.music.load("MusicaFondo.mp3") #Le digo al programa que esta es la musica que debe poner a andar
mixer.music.set_volume(0.1) #Le digo el volumen en el que debe estar (entre 0 y 1)
mixer.music.play(-1) #Le digo que la musica me la debe hacer andar en loop



"Crear Jugador"
img_jugador = pygame.image.load("jugador.png") #Cargo la imagen de mi jugador en una variable
#Establezco las coordenadas de mi jugador en mi pantalla
jugador_x = 368 #Se elije este numero porque la mitad de 800 es 400 y la mitad de mi jugador es 36 xq es de 64px y asi queda en el medio
jugador_y = 500 #Se elije este numero porque queremos que arranque en la base y como mi icono es de 64px hay que subirlo esa cantidad
jugador_x_cambio = 0 #Se usa para que el jugador tenga un movimiento conituno en vez de ir tocando cada vez

"Ubicacion jugador"
def jugador(pos_x,pos_y): #Funcion que  pone a mi jugador en la ventana
    pantalla.blit(img_jugador,(pos_x,pos_y))

"Crear Enemigo"
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = [] #Para que este en perpetuo movimiento
enemigo_y_cambio = [] #altura que baja la nave cada vez que toca un borde de la ventana
cant_enemigos = 7
for e in range(cant_enemigos):
    img_enemigo.append(pygame.image.load("alien.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(0, 200))
    enemigo_x_cambio.append(0.3) #Para que este en perpetuo movimiento
    enemigo_y_cambio.append(64) #altura que baja la nave cada vez que toca un borde de la ventana

"Ubicacion enemigo"
def enemigo(pos_x,pos_y,i):
    pantalla.blit(img_enemigo[i],(pos_x,pos_y))

"Evita que el enemigo exceda el borde inferior de la pantalla"
def cambiar_altura_enemigo(altura,cambio):
    if altura + cambio < 500:
        return altura + cambio
    else:
        return 500

'Crar bala'
img_bala = pygame.image.load("bala.png")
bala_y = 468
bala_x = 0
bala_y_cambio = 1 #altura que baja la nave cada vez que toca un borde de la ventana
visibilidad_bala = False

"ubicar bala"
def bala(pos_x, pos_y):
    global visibilidad_bala
    visibilidad_bala = True
    pantalla.blit(img_bala,(pos_x + 16,pos_y))

"Control puntaje"
puntos = 0
fuente_como_bytes = fuente_bytes("FreeSansBold.ttf")
fuente = pygame.font.Font(fuente_como_bytes,32)

"Funcion mostrar puntaje en pantalla"
def puntje(): #Se debe armar un texto para mostrar en pantalla
    texto = fuente.render(f"Puntaje: {puntos}",True,(255,255,255))
    pantalla.blit(texto,(12,12))

"Texto final del juego"
fuente_final = pygame.font.Font(fuente_como_bytes,64)

"Funcion mostrar texto final en pantalla"
def texto_final():
    textoF = fuente_final.render("GAME OVER",True,(255,255,255))
    pantalla.blit(textoF,(186,236))

"Funcion para detectar colision"
def detect_colision(x1,y1,x2,y2): #Devulve True si hay colision y Flase si no
    distancia = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2)) #Formula matematica para calular la distancia entre dos puntos
    if distancia < 27: #Se elije este numero ya que mi bala ocupa 32 pixeles, si estan a 27 pixeles de distancaia se puede considerar que hubo choque
        return True
    else:
        return False

"LOOP DEL JUEGO"
se_ejecuta = True
while se_ejecuta:
    pantalla.blit(fondo,(0,0))  # Determino el fondo de mi pantalla, debe arrancar en 0,0 ya
    "Iterar eventos"
    for evento in pygame.event.get():  #Obtengo los eventos que estan ocurriendo ahora mismo en mi pantalla

        if evento.type == pygame.QUIT: #Si el evento es que el usuario toco la x de la ventana
            se_ejecuta = False  #Salgo y termino la ejecucion

        if evento.type == pygame.KEYDOWN: #Acciones que realiza cuando se toco una tecla
            if evento.key == pygame.K_LEFT: #Si la tecla es la felcha izquierda
                jugador_x_cambio -= 0.3
            if evento.key == pygame.K_RIGHT: #Si la teclas es la flecha derecha
                jugador_x_cambio += 0.3
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3") #Agrego el sonido que quiero que se haga cada vez que disparo
                sonido_bala.set_volume(0.2)
                if not visibilidad_bala:
                    sonido_bala.play()
                    bala_x = jugador_x  # Defino que la bala salga de la posicion del jugador y despues mantenga su trayecto
                    bala(bala_x, bala_y)


        if evento.type == pygame.KEYUP: #Acciones que realiza cuando se deja de tocar una tecla
            if evento.key == pygame.K_LEFT or pygame.K_RIGHT:
                jugador_x_cambio = 0 #resetea el valor del movimiento

    'Modificar ubicacion jugador'
    jugador_x += jugador_x_cambio #Permite que la nave se mueva continuamente hacia la direccion mientras se presiona la tecla

    "Mantener jugador dentro de pantalla"
    if jugador_x < 0: #Se fija que la imagen del jugador no exceda el borde izq de la pantalla
        jugador_x = 0
    elif jugador_x > 736: #Se fija que la imagen del jugador no exceda el borde derecho de la pantalla
        jugador_x = 736 #Usa este numero porque la imagen ocupa 64px

    'Modificar ubicacion enemigo'
    for e in range(cant_enemigos):

        "Chequeo fin del juego"
        if enemigo_y[e] >= 500: #Me fijo si el enemigo esta en el mimso nivel que mi nave
            for k in range(cant_enemigos): #Por cada enemigo que haya cumplido esa condicion
                enemigo_y[k] = 1000 #Lo saco de la pantalla
            texto_final()
            break #Una vez que modifica al enemigo que necesita sale

        enemigo_x[e] += enemigo_x_cambio[e]  # Permite que la nave se mueva continuamente hacia la direccion

        "Mantener enemigo dentro de pantalla"
        if enemigo_x[e] < 0:  # Se fija que la imagen del enemigo no exceda el borde izq de la pantalla
            enemigo_x_cambio[e] = -enemigo_x_cambio[e]#cambia el sentido de movimento del enemigo
            enemigo_y[e] = cambiar_altura_enemigo(enemigo_y[e] ,enemigo_y_cambio[e])
        elif enemigo_x[e]  > 736:  # Se fija que la imagen del enemigo no exceda el borde derecho de la pantalla
            enemigo_x_cambio[e]  = -enemigo_x_cambio[e]
            enemigo_y[e]  = cambiar_altura_enemigo(enemigo_y[e] , enemigo_y_cambio[e]) #Establece la nueva altura o lo mantiene en el borde inferior de la pantalla
        "Colision"
        colision = detect_colision(bala_x, bala_y, enemigo_x[e], enemigo_y[e])
        if colision:  # Si hay choque entre bala y enemigo
            sonido_colision = mixer.Sound("Golpe.mp3")
            sonido_colision.set_volume(0.1)
            sonido_colision.play()
            bala_y = 468
            visibilidad_bala = False  # Se utiliza la bala y desaparece
            puntos += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(0, 200)  # Reseteo la pos del enemigo como si apareciera otro

        enemigo(enemigo_x[e], enemigo_y[e],e)

    "Lanzar bala"
    if visibilidad_bala:
        "Movimiento bala"
        if bala_y >0:
            bala_y -= bala_y_cambio
            bala(bala_x, bala_y)
        else:
            bala_y = 468
            visibilidad_bala = False


    puntje()
    jugador(jugador_x, jugador_y)
    pygame.display.update() #Se actualiza el estado de la pantalla
from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime

"Precios objetos menu"
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

"FUNCIONES CALCULADORA"
def click_boton(boton_presionado):
    global operador
    operador = operador + boton_presionado #Agrego mi elemento al string de mi operacion
    visor_calculadora.delete(0,END) #Borra el visor para que no se pisen los resultados
    visor_calculadora.insert(END,operador) #Muesta por el visor el resultado de operador actual por la derecha

def borrar_visor():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obt_resultado():
    global operador
    res = str(eval(operador)) #Eval es una funcion que lee el string y realiza la operacion en base a su formato
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, res)
    operador = ''

"Funciones CheckButtons"
def revisar_check():
    for n in range(0,len(cuadros_comida)):
        if variables_comida[n].get() == 1:
            cuadros_comida[n].config(state = NORMAL) #Permite modificcar el campo
            if cuadros_comida[n].get() == '0':
                cuadros_comida[n].delete(0,END)
            cuadros_comida[n].focus() #Deja el cursor tiritando en el cuador
        else:
            cuadros_comida[n].config(state = DISABLED)
            texto_comida[n].set('0')

    for x in range(0,len(cuadros_bebida)):
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state = NORMAL) #Permite modificcar el campo
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus() #Deja el cursor tiritando en el cuador
        else:
            cuadros_bebida[x].config(state = DISABLED)
            texto_bebida[x].set('0')

    for x in range(0,len(cuadros_postres)):
        if variables_postre[x].get() == 1:
            cuadros_postres[x].config(state = NORMAL) #Permite modificcar el campo
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus() #Deja el cursor tiritando en el cuador
        else:
            cuadros_postres[x].config(state = DISABLED)
            texto_postres[x].set('0')

"Funciones botones"
def total():
    subtotal_comida = 0
    for n in range(0,len(texto_comida)):
        #Obtengo el valor numerico de la cantidad comprada de esa comida que esta guardada en texto comida
        subtotal_comida += (float(texto_comida[n].get())*precios_comida[n])

    subtotal_bebida = 0
    for n in range(0,len(texto_bebida)):
        #Obtengo el valor numerico de la cantidad comprada de esa comida que esta guardada en texto comida
        subtotal_bebida += (float(texto_bebida[n].get())*precios_bebida[n])

    subtotal_postres = 0
    for n in range(0,len(texto_postres)):
        #Obtengo el valor numerico de la cantidad comprada de esa comida que esta guardada en texto comida
        subtotal_postres += (float(texto_postres[n].get())*precios_postres[n])

    subtotal = subtotal_comida + subtotal_bebida + subtotal_postres
    impuestos = subtotal * 0.07
    totalf = subtotal + impuestos

    var_costo_comida.set(f'${round(subtotal_comida,2)}') #Imprimo mi valor en la pantalla
    var_costo_bebida.set(f'${round(subtotal_bebida, 2)}')
    var_costo_postres.set(f'${round(subtotal_postres, 2)}')
    var_subtotal.set(f'${round(subtotal, 2)}')
    var_impuestos.set(f'${round(impuestos, 2)}')
    var_total.set(f'${round(totalf, 2)}')

def recibo():
    text_recibo.delete(1.0, END) #Me borra cualquier ticket anterior en pantalla
    num_recibo = f'#N - {random.randint(1000,9999)}'
    fecha_act = datetime.datetime.now()
    fecha_rec = f'{fecha_act.day}/{fecha_act.month}/{fecha_act.day} - {fecha_act.hour}:{fecha_act.minute}'
    text_recibo.insert(END,f'Datos:  {num_recibo}\t\t{fecha_rec}\n')
    text_recibo.insert(END, f'*'*49 + '\n')
    text_recibo.insert(END,'Items\tCant\tCosto Items\n')
    text_recibo.insert(END,f'-'*59 +'\n')

    for x in range(0,len(texto_comida)):
        if texto_comida[x].get() != '0': #Por cada elemnto comprado muestro la cantidad y el total
            text_recibo.insert(END, f'{lista_comidas[x]}\t{texto_comida[x].get()}\t'
                                          f'$ {round(int(texto_comida[x].get()) * precios_comida[x],2)}\n')
    for x in range(0,len(texto_bebida)):
        if texto_bebida[x].get() != '0': #Por cada elemnto comprado muestro la cantidad y el total
            text_recibo.insert(END, f'{lista_bebidas[x]}\t{texto_bebida[x].get()}\t'
                                          f'$ {round(int(texto_bebida[x].get()) * precios_bebida[x],2)}\n')
    for x in range(0,len(texto_postres)):
        if texto_postres[x].get() != '0': #Por cada elemnto comprado muestro la cantidad y el total
            text_recibo.insert(END, f'{lista_postres[x]}\t{texto_postres[x].get()}\t'
                                          f'$ {round(int(texto_postres[x].get()) * precios_postres[x],2)}\n')
    text_recibo.insert(END, f'-'*59+'\n')
    text_recibo.insert(END, f'Costo comida: \t\t {var_costo_comida.get()}\n')
    text_recibo.insert(END, f'Costo bebida: \t\t {var_costo_bebida.get()}\n')
    text_recibo.insert(END, f'Costo postres: \t\t {var_costo_postres.get()}\n')
    text_recibo.insert(END, f'-'*59+'\n')
    text_recibo.insert(END, f'Subtotal: \t\t {var_subtotal.get()}\n')
    text_recibo.insert(END, f'Impuestos: \t\t {var_impuestos.get()}\n')
    text_recibo.insert(END, f'Total: \t\t {var_total.get()}\n')

def guardar_recibo():
    info_recibo = text_recibo.get(1.0,END) #Guardo todo mi recibo en una variable
    arch = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt') #Creo un arch de modo escritura y formato txt
    arch.write(info_recibo)
    arch.close()
    messagebox.showinfo("Informacion", "Su archivo ah sido guardado") #Me genera una ventana con el siguiente mensaje

def reset():
    text_recibo.delete(1.0, END)
    #Borro la cantidad de alimentos
    for texto in texto_comida:
        texto.set('0')
    #Bloqueo el selector de alimentos
    for cuadro in cuadros_comida:
        cuadro.config(state = DISABLED)
    #Desactivo los checkboxes
    for v in variables_comida:
        v.set(0)

    for texto in texto_bebida:
        texto.set('0')
    for cuadro in cuadros_bebida:
        cuadro.config(state = DISABLED)
    for v in variables_bebida:
        v.set(0)

    for texto in texto_postres:
        texto.set('0')
    for cuadro in cuadros_postres:
        cuadro.config(state = DISABLED)
    for v in variables_postre:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


"Inicalizamos Tkinter"
app = Tk()

"Definimos formato ventana"
app.geometry("1020x630+0+0") #Tam pantalla + Ubicacion eje x + Ubicacion eje y

"Evitamos mazimizar la pantalla"
app.resizable(False,False)

"Establecer titulo de ventana"
app.title("Sistema de Facturacion - RestoBar")

"Establecer fondo de la ventana"
app.config(bg = "burlywood")

"Genero panel Superior"
panel_sup = Frame(app, bd = 1, relief = FLAT)
panel_sup.pack(side = TOP)

"Generar etiqueta Titulo"
etiqueta_titulo = Label(panel_sup,text = "Sistema de Facturacion", fg = "azure4", font = ("Dosis",45), bg = "burlywood",
                        width = 27)
etiqueta_titulo.grid(row = 0, column= 0) #Ubico a mi titulo dentro del Frame

"Genero Panel Izq"
panel_izq = Frame(app, bd = 1, relief = FLAT)
panel_izq.pack(side = LEFT)

"Generar Panel Costos"
panel_costos = Frame(panel_izq, bd = 1, relief=FLAT, bg = 'azure4')
panel_costos.pack(side = BOTTOM)

"Generamos Panel comidas"
panel_comidas = LabelFrame(panel_izq, text = 'Comida', font = ('Dosis',19,'bold'), bd = 1,
                           relief = FLAT, fg = 'azure4')
panel_comidas.pack(side = LEFT)

"Generamos Panel bebidas"
panel_bebidas = LabelFrame(panel_izq, text = 'Bebidas', font = ('Dosis',19,'bold'), bd = 1,
                           relief = FLAT, fg = 'azure4')
panel_bebidas.pack(side = LEFT) #Aunque diga izquierda como primero se ubico el panl de las comidas, este estara ubicado a la derecha de este

"Generamos Panel postres"
panel_postres = LabelFrame(panel_izq, text = 'Postres', font = ('Dosis',19,'bold'), bd = 1,
                           relief = FLAT, fg = 'azure4')
panel_postres.pack(side = LEFT)

"Genrar Panel Derecho"
panel_der = Frame(app, bd = 1, relief = FLAT)
panel_der.pack(side = RIGHT)

"Generar Panel Calculadora"
panel_calcu = Frame(panel_der, bd = 1, relief = FLAT, bg = "burlywood")
panel_calcu.pack() #Si se deja vacio va x defecot en el TOP

"Generar Panel Recibo"
panel_recibo = Frame(panel_der, bd = 1, relief = FLAT, bg = "burlywood")
panel_recibo.pack()

"Generar Panel Botones"
panel_botones = Frame(panel_der, bd = 1, relief = FLAT, bg = "burlywood")
panel_botones.pack()

"Listas de Productos"
#Son necesarias para acceder a ellas sin que tengan que ser creadas cada vez
lista_comidas = ['pollo','cordero','salmon','merluza','pizza1','pizza2','pizza3']
lista_bebidas = ['agua','soda','jugo','cola','vino1','vino2','cerveza']
lista_postres = ['helado','brownies','fruta','flan','mousse','pastel1','pastel2']

"Creo loop para generar botones con opciones de comidas"
variables_comida = [] #La necesito para guardar los valores de onvalue u offvalue de mis elemetntos
contador = 0
cuadros_comida = [] #Lista que me va a permitir almacenar la cantidad pedida de c/elemento
texto_comida = []

for comida in lista_comidas:
    "Crear CheckButton"
    variables_comida.append('')
    variables_comida[contador] = IntVar() #Un tipo de variable que me permite usar tkinter
    chk_comida = Checkbutton(panel_comidas,
                             text = comida.title(),
                             font = ('Dosis',19,'bold'),
                             onvalue = 1, #Los valores que tendran los botones cuando esten activas o desactivos respectivamentes
                             offvalue = 0,
                             variable = variables_comida[contador],
                             command = revisar_check) #Se le asgina funcionalidad a el campo

    chk_comida.grid(row = contador,
                    column = 0,
                    sticky = W) #Sticky = W hace que los botones siempre esten justificados del lado izq de la ventana

    "Crear Cuadros de entrada"
    cuadros_comida.append('') #Se cargan con un caracter vacio para que existan las listas
    texto_comida.append('')
    texto_comida[contador] = StringVar() #Variable especial de Tkinter
    texto_comida[contador].set('0') #Valor por defecto que tendran nuestros cuadros
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font = ('Dosis',18,'bold'),
                                     bd = 1,
                                     width = 6,
                                     state = DISABLED, #Esto hace que no sea seleccionable si no se tildo el checkbox
                                     textvariable = texto_comida[contador]) #Necesario siempre en estos tipos de variable
    cuadros_comida[contador].grid(row = contador,
                                  column = 1)

    contador += 1

variables_bebida = []
contador = 0
cuadros_bebida = []
texto_bebida = []
for bebida in lista_bebidas:
    "Crear CheckButton"
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    chk_bebida = Checkbutton(panel_bebidas,
                             text=bebida.title(),
                             font=('Dosis', 19, 'bold'),
                             onvalue=1,
                             offvalue=0,
                             variable=variables_bebida[contador],
                             command = revisar_check)

    chk_bebida.grid(row=contador,
                    column=0,
                    sticky=W)

    "Crear Cuadros de entrada"
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font = ('Dosis',18,'bold'),
                                     bd = 1,
                                     width = 6,
                                     state = DISABLED,
                                     textvariable = texto_bebida[contador])
    cuadros_bebida[contador].grid(row = contador,
                                  column = 1)
    contador += 1


variables_postre = []
contador = 0
cuadros_postres = []
texto_postres = []
for postre in lista_postres:
    "Crear CheckButton"
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    chk_postre = Checkbutton(panel_postres,
                             text=postre.title(),
                             font=('Dosis', 19, 'bold'),
                             onvalue=1,
                             offvalue=0,
                             variable=variables_postre[contador],
                             command = revisar_check)

    chk_postre.grid(row=contador,
                    column=0,
                    sticky=W)

    "Crear Cuadros de entrada"
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                     font = ('Dosis',18,'bold'),
                                     bd = 1,
                                     width = 6,
                                     state = DISABLED,
                                     textvariable = texto_postres[contador])
    cuadros_postres[contador].grid(row = contador,
                                  column = 1)
    contador += 1

"Variables de costos"
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

"Etiquetas de Costo y campos de entrada"
#Commida
etiqueta_costo_comida = Label(panel_costos,
                              text = 'Costo Comida',
                              font = ('Dosis',12,'bold'),
                              bg = 'azure4',
                              fg = 'white')
etiqueta_costo_comida.grid(row = 0,
                           column = 0,
                           padx = 41)
texto_costo_comida = Entry(panel_costos,
                           font = ('Dosis',12,'bold'),
                           bd = 1,
                           width = 10,
                           state = "readonly", #Esto es para que no se pueda modificar
                           textvariable = var_costo_comida)
texto_costo_comida.grid(row = 0,
                        column = 1,
                        padx = 41)
#Bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text = 'Costo Bebida',
                              font = ('Dosis',12,'bold'),
                              bg = 'azure4',
                              fg = 'white')
etiqueta_costo_bebida.grid(row = 1,
                           column = 0,
                           padx = 41)
texto_costo_bebida = Entry(panel_costos,
                           font = ('Dosis',12,'bold'),
                           bd = 1,
                           width = 10,
                           state = "readonly", #Esto es para que no se pueda modificar
                           textvariable = var_costo_bebida)
texto_costo_bebida.grid(row = 1,
                        column = 1,
                        padx = 41)
#Postres
etiqueta_costo_postres = Label(panel_costos,
                              text = 'Costo Postres',
                              font = ('Dosis',12,'bold'),
                              bg = 'azure4',
                              fg = 'white')
etiqueta_costo_postres.grid(row = 2,
                            column = 0,
                            padx = 41)
texto_costo_postres = Entry(panel_costos,
                           font = ('Dosis',12,'bold'),
                           bd = 1,
                           width = 10,
                           state = "readonly", #Esto es para que no se pueda modificar
                           textvariable = var_costo_postres)
texto_costo_postres.grid(row = 2,
                         column = 1,
                         padx = 41)
#Subtotal
etiqueta_subtotal = Label(panel_costos,
                              text = 'Subtotal',
                              font = ('Dosis',12,'bold'),
                              bg = 'azure4',
                              fg = 'white')
etiqueta_subtotal.grid(row = 0,
                       column = 3,
                       padx = 41)
texto_subtotal = Entry(panel_costos,
                           font = ('Dosis',12,'bold'),
                           bd = 1,
                           width = 10,
                           state = "readonly", #Esto es para que no se pueda modificar
                           textvariable = var_subtotal)
texto_subtotal.grid(row = 0,
                    column = 4,
                    padx = 41)
#Impuestos
etiqueta_impuestos = Label(panel_costos,
                              text = 'Impuestos',
                              font = ('Dosis',12,'bold'),
                              bg = 'azure4',
                              fg = 'white')
etiqueta_impuestos.grid(row = 1,
                        column = 3,
                        padx = 41)
texto_impuestos = Entry(panel_costos,
                           font = ('Dosis',12,'bold'),
                           bd = 1,
                           width = 10,
                           state = "readonly", #Esto es para que no se pueda modificar
                           textvariable = var_impuestos)
texto_impuestos.grid(row = 1,
                    column = 4,
                     padx = 41)
#Total
etiqueta_total = Label(panel_costos,
                              text = 'Total',
                              font = ('Dosis',12,'bold'),
                              bg = 'azure4',
                              fg = 'white')
etiqueta_total.grid(row = 2,
                    column = 3,
                    padx = 41)
texto_total = Entry(panel_costos,
                           font = ('Dosis',12,'bold'),
                           bd = 1,
                           width = 10,
                           state = "readonly", #Esto es para que no se pueda modificar
                           textvariable = var_total)
texto_total.grid(row = 2,
                 column = 4,
                 padx = 41)

#Panel Der
"Creacion Botones"
botones = ['total','recibo','guardar','reset'] #Guardamos todos los botones en una lista ya que los crearemos en un loop
columnas = 0
for boton in botones:
    bb = Button(panel_botones,
                text = boton.title(),
                font = ('Dosis',12,'bold'),
                fg = 'white',
                bg = 'azure4',
                bd = 1,
                width = 6)
    bb.grid(row = 0,
            column = columnas)
    if boton == 'total':
        bb.configure(command = lambda tecla = boton: total())
    elif boton == 'recibo':
        bb.configure(command = lambda tecla = boton: recibo())
    elif boton == 'guardar':
        bb.configure(command = lambda tecla = boton: guardar_recibo())
    else:
       bb.configure(command = lambda tecla = boton: reset())
    columnas += 1

"Area de recibo"
text_recibo = Text(panel_recibo,
                   font = ('Dosis',12,'bold'),
                   bd = 1,
                   width = 42,
                   height = 10)
text_recibo.grid()

"Calculadora"
visor_calculadora = Entry(panel_calcu, #Es el area que apareceran los resultados de las cuentas
                          font = ('Dosis',12,'bold'),
                          width = 32,
                          bd = 1)
visor_calculadora.grid(row =0,
                       column = 0,
                       columnspan = 4) #Este campo hace que la columna aumente de tam

#Botones Calculdora, estan en el orden de izq a derecha, de arriba para abajo
operador = '' #Utilizado para guardar una cadena de carateres con la operacion a realizar
botones_calcu = ['7','8','9','+','4','5','6','-',
                 '1','2','3','*','C','B','0','/']
botones_guardados = [] #Es necesaria para poder luego aplicarles funcionalidades
fila = 1
colum = 0
contador = 0
for boton in botones_calcu:
        bb = Button(panel_calcu,
                    text = boton.title(),
                    font = ('Dosis',12,'bold'),
                    fg = 'white',
                    bg = 'azure4',
                    bd = 1,
                    width = 6)
        bb.grid(row = fila,
                column = colum)
        if boton == 'B':
            bb.configure(command = lambda tecla = boton:borrar_visor())
        elif boton == 'C':
            bb.configure(command = lambda tecla = boton:obt_resultado())
        else:
            bb.configure(command = lambda tecla = boton: click_boton(tecla) )
        colum += 1
        if colum == 4:
            fila += 1
            colum = 0



"Evitamos que la ventana se cierre"
app.mainloop()
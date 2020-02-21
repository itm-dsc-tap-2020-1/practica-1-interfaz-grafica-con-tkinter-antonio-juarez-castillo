import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox

def acercaDe():
    mBox.showinfo("Acerca", "Nombre: Antonio (too_2000)\nCorreo: toox2000@gmail.com")

def salirM():
    ventana.quit()
    ventana.destroy()
    exit()

def buttonTab1():
    if(nombre.get() and apellidop.get() and apellidom.get() and direccion.get() and coloniac.get() and ciudadc.get() and municipioc.get()):
        ttk.Label(tab1, text="  Completado  ").grid(row=7,column=1)
        ttk.Label(contenedor1, text="Nombre: "+nombre.get()).grid(row=0,column=0)
        ttk.Label(contenedor1, text="Apellido Paterno: "+apellidop.get()).grid(row=1,column=0)
        ttk.Label(contenedor1, text="Apellido Materno: "+apellidom.get()).grid(row=2,column=0)
        ttk.Label(contenedor1, text="Direccion: "+direccion.get()).grid(row=3,column=0)
        ttk.Label(contenedor1, text="Colonia: "+coloniac.get()).grid(row=4,column=0)
        ttk.Label(contenedor1, text="Ciudad: "+ciudadc.get()).grid(row=5,column=0)
        ttk.Label(contenedor1, text="Municipio: "+municipioc.get()).grid(row=6,column=0)
    else:
        ttk.Label(tab1, text=" Incompleto ").grid(row=7,column=1)
        for widget in contenedor1.winfo_children():
            widget.destroy()

def buttonTab2():
    for widget in contenedor2.winfo_children():
        widget.destroy()
    if(vida.get()):
        ttk.Label(contenedor2, text="Pasatiempos:").grid(row=0,column=0)
        ttk.Label(contenedor2, text="\nEstado Civil:").grid(row=4,column=0)
        ttk.Label(contenedor2, text="\nObjetivo de la vida:").grid(row=6,column=0)
        if(opc1.get()): ttk.Label(contenedor2, text="Leer").grid(row=1,column=0)
        if(opc2.get()):  ttk.Label(contenedor2, text="Ver películas").grid(row=2,column=0)
        if(opc3.get()):  ttk.Label(contenedor2, text="Redes Sociales").grid(row=3,column=0)
        if(opcr.get()):  ttk.Label(contenedor2, text=opcr.get()).grid(row=5,column=0)
        if(vida.get()):  ttk.Label(contenedor2, text=vida.get()).grid(row=7,column=0)
    else:
        ttk.Label(contenedor2, text="Incompleto").grid(row=0,column=0)
def imprimirg():
    hobby=""
    if(opc1.get()): hobby+="Leer\n"
    if(opc2.get()): hobby+="Ver películas\n"
    if(opc3.get()): hobby+="Redes Sociales"

    if(vida.get() and nombre.get() and apellidop.get() and apellidom.get() and direccion.get() and coloniac.get() and ciudadc.get() and municipioc.get()):
        mBox.showinfo("Datos", "Nombre: "+nombre.get()+"\nApellido Paterno: "+apellidop.get()+
        "\nApellido Materno: "+apellidom.get()+"\nDireccion: "+direccion.get()+
        "\nColonia: "+coloniac.get()+"\nCiudad: "+ciudadc.get()+"\nMunicipio: "+municipioc.get()+
        "\nPasatiempos:\n"+hobby+"\nEstado Civil: "+opcr.get()+"\nObjetivo de la vida:\n"+vida.get())
    else:
        mBox.showinfo("Datos","Faltan Datos")

ventana = tk.Tk()
ventana.title('Sistema Escolar')
#Pestañas
tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1, text="Datos Personales")
tabControl.pack(expand=1, fill="both")

tab2=ttk.Frame(tabControl)
tabControl.add(tab2, text="Datos Extras")

#Menu
barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)
opciones_menu=Menu(barra_menu)
opciones_menu.add_command(label="Imprimir", command = imprimirg)
opciones_menu.add_command(label="Salir", command=salirM)
barra_menu.add_cascade(label="Sistema", menu=opciones_menu)

menu_ayuda=Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de ", command= acercaDe)
barra_menu.add_cascade(label= "Ayuda", menu=menu_ayuda)

#||||Datos Personales||||
nombre = ttk.Label(tab1, text='Nombre').grid(row=0, column=0)
apellidoP = ttk.Label(tab1, text='Apellido P.').grid(row=1, column=0)
apellidoM = ttk.Label(tab1, text='Apellido M.').grid(row=2, column=0)
direccion = ttk.Label(tab1, text='Dirección').grid(row=3, column=0)
colonia = ttk.Label(tab1, text='Colonia').grid(row=4, column=0)
ciudad = ttk.Label(tab1, text='Ciudad').grid(row=5, column=0)
municipio = ttk.Label(tab1, text='Municipio').grid(row=6, column=0)

#TextBox
nombre = tk.StringVar()
nombreCapturado = ttk.Entry(tab1, width=24, textvariable=nombre)
nombreCapturado.grid(row=0, column=1)

apellidop = tk.StringVar()
apellidopCapturado = ttk.Entry(tab1, width=24, textvariable=apellidop)
apellidopCapturado.grid(row=1, column=1)

apellidom = tk.StringVar()
apellidomCapturado = ttk.Entry(tab1, width=24, textvariable=apellidom)
apellidomCapturado.grid(row=2, column=1)

direccion = tk.StringVar()
direccionCapturado = ttk.Entry(tab1, width=24, textvariable=direccion)
direccionCapturado.grid(row=3, column=1)

#ComboBox

coloniac=tk.StringVar()
col=ttk.Combobox(tab1, width=24, textvariable=coloniac)
col['values']=("Prados Verdes", "Santiaguito","Manantiales")
col.grid(row=4,column=1)
col.current(0)

ciudadc= tk.StringVar()
city= ttk.Combobox(tab1,width=24, textvariable=ciudadc)
city['values']=("Morelia","Guadalajara","Monterrey")
city.grid(row=5, column=1)
city.current(0)

municipioc=tk.StringVar()
mun=ttk.Combobox(tab1, width=24, textvariable=municipioc)
mun['values']=("Morelia", "Patzcuaro","Zamora")
mun.grid(row=6, column=1)
mun.current(0)

#Button
imprimirtab1=ttk.Button(tab1, text="Imprimir Datos Personales", command=buttonTab1)
imprimirtab1.grid(row=6, column=3)

#Contenedor
contenedor1=ttk.LabelFrame(tab1)
contenedor1.grid(row=9,column=0)
#||||Extras||||

pasatiempo = ttk.Label(tab2, text='Pasatiempos').grid(row=0, column=0)
estadoCivil = ttk.Label(tab2, text='Estado Civil').grid(row=2, column=0)
objetivoVida= ttk.Label(tab2, text='Objetivo de la vida').grid(row=4, column=0)

#CheckButton
opc1= tk.IntVar()
checkb1=tk.Checkbutton(tab2, text="Leer", variable=opc1, state='normal')
checkb1.grid(row=1, column=0, sticky=tk.W)
checkb1.select()
opc2=tk.IntVar()
checkb2=tk.Checkbutton(tab2, text="Películas", variable=opc2, state="normal")
checkb2.grid(row=1, column=1,sticky=tk.W)
checkb2.deselect()
opc3=tk.IntVar()
checkb3=tk.Checkbutton(tab2, text="Redes Sociales", variable=opc3, state='normal')
checkb3.grid(row=1, column=3, sticky=tk.W)
checkb3.deselect()
#RadioButton

opcr=tk.StringVar()
radiob1=tk.Radiobutton(tab2, text="Soltero", variable=opcr, value="Soltero")
radiob1.grid(row=3, column=0)

radiob2=tk.Radiobutton(tab2, text="Casado", variable=opcr, value="Casado")
radiob2.grid(row=3, column=1)

radiob3=tk.Radiobutton(tab2, text="Viudo", variable=opcr, value="Viudo")
radiob3.grid(row=3, column=2)

radiob1.select()

#Textbox
vida=tk.StringVar()
vidat=ttk.Entry(tab2, width=36, textvariable=vida).grid(row=5, column=0, expand=True)

#Button
imprimirtab2=ttk.Button(tab2, text="Imprimir Datos Extras", command=buttonTab2).grid(row=5, column=4)
contenedor2=ttk.LabelFrame(tab2)
contenedor2.grid(row=7,column=0)
ventana.mainloop()
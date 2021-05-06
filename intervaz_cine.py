from tkinter import *
from tkinter import ttk
import cine_database

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

pelicula = StringVar()
hora = StringVar()
fecha = StringVar()
idioma = StringVar()

def show_data():
   pelicula = entry_pelicula.get()
   hora = entry_hora.get()
   fecha = entry_fecha.get()
   idioma = entry_idioma.get()
   print(pelicula)
   print(hora)
   print(fecha)
   print(idioma)

def register():
   pelicula = entry_pelicula.get()
   hora = entry_fecha.get()
   fecha = entry_hora.get()
   idioma = entry_idioma.get()

   cine_db = cine_database.MyDatabase()
   data = (pelicula, hora, fecha, idioma)
   print(data)
   cine_db.insert_db(pelicula, hora, fecha, idioma)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=150)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender OPTIONS
frame_food = Frame(frame_options, width=350, height=500, bg="#d48df0")
frame_food.place(x=25, y=30)
label_pelicula = Label(frame_food, 
             text="pelicula:",
             font=("Calibri", "22", "bold"),
             fg="white",
             bg="#d48df0")
label_pelicula.place(x=20, y=60)
entry_pelicula = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_pelicula.place(x=20, y=100)
label_hora = Label(frame_food, 
             text="hora:",
             font=("Calibri", "22", "bold"),
             fg="white",
             bg="#d48df0")
label_hora.place(x=20, y=130)
entry_hora = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_hora.place(x=20, y=170)
label_fecha = Label(frame_food, 
             text="fecha:",
             font=("Calibri", "22", "bold"),
             fg="white",
             bg="#d48df0")
label_fecha.place(x=20, y=200)
entry_fecha = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_fecha.place(x=20, y=240)

label_idioma = Label(frame_food, 
             text="idioma:",
             font=("Calibri", "22", "bold"),
             fg="white",
             bg="#d48df0")
label_idioma.place(x=20, y=270)
entry_idioma = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_idioma.place(x=20, y=310)


button_register = Button(frame_food, text="Registrarme", command=register, font=("Calibri", "14", "bold"))
button_register.place(x=20, y=350)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
             text="Menú",
             font=("Calibri", "14"))
title.place(x=320, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
             text="¡Bienvenido(a)!", 
             font=("Calibri", "22", "bold"),
             justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
             text="¿estas listo para disfrutar?", 
             font=("Calibri", "18"),
             justify=LEFT)
title2.place(x=25, y=50)
window.mainloop()
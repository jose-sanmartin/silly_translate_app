import tkinter as tk
from transformers import pipeline
from tkinter import font
from tkinter import ttk
from tkinter import PhotoImage

#definir el pipeline de traducción
pipe = pipeline('translation', model='Helsinki-NLP/opus-mt-en-es', device= -1) #puedes cambiar a 0 si tienes cuda y torch

#función para procesar y traducir el texto
def procesar_y_traducir():
    texto = entrada_texto.get('1.0', 'end-1c')
    texto_modificado = texto.replace('\n', ' ')
    texto_modificado = texto_modificado.replace('-', ' ') #puedes modificar eliminando esta línea por si tienes peores rendimientos
    resultado = pipe(texto_modificado)
    salida_texto.delete('1.0', 'end')
    salida_texto.insert('1.0', resultado[0]['translation_text'])

#función para eliminar solo los saltos de línea
def eliminar_saltos_de_linea():
    texto = entrada_texto.get('1.0', 'end-1c')
    texto_modificado = texto.replace('\n', ' ')
    salida_texto.delete('1.0', 'end')
    salida_texto.insert('1.0', texto_modificado)

#generación del root y parámetros generales
root = tk.Tk()

#logo = PhotoImage(file='own_direction') # introduce tu propio logo!!

root.title('Silly translator by JLSM')

root.config(bg='#80E8F0')

#root.iconphoto(True, logo)

fuente = font.Font(family='Roboto', size=15)

style = ttk.Style()
style.theme_use('alt')

#widgets

#entry widget
entrada_texto = tk.Text(root, height=15, width=100, font=fuente)
entrada_texto.insert("1.0", "Borra e introduce aquí tu texto a traducir")
entrada_texto.config(fg='grey')
entrada_texto.pack(pady=10)

#button widget para traducir
style.configure('TButton', font=('Roboto', 15), background='#80E8F0', foreground='black')
boton_traducir = ttk.Button(root, text='Traducir!!', command=procesar_y_traducir, style='TButton')
boton_traducir.pack(pady=10)

#button widget para eliminar saltos de línea
boton_eliminar_saltos = ttk.Button(root, text='Eliminar Saltos de Línea', command=eliminar_saltos_de_linea, style='TButton')
boton_eliminar_saltos.pack(pady=10)

#output widget
salida_texto = tk.Text(root, height=15, width=100, font=fuente)
salida_texto.pack(pady=10)

root.mainloop()


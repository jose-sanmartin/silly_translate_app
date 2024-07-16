import tkinter as tk
from transformers import pipeline
from tkinter import font

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es", device=-1) #puedes cambiara a 0 si tienes cuda y torch

def procesar_y_traducir():
    texto = entrada_texto.get("1.0", "end-1c")
    texto_modificado = texto.replace('\n', ' ') 
    resultado = pipe(texto_modificado)
    salida_texto.delete("1.0", "end")
    salida_texto.insert("1.0", resultado[0]['translation_text']) 

root = tk.Tk()

root.title("Traductor de texto")

fuente = font.Font(family="Helvetica", size=15) 

entrada_texto = tk.Text(root, height=15, width=100, font=fuente)

entrada_texto.pack()

boton = tk.Button(root, text="Traducir", command=procesar_y_traducir)

boton.pack()

salida_texto = tk.Text(root, height=15, width=100, font= fuente)

salida_texto.pack()

root.mainloop()

import tkinter as tk
from transformers import pipeline
from tkinter import font

# Configuración inicial del pipeline de traducción
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es", device=0)  # Usando CPU

def procesar_y_traducir():
    texto = entrada_texto.get("1.0", "end-1c")  # Obtiene el texto desde el widget de entrada
    texto_modificado = texto.replace('\n', ' ')  # Elimina los saltos de línea
    resultado = pipe(texto_modificado)  # Traduce el texto
    salida_texto.delete("1.0", "end")  # Limpia el campo de salida antes de insertar el nuevo texto
    salida_texto.insert("1.0", resultado[0]['translation_text'])  # Inserta el texto traducido en el widget de salida

# Crear la ventana principal
root = tk.Tk()
root.title("Traductor de texto")

fuente = font.Font(family="Helvetica", size=15) 

# Widget de entrada de texto
entrada_texto = tk.Text(root, height=15, width=100, font=fuente)
entrada_texto.pack()

# Botón para procesar el texto
boton = tk.Button(root, text="Traducir", command=procesar_y_traducir)
boton.pack()

# Widget de salida de texto, similar a la entrada
salida_texto = tk.Text(root, height=15, width=100, font= fuente)
salida_texto.pack()

# Iniciar la interfaz gráfica
root.mainloop()

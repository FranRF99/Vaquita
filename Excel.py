import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from datetime import datetime
from tkinter import filedialog

#from PIL import Image, ImageT

class Datos:
    def __init__(self, IDE, IE):
        self.IDE = IDE
        self.IE = IE

def seleccionar_BD():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana de Tkinter
    ruta_archivoxslx = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])  # Abre el explorador de archivos y filtra solo archivos .xlsx
    return ruta_archivoxslx

def seleccionar_CSV():
    fecha =datetime.now().date()
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana de Tkinter
    ruta_archivo_csv = filedialog.askopenfilename(filetypes=[('Excel Files', '*.csv')])
    archivo = pd.read_csv(f'{ruta_archivo_csv}', delimiter=';', encoding='utf-8')
    archivo.columns = archivo.columns.str.strip()
    archivo.to_excel(f'C:\\Users\\franr\\OneDrive\\Escritorio\\Trabajos Web\\Inta\\Datos_{fecha}.xlsx', index=False )
    datos_csv=archivo
  # Abre el explorador de archivos y filtra solo archivos .xlsx
    
    return datos_csv



def Juntador_baseDD_CSV(df1, archivo):
    # Asegúrate de que tus datos estén en la columna correcta, por ejemplo, 'codigo'
    codigos_df1 = df1['IE']
    codigos_df2 = archivo['IDE']
    for codigo in codigos_df1:  
        if codigo in codigos_df2.values:
            print (f"{codigo} ya está cargado")

ruta_archivoxslx = seleccionar_BD()
df1 = pd.read_excel(ruta_archivoxslx, skiprows=1, usecols="L:")
archivo = seleccionar_CSV()
Juntador_baseDD_CSV(df1, archivo)

    
def salir():
    app.destroy()

app = tk.Tk()
app.title("Mi Aplicación")
app.geometry("500x500")
app.resizable(0, 0)

# Crear y empaquetar el botón antes de app.mainloop()
boton = tk.Button(app, text="Elegir base de datos", command=seleccionar_BD)
boton.pack()
boton2 = tk.Button(app, text="Elegir Datos barra", command=seleccionar_CSV)
boton2.pack()
boton3 = tk.Button(app, text="Pasar datos barra a Base de datos", command=Juntador_baseDD_CSV)
boton3.pack()
boton4 = tk.Button(app, text="salir", command=salir)
boton4.pack()

# Mantener una referencia a la imagen y asegurarse de que la ruta es correcta
ruta_imagen = "C:\\Users\\franr\\OneDrive\\Escritorio\\Trabajos Web\\Inta\\vaquita.png"
imagen = tk.PhotoImage(file=ruta_imagen)
lbl_img = tk.Label(app, image=imagen)
lbl_img.pack()
app.mainloop()


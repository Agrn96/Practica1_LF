from tkinter import *
from tkinter import filedialog

def cargar_Archivo():
    filename = filedialog.askopenfile(filetypes=(('text files', 'txt'),))
    return(filename)
    
    
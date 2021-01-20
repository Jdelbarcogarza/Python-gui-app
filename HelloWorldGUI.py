'''
Hello World App sacada de realpython para comenzar a utilizar APIs solamente con python.
Primer intento en haer GUI con tkinter. Tutorial sacado de 
https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

Fecha: 18/01/21
'''

import tkinter as tk


def main():
    # esto crea una ventana. window es la variable.
    window = tk.Tk()
    # aqui solo declaramos el label. No se ha puesto sobre nuestra main window
    label = tk.Label(
    text="Hello, Tkinter",
    # parametro que puede escribirse como fg. Acepta hexadecimal y HTML colors
    foreground="white",
    # parametro que puede escribirse como bg. Acepta hexadecimal y HTML colors
    background="black",
    # dimensiones del label dentro de nuestro window. LAS UNIDADES SON TEXT UNITS. No px.
    width=10,
    height=10
    )

    # con el método pack se imprime el widget en la window
    label.pack()

    button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    )

    button.pack()


    label2 = tk.Label(text="Name")
    entry = tk.Entry()

    name = entry.get()

    '''
    Estos metodos son para 

    Retrieving text with .get()
    Deleting text with .delete()
        * entry.delete(0, tk.END) borra todos los caracterse de un entry.
        los argumentos (a,b) funcionan como string slicing.

    Inserting text with .insert()

    '''

    label2.pack()
    entry.pack()

    # sin este comando, el programa no corre.
    '''
    This method listens for events, such as button clicks or keypresse
    and blocks any code that comes after it from running until the window it’s called on is closed. 
    '''
    window.mainloop()

if __name__ == "__main__":
    main()
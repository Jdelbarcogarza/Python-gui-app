'''
Este programa es un editor de texto sencillo. Se siguió con un tutorial sacado de
https://realpython.com/python-gui-tkinter/#making-your-applications-interactive

Fecha: 20/01/21
'''
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():

    # Se crea la ventana
    window = tk.Tk()

    # Se agrega el título de la App
    window.title("Simple Text Editor")

    # Se eligen las dimensiones mínimas de la ventana (width, height)
    window.minsize(700,600)

    #Hacemos que la ventana sea adaptable si se cambia de tamaño
    window.rowconfigure(0, weight=1, minsize=200)
    window.columnconfigure(1, weight=1, minsize=200)

    # Creamos un frame para pone ahí dentro nuestro grid. Solo lo utilizaremos para organizar los botones
    frm_buttons = tk.Frame(window)

    '''
    Después de haber puesto los widgets se definirá como deberán comportarse los mismos dentro del
    grid si la pantalla cambia de tamaño
    '''

    #Declaramos los widgets de botón y se colocan
    btn_open = tk.Button(frm_buttons, text="Open File")
    btn_save = tk.Button(frm_buttons, text="Save As")
    
    # Entry es de una sola línea, text recibe texto multilínea.
    # Lo ponemos en el window para que siempre ocupe todo el espacio de la ventana
    txt_Area = tk.Text(window, relief=tk.SUNKEN, borderwidth=2)
    
    # Colocamos los widgets de manera vertical
    btn_save.grid(row=0, column=0, sticky="NEWS", padx = 5, pady=5)
    btn_open.grid(row=1, column=0, sticky="NEWS", padx=5,)

    '''
    RECUERDA SIEMPRE PONER EL FRAME EL EL GRID CON SUS COORDENADAS. pUEDES YA HABER PUESTO LOS
    WIDGETS, PERO SI NO ESTÁ PUESTO EL FRAME LOS WIDGETS NO APARECEN
    '''
    # Se aplica a la ventana el frame previamente declarado en la ubicación (0,0) de la ventana.
    # Recordemos que el master de este frame es window
    # El atributo sticky del frame es NS para que quede alineado siempre. 
    frm_buttons.grid(row=0, column=0, sticky="NS")

    # Se coloca el text Area 
    # Como el text Area no está dentro de un frame y su master es window (la ventana en sí).
    # Podemos ponerle sticky = news para que llene el resto del espacio de su celda, que es el
    # espacio que le queda a la ventana llenandola por completo. 
    txt_Area.grid(row=0, column=1, padx=5, pady=5, sticky="NEWS")


    # Ahora se le agrega funcionalidad y lógica a los botones

    # Esta función se encarga de abrir los folders de el ordenador. 
    # Se copió y se pegó.
    def open_file(event):

        """Open a file for editing."""

        filepath = askopenfilename(

            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]

        )

        if not filepath:

            return

        # Si se abre un archivo esta línea borra todo el contenido de el text Area
        txt_Area.delete("1.0", tk.END)

        # Se abre el archivo
        with open(filepath, "r") as input_file:

            # Se lee el archivo
            text = input_file.read()

            # Se inserta el archivo
            txt_Area.insert(tk.END, text)

        window.title(f"Simple Text Editor - {filepath}")

    # conectamos la función anterior con el event handler del botón de open
    btn_open.bind("<ButtonRelease>", open_file)

    def save_file(event):

        """Save the current file as a new file."""

        filepath = asksaveasfilename(

            defaultextension="txt",

            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],

        )

        if not filepath:

            return

        with open(filepath, "w") as output_file:

            text = txt_Area.get("1.0", tk.END)

            output_file.write(text)

        window.title(f"Simple Text Editor - {filepath}")


    # conectamos el botón de Save As a la función que tenemos de arriba para salvar el archivo
    btn_save.bind("<ButtonRelease>", save_file)

    window.mainloop()

if __name__ == "__main__":
    main()
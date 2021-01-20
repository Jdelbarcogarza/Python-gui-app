import tkinter as tk


def main():
    # esta es nuestra ventana
    window = tk.Tk()
    '''
    IMPORTANTE
    Note to self: no se debe usar .pack() y .grid() en la misma master window.
     "A common mistake is to use the wrong parent for some of the widgets." 
     Tienen que estar separados por diferentes frames.

     OJO

     The important thing to realize here is that even though .grid() is called on each Frame object, 
     the geometry manager applies to the window object.
      Similarly, the layout of each frame is controlled with the .pack() geometry manager.

     ¿Qué es master?

     Your Application class is a subclass of tk.Frame. The master parameter is the parent 
     widget and it is an optional parameter (by default it is none)
    that will be passed to the new instance of Application class when it is initialized.
    '''
    # Titulo de la ventana
    window.title("Address Entry Form")

    # el frame principal tiene como master a nuestra ventana, tiene un border tipo groove con un 
    # grosor de 1. El frame principal contendrá un grid. Dicho grid tendrá labels y entries.
    frame_principal = tk.Frame(master=window, width=500,
     height=500, borderwidth=1)
    
    # se agrega el frame_principal y su configuración a la ventana
    frame_principal.pack()

    # creamos lista con lo que contendrán nuestros labels para acceder a ellos dentro de un for
    # e imprimirlos de manera automática
    list_label_content = [
        "First Name:", "Last Name:", 
        "Address Line 1:", "Address Line 2:", 
        "City:", "State/Province:",
        "Postal Code:", "Country:"
        ]


    # En este for creamos un grid con 2 columnas y 9 rengoles que contendran [label - entry] en cada renglón.
    # Cada celda del grid debe ser un frame. Dentro de un for crearemos y llenaremos cada celda 
    # con el widget que le corresponde
    
    # 'i' representa los renglones 
    for i in range(0, len(list_label_content)):

        # 'j' representa las columnas
        for j in range(0,2):

            # Antes de llenar las celdas. Cada una es frame. Por eso en cada columna se correrá
            # este pedazo de código.

            frame_celda_individual = tk.Frame(master=frame_principal)
            #creamos el grid
            frame_celda_individual.grid(row=i, column=j, sticky="e")
            # hacemos un if para verificar en qué renglón estamos y poner el contenido correcto
            # en esa celda. Si j == 0 -> ponemos label, Si j == 1 -> ponemos entry.
            if (j == 0):

                label_requisite = tk.Label(master=frame_celda_individual,
                 text=list_label_content[i], relief=tk.FLAT)
                label_requisite.pack()

            else:

                entry_blank_space = tk.Entry(master=frame_celda_individual ,width=50)
                entry_blank_space.pack()
            

    # Ahora se deben agregar botones de 'Clear' y 'Submit', para interactuar con el input del usuario
    # haremos un grid de 1 renglon y 2 columnas para alinearlos correctamente.
    
    '''
    Estos dos sirven para .pack() solamente
    # ipadx o ipady es padding.
    # padx o pady es como si fuera margin
    '''

   

    button_Clear = tk.Button(master=window, text="Clear")
    button_Clear.pack(fill= tk.Y, side=tk.RIGHT, padx=20, ipadx=5, pady=5)
    

    button_Submit = tk.Button(master=window, text="Submit")
    button_Submit.pack(fill= tk.Y, side=tk.RIGHT , ipadx=5, pady = 5)
    
            
            
            


    window.mainloop()

if __name__ == "__main__":
    main()
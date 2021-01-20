'''
ejercicio sobre interactividad e event handlers con tkinter. Tambien más que nada se 
practicó la responsiveness de las ventanas y de como centrar un grid y elementos dentro de los grids
y de la ventana.

algo muy importante fue practicar con el uso de grids dentro de frames. Esto con el propósito de 
hacer apps con esta estructura de GUI más adelante.

Fecha: 20/01/2021
'''
import tkinter as tk
from random import randint

    


def main():

    # Función que devuelve un número random cuando se presiona el botón de "Roll!".
    '''
    El parámetro de la funcion "event" es el evento que activó nuestra función, en este caso fue 
    el soltar el botón izquierdo del mouse cuando se presionó el botón de "Roll!"
    '''
    def rollDie(event):
        # Guardamos un número random del 1 al 6
        random_num = randint(1,6)

        value = random_num

        lbl_number["text"] = value

    window = tk.Tk()
    #Le ponemos título a nuestra pantalla
    window.title("Roll Die App")

    # (width , height) Esta es la medida mínima de la ventana
    window.minsize(250, 90)

    '''
    NOTAS:

        The whole grid stays at the top-left corner as the window expands.

        You can adjust how the rows and columns of the grid grow as the window is resized using 
        .columnconfigure() and .rowconfigure() on the window object. Remember, the grid is
        attached to window, even though you’re calling .grid() on each Frame widget. 
        Both .columnconfigure() and .rowconfigure() take three essential arguments:

        1. The index of the grid column or row that you want to 
        configure (or a list of indices to configure multiple rows or columns at the same time)

        2. A keyword argument called weight that determines 
        how the column or row should respond to window resizing, relative to the other columns and rows

        3. A keyword argument called minsize that sets the minimum
        size of the row height or column width in pixels

    '''

    # en estas dos líneas de código se le dice al programa que se le permita hacer un "resize" 
    # de su contenido.
    window.grid_rowconfigure(0, weight=1, minsize=50)
    window.grid_columnconfigure(0, weight=1, minsize=50)


    # creamos un frame para guardar ahí nuestro grid
    frm_main = tk.Frame(window)

    # como queremos que el contenido del grid ocupe toda la pantalla se le pone el atributo de sticky
    # el valor de NEWS (son los 4 puntos cardinales).
    frm_main.grid(row=0, column=0, sticky="news")

    # Aqui es importante seleccionar como queremos que se comporten los elementos de cada celda del grid
    # cuando cambiamos el tamaño de la pantalla, ajustando el tamaño mínimo del ancho de las columnas
    # o altura de los renglones. El atributo weight indica que tanto debe crecer un widget con respecto
    # a otro tomando en cuenta el espacio libre que hay en la pantalla.
    frm_main.grid_columnconfigure(0, weight=1, minsize=15)
    frm_main.grid_rowconfigure(0, weight=1, minsize=15)
    frm_main.grid_rowconfigure(1, weight=1, minsize=15)

    # Ya que fijamos como se van a comportar las celdas que serán ocupadas por nuestros widgets
    '''
    OJO

    En este programa se puso arriba la configuración del comportamiento de las celdas del grid,
    pero en realidad deberían ir hasta abajo porque primero se ponen los widgets.
    '''
    # Se crea el widget
    btn_roll = tk.Button(frm_main, text="Roll!")

    # Se coloca en su respectiva posición dentro del frame que creamos con el llenado NEWS
    btn_roll.grid(row=0, column=0, sticky="news")

    '''
    OJO
    Estas dos líneas de código ya no son necesarias porque se configuró el comportamiento de dicha celda
    en el frame (línea 50-58) Si lo escribimos de nuevo solo estaríamos repitiendonos a nosotros mismos.
    Si no hubieramos configurado el frame como se hizo, si tendría sentido colocar estas líneas.

    btn_roll.grid_rowconfigure(0, weight=1)
    btn_roll.grid_columnconfigure(0, weight=1)
    '''
    # Se declara el segundo widget
    lbl_number = tk.Label(frm_main, text="0" , bg="yellow")

    # Se coloca el widget en su respectiva posición llenando con su contenido el espacio de la celda
    # con sticky = "NEWS"
    lbl_number.grid(row=1,column=0, sticky="news")
    '''
    Igual que en las líneas 78 y 79, no es necesario poner estas líneas de código


    lbl_number.grid_rowconfigure(1, weight=2)
    lbl_number.grid_columnconfigure(0, weight=2)
    '''

    # Ahora se agregará la lógica a los botónes con event handlers. No se usará el atributo command
    # porque debemos pasar parametros a la funcion rollDie().
    # Guardamos el valor el contenido del label lbl_number en una variable para pasarlo como argumento
    # en nuestra función dentor del event handler.
    # accesamos a el label para modificar su valor. Accedemos a el atributo "text" como 
    # si fuera un diccionario, dónde "text2 es la llave y "0" es el valor por default.
    '''
    Esta linea ya no se usa porque nuestra función dieRoll() toma directamente el valor y lo cambia
    number_in_label = lbl_number["text"]
    '''
    
    
    # Utilizaremos el evento ButtonRelease, sacado de una lista de otros eventos.
    
    btn_roll.bind("<ButtonRelease>", rollDie)

    window.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import *
# Implement the default Matplotlib key bindings.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Hélice Conica

# Hélice Circular

# Corona Sinusoidal

X = np.linspace(0, 2 * np.pi, 50)
Y = np.sin(X)         #definimos datos compuestos para x,y. Ademas configuramos recorrido 5 sg.

fig, ax = plt.subplots(1, 1)
ax.set_xlim([0, 2 * np.pi])
ax.set_ylim([-1.1, 1.1])
ax.set_title("Corona Sinusoidal")

sinusoide, = ax.plot([], [])   #definimos elementos de ventana, como la onda y el punto sobre ella
punto, = ax.plot([], [], 'o', color='red')

def sine(i):
    sinusoide.set_data(X[:i], Y[:i])
    punto.set_data(X[i], Y[i])      #se define funcion principal


anim = animation.FuncAnimation(fig, sine, frames=len(X), interval=16, blit=False, repeat=False)  #Animar la curva mediante FuncAnimation, se
#...detiene el bucle con Repeat=False
plt.show()

pass


# Curva de Viviani

# Hipopoda

# Espiral Cónica de Papus

# Curva de Arquitas

# Horóptera

# Curva Bicilindrica

if __name__ == '__main__':
    # Creación de Ventanas
    root = tk.Tk()
    root.wm_title("Tarea 02 (15%)")
    root.geometry("800x600")

    # Crear frame contenedor de los elementos
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    # Añadir titulo
    label = tk.Label(frame, text="Curvas Paramétricas Famosas", height="2")
    label.pack(fill=tk.X, expand=1)

    sinusoidal_im = tk.PhotoImage(file="sinusoidal.gif")
    sinusoidal_button = tk.Button(master=frame, text="Corona Sinusoidal en 45°", command=sine, image=sinusoidal_im)
    sinusoidal_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    tk.mainloop()

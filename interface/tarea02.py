import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Hélice Conica

# Hélice Circular

# Corona Sinusoidal

""" CORONA SINUSOIDAL ANIMADA MEDIANTE MATPLOTLIB
    
    Integrantes:
        _Luis Soto Zelada (@Luiss23)
        _Diego Rojas (@diegoskky)
        _Lucia Vilches (@luciavj)
    
    """
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

X = np.linspace(0, 2 * np.pi, 100)
Y = np.sin(X)         #definimos datos compuestos para x,y

fig, ax = plt.subplots(1, 1)
ax.set_xlim([0, 2 * np.pi])
ax.set_ylim([-1.1, 1.1])
ax.set_title("Corona Sinusoidal")

sinusoide, = ax.plot([], [])   #definimos escenario
punto, = ax.plot([], [], 'o', color='red')

def sine(i):
    sinusoide.set_data(X[:i], Y[:i])
    punto.set_data(X[i], Y[i])      #se define la curva o sinusoide


anim = animation.FuncAnimation(fig, sine, frames=len(X), interval=50)  #Animar la curva mediante animacion matplotlib
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

    tk.mainloop()

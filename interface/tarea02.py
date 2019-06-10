import tkinter as tk
from tkinter import *
# Implement the default Matplotlib key bindings.
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# Hélice Conica
def helice_conica():
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    def gen(n):
        theta = 0
        e = 2.718281
        a = 0.5
        an1 = 45
        an2 = 30

        while theta > -25 * np.pi:
            x = a * (e ** (np.sin(an1) * (1 / np.tan(an2) * theta))) * np.cos(theta)
            y = a * (e ** (np.sin(an1) * (1 / np.tan(an2) * theta))) * np.sin(theta)
            z = a * (e ** (np.sin(an1) * (1 / np.tan(an2) * theta))) * (1 / np.tan(an1))
            yield np.array([x, y, z])
            theta += -8 * np.pi / n

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 150
    data = np.array(list(gen(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

    # Setting the axes properties
    ax.set_xlim3d([-10.0, 10.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-10.0, 10.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 10.0])
    ax.set_zlabel('Z')

    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=1000 / N, blit=False, repeat=False)

    plt.show()

# Hélice Circular
def helice_circular_1():
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    def gen(n):
        t = 0
        r = 5
        while t < 8 * np.pi:
            yield np.array([r * np.cos(t), r * np.sin(t), t])
            t += 5.5 * np.pi / n

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 100
    data = np.array(list(gen(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], label='Curva Helice Circular')
    ax.legend()

    # Setting the axes properties

    ax.set_xlim3d([-8.0, 8.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-8.0, 8.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 16.0])
    ax.set_zlabel('Z')
    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=16, repeat=False)
    plt.show()

    pass
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

    Conica_im = tk.PhotoImage(file="helice_conica.gif")
    conica_button = tk.Button(master=frame, text="Hélice Cónica", command=helice_conica, image=Conica_im)
    conica_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    helice_circular_im=tk.PhotoImage(file="helice_circular1.gif")
    helice_circular_button=tk.Button(master=frame, text="helice circular", command=helice_circular_1, image=helice_circular_im)
    helice_circular_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    tk.mainloop()

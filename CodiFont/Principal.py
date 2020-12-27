from MainFrame import *
from Robot import *
import tkinter as tk

n = 6

# ==================================================================================
# nom: asignar_params
# funció: Amb aquesta funció assignem el tamany de la cuadrícula de joc
# paràmetres: `num` --> tipus int que ens arriba de l'Entry que conté el tamany de
#               la cuadrícula
# cridada: la funció és cridada quan l'usuari pitja el botó crea simulació
# ==================================================================================
def asignar_params(num):
    global n

    # Asignem el tamany de la cuadrícula
    res = num.get()
    # comprovam que sigui un nombre
    n = int(res) if res.isdigit() else 5

    # Tancam la finestra
    root.destroy()


if __name__ == "__main__":
    # Cream una finestra inicial en la qual se li demanarà a l'usuari que introdueixi els
    # paràmetres sobre els quals voldrà executar la simulació de la cova del monstre
    root = tk.Tk()
    root.title("Paràmetres")
    lbl = tk.Label(root, text = "Introduïu el tamany del tauler, per defecte serà de 5x5")
    lbl.pack()
    num = tk.Entry(root, width=5)
    num.pack()

    tamany = tk.Button(root, text = "CREA SIMULACIÓ")
    tamany["command"] = lambda: asignar_params(num)
    tamany.pack()

    root.mainloop()

    root = tk.Tk()
    root.title("ROBOT AMB PASSADISSOS ESTRETS")
    mf = MainFrame(root, n)
    mf.pack(side="left", fill="both", expand=True)
    a = Robot(n)

    # Botó per inserir els murs
    mur = tk.Button(root, text = "Mur", bg = "Grey", width = 5, height = 2)
    mur["command"] = lambda: mf.afegirElement(1)
    mur.pack(side="top", fill="both")

    # Botó per inserir l'agent en una posició en concret
    agent = tk.Button(root, text = "Agent", bg = "Grey",width = 5, height = 2)
    agent["command"] = lambda: mf.afegirElement(2)
    agent.pack(side="top", fill="both")

    # Botó per inicialitzar la simulació
    init = tk.Button(root, text = "Inicialitza", bg = "yellow")
    init["command"] = lambda: mf.inicialitza(a)
    init.pack(side="bottom", fill="both")

    lbl = tk.Label(root, text = "Escull la velocitat")
    lbl.pack(side="top", fill="both")
    # Definim els radio buttons per a definir la velocitat segons 3 nivells
    var = tk.IntVar()
    # Velocitat lenta
    vel1 = tk.Radiobutton(root, text="Lent", variable=var, value=1)
    vel1["command"] = lambda: a.Vel(var)
    vel1.pack(side="top", fill = "both")
    # Velocitat mitja
    vel2 = tk.Radiobutton(root, text="Mig", variable=var, value=2)
    vel2["command"] = lambda: a.Vel(var)
    vel2.pack(side="top", fill = "both")
    vel2.select() # Per defecte anirem a ritme mig
    # Velocitat ràpida
    vel3 = tk.Radiobutton(root, text="Rapid", variable=var, value=3)
    vel3["command"] = lambda: a.Vel(var)
    vel3.pack(side="top", fill="both")

    root.mainloop()
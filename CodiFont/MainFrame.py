from functools import partial
import tkinter as tk
from tkinter import messagebox

class MainFrame(tk.Frame):

    def __init__(self, parent,  n, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.init = False
        self.ag = False
        self.el = 1
        self.x = []
        for row in range(0, n):
            self.col = []
            for column in range(0, n):
                new_button = tk.Button(self, bg = 'brown', width = 5, height = 2)
                new_button.configure(fg="white")
                new_button.grid(row=row, column=column)
                new_button["command"] = partial(self.press, new_button, row, column)
                self.col.append(new_button)
            self.x.append(self.col)

    # ==================================================================================
    # nom: press
    # funció: Amb aquesta funció permetem que s'insereixin els murs o l'agent, segons
    #         la variabe self.el.
    # paràmetres: `btn` --> tipus button que conté el botó on s'ha d'inserir l'element
    #             `r` --> tipus int que conté la posició y del botó
    #             `c` --> tipus int que conté la posició x del botó
    # cridada: la funció és cridada quan l'usuari prem un dels botons de la cuadrícula
    # ==================================================================================
    def press(self, btn, r, c):
        if self.el == 1:
            btn.configure(bg="grey")
            btn.configure(activebackground="grey")
            btn.configure(text="X")
        elif self.el == 2:
            if self.ag == False:
                btn.configure(bg="black")
                btn.configure(activebackground="black")
                btn.configure(text="Agent")
                self.ag = True
                self.r = r
                self.c = c

    # ==================================================================================
    # nom: inicialitza
    # funció: Amb aquesta funció inicialitzem la simulació cridant a la funció inicialitza
    #         de la classe robot. No es podrà inicialitzar si no s'ha inserit l'agent
    # paràmetres: `l` --> tipus robot que conté tota la lògica del robot
    # cridada: la funció és cridada quan l'usuari pitja el botó de inicialitza
    # ==================================================================================
    def inicialitza(self, l):
        if self.ag == True and self.init == False:
            self.init = True
            l.inicialitza(self, self.r, self.c)
        else:
            messagebox.showinfo("Alerta!", "No heu introduit la posició de l'agent")

    # ==================================================================================
    # nom: afegirElement
    # funció: Amb aquesta funció canvia el valor de self.el, permetent a l'usuari triar
    #         entre inserir murs o l'agent
    # paràmetres: `el` --> tipus int que indica quin element s'ha inserir
    # cridada: la funció és cridada quan l'usuari pitja en el botó de murs o el d'agent
    # ==================================================================================
    def afegirElement(self, el):
        self.el = el

    # ==================================================================================
    # nom: info
    # funció: Amb aquesta funció retornem la casella en la posició [r, c]
    # paràmetres: `r` --> posició x de la casella a tornar
    #             `c` --> posició y de la casella a tornar
    # cridada: la funció és cridada quan l'usuari vol saber el contingut d'una casella
    # ==================================================================================
    def info(self, r, c):
        return self.x[r][c]



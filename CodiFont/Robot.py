import tkinter as tk
import random as rn
import time as t
import sys

class Robot():
    
    def __init__(self, n):
        self.W = [0, 0, 0, 0, 0, 0, 0, 0] # Vector amb el conjunt de percepcions
        self.oldW = [0, 0, 0, 0] # Vector amb les percepcions de {N, S, E, O} passades
        self.newW = [0, 0, 0, 0]  # Vector amb les percepcions de {N, S, E, O} actuals
        self.r = 0  # Posició y de l'agent
        self.c = 0  # Posició x de l'agent
        self.n = n-1
        self.actS = 0 # Estat actual {1: nort, 2: sud, 3: est, 4: oest}
        self.vel = 0.2 # Velocitat inicial per defecte

    # ==================================================================================
    # nom: unio
    # funció: Aquesta funció actualitza el vector W segons el moviment actual, és a dir,
    #         els valors de newW.
    # paràmetres: `MainFrame` --> tipus tk.Frame que conté tota la informació sobre la qua-
    #               drícula de l'ambient
    # cridada: La funció es cridada en la funció inicialitza per a actualitzar
    #          la percepció de l'agent abans de dur a terme el moviment
    # ==================================================================================
    def actualitzaW(self, MainFrame):

        self.newW = [0, 0, 0, 0] # inicialitzem
        if self.r-1 < 0 or MainFrame.info(self.r-1, self.c)["bg"] == 'grey':
            self.newW[0] = 1
        if self.c-1 < 0 or MainFrame.info(self.r, self.c-1)["bg"] == 'grey':
            self.newW[3] = 1
        if self.c+1 > self.n or MainFrame.info(self.r, self.c+1)["bg"] == 'grey':
            self.newW[1] = 1
        if self.r+1 > self.n or MainFrame.info(self.r+1, self.c)["bg"] == 'grey':
            self.newW[2] = 1

        self.W = [0, 0, 0, 0, 0, 0, 0, 0] # inicialitzam vector W a 0
        # inserim els valors de newW a W
        for i in range(4):
            self.W[i*2 + 1] = self.newW[i]
        
    # ==================================================================================
    # nom: unio
    # funció: Aquesta funció actualitza el vector W segons els valors del vector oldW. 
    #         Després actualitzem oldW per newW
    # paràmetres: `W1` --> posició del vector W a modificar per la de oldW[o1]
    #             `W2` --> posició del vector W a modificar per la de oldW[o2]
    #             `o1` --> posició del vector oldW a inserir a W[W1]
    #             `o2` --> posició del vector oldW a inserir a W[W2]
    # cridada: La funció es cridada el bucle de la funció inicialitza per a actualitzar
    #          la percepció de l'agent abans de dur a terme el moviment
    # ==================================================================================
    def unio(self, W1, W2, o1, o2):
        self.W[W1] = self.oldW[o1]
        self.W[W2] = self.oldW[o2]
        self.oldW = self.newW[:] # Actualitzam el vector oldW

    # ==================================================================================
    # nom: moviment
    # funció: Aquesta funció du a terme el moviment de l'agent segons la posició inferida
    #         en la funció moure
    # paràmetres: `row` --> enter que conté la nova posició y inferida (la qual l'agent
    #               s'ha de moure)
    #             `col` --> enter que conté la nova posició x inferida (la qual l'agent
    #               s'ha de moure)
    #             `mf` --> tipus tk.Frame que conté tota la informació sobre la qua-
    #               drícula de l'ambient
    # cridada: La funció és cridada desde moure, la qual la crida just després d'haver 
    #          inferit la posició siguient de l'agent
    # ==================================================================================
    def moviment(self, row, col, mf):
        mf.info(r=self.r, c=self.c)["bg"] = 'brown'
        mf.info(r=self.r, c=self.c)["text"] = ""
        self.c = col
        self.r = row
        mf.info(r=self.r, c = self.c)["bg"] = 'black'
        mf.info(r=self.r, c=self.c)["text"] = "Agent"

    # ==================================================================================
    # nom: moure
    # funció: Aquesta funció és la que infereix el moviment que s'ha de dur a terme
    # paràmetres: `MainFrame` --> tipus tk.Frame que conté tota la informació sobre la qua-
    #               drícula de l'ambient
    # cridada: La funció és cridada desde el bucle de inicialitza, després de haver ac-
    #          tualitzat el vector W amb les noves percepcions
    # ==================================================================================
    def moure(self, MainFrame):    
        t.sleep(self.vel)
        if self.W[1] and not self.W[3] and (self.actS != 4 or (self.W[7] and self.W[5])) and  (not (self.actS == 1 and self.W[6] and not self.W[7])):
            # mourer-se a l'est
            self.moviment(self.r, self.c+1, MainFrame)
            if self.actS != 3:
                self.actS = 3
                
        elif self.W[3] and not self.W[5] and (self.actS != 1 or (self.W[1] and self.W[7])) and not (self.actS == 3 and self.W[0] and not self.W[1]):
            # mourer-se al sud
            self.moviment(self.r+1, self.c, MainFrame)
            if self.actS != 2:
                self.actS = 2

        elif self.W[5] and not self.W[7] and (self.actS != 3 or (self.W[3] and self.W[1])) and not (self.actS == 2 and self.W[2] and not self.W[3]):
            # mourer-se a l'oest
            self.moviment(self.r, self.c-1, MainFrame)
            if self.actS != 4:
                self.actS = 4

        elif self.W[7] and not self.W[1] and (self.actS != 2 or (self.W[5] and self.W[3])) and not (self.actS == 4 and self.W[4] and not self.W[5]):
            # mourer-se al nord si self.X[3] and not self.X[0]
            self.moviment(self.r-1, self.c, MainFrame)
            if self.actS != 1:
                self.actS = 1

        elif self.W[0] and not self.W[1] and self.actS != 2:
            # mourer-se al nord
            self.moviment(self.r-1, self.c, MainFrame)
            if self.actS != 1:
                self.actS = 1

        elif self.W[2] and not self.W[3] and self.actS != 4:
            # mourer-se a l'est
            self.moviment(self.r, self.c+1, MainFrame)
            if self.actS != 3:
                self.actS = 3

        elif self.W[4] and not self.W[5] and self.actS != 1:
            # mourer-se al sud
            self.moviment(self.r+1, self.c, MainFrame)
            if self.actS != 2:
                self.actS = 2

        elif self.W[6] and not self.W[7] and self.actS != 3:
            # mourer-se a l'oest
            self.moviment(self.r, self.c-1, MainFrame)
            if self.actS != 4:
                self.actS = 4

        else:
            # mourer-se al nord per defecte si es pot
            if not self.W[1] and self.actS != 2:
                self.moviment(self.r-1, self.c, MainFrame)
                self.actS = 1
            # mourerse a l'est per defecte si es pot
            elif not self.W[3]:
                self.moviment(self.r, self.c+1, MainFrame)
                self.actS = 3
            # mourerse al sud per defecte si es pot
            elif not self.W[5]:
                self.moviment(self.r+1, self.c, MainFrame)
                self.actS = 2
            # mourerse a l'oest per defecte si es pot
            elif not self.W[7]:
                self.moviment(self.r, self.c-1, MainFrame)
                self.actS = 4
        
        MainFrame.update() # actualitzem la cuadrícula per observar els canvis

    # ==================================================================================
    # nom: inicialitza
    # funció: Aquesta funció conté el bucle pel qual l'agent recoorrerà indefinidament
    #         el perímetre
    # paràmetres: `mf` --> tipus tk.Frame que conté tota la informació sobre la qua-
    #               drícula de l'ambient
    #             `r` --> posició de la y (o línies) inicial
    #             `c` --> posició de la x (o columnes) inicial
    # cridada: La funció es cridada desde la classe MainFrame, la qual inicialitza el joc
    #          quan s'ha pitjat al botó inicialitza
    # ==================================================================================
    def inicialitza(self, mf, r, c):
        self.r = r
        self.c = c
        mf.info(self.r, self.c).configure(bg='black')

        # Actualitzem W inicialment amb els valors que es coneixen de newW
        self.actualitzaW(mf)
        while True:
            # Inferim el moviment que s'ha de dur a terme segons
            # les percepcions obtingudes de W
            self.moure(mf)
            
            # Actualitzem W amb els valors que es coneixen de newW
            self.actualitzaW(mf)
            # Actualitzem el vector W segons el moviment que s'ha fet
            if self.actS == 1:
                self.unio(4, 6, 1, 3)
            elif self.actS == 2:
                self.unio(0, 2, 3, 1)
            elif self.actS == 3:
                self.unio(0, 6, 0, 2)
            elif self.actS == 4:
                self.unio(2, 4, 0, 2)
                

    # ==================================================================================
    # nom: Vel
    # funció: Amb aquesta funció permetem que es pugui canviar la velocitat de l'agent
    # paràmetres: `var` --> tipus int que ens arriba del radio button, indicant quin
    #               dels radio buttons està seleccionat
    # cridada: la funció és cridada quan l'usuari canvia la selecció del radio buttom
    # ==================================================================================
    def Vel(self, var):
        if var.get() == 1:
            self.vel = 0.5
        elif var.get() == 2:
            self.vel = 0.2
        else: # Velocitat per defecte
            self.vel = 0.1
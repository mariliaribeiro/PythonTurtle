#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com
# prg2-Pirata.py


'''
Um pirata bêbado faz uma volta aleatória e, em seguida, dá 100 passos 
para a frente, faz outra volta aleatória, dá mais 100 passos, 
vira outra quantidade aleatória, etc.
Um estudante de ciências sociais registra o ângulo de cada volta antes dos
100 serem dados. 
Seus dados experimentais são [160, -43, 270, -97, -43, 200, -940, 17, -86]. 
(Ângulos positivos são anti-horários). 
Use uma tartaruga para desenhar o caminho tomado pelo nosso amigo bêbado.
'''

from turtle import *
import random

angulos = [160, -43, 270, -97, -43, 200, -940, 17, -86]
gira = random.randint(0,50)
#shape('circle')

def pirata(angulos, gira):
    for i in range(10):
        angulo = random.choice(angulos)
        print(angulo)
        right(angulo)
        #circle(angulo)
        stamp()
        fd(100)
    print(gira)
    for i in range(gira):
        left(gira)
        speed('fast')

def main():
    bgcolor('#8B6914') # background
    title("Pirata bêbado")
    pirata(angulos, gira)

    mainloop()
    
if __name__ == '__main__':
    main()

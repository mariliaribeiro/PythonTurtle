#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com
# prg2-Estrela_Espiral.py


'''
Faça um programa que desenhe uma estrela em espiral, como esta:
http://michael0x2a.com/_assets/media/turtle-examples/spiraling-star.f72d.png
'''



from turtle import *

def estrela():
    hideturtle() # apaga tartaruga
    
    for i in range(4):
        left(230)
        forward(40 + (i * 110))
        left(200)
        forward(60 + (i * 140))
        left(215)
        forward(60 + (i * 170))
        left(210)
        forward(60 + (i * 170))
        right(135)
        forward(60 + (i * 100))

def main():
    title("Estrela de cinco pontas")
    estrela()

    mainloop()
    
if __name__ == '__main__':
    main()


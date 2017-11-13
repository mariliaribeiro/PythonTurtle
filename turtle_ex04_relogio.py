#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com
# prg2-Relogio.py

'''
Escreva um programa que faça um relógio com tartarugas, como este:
http://openbookproject.net/thinkcs/python/english3e/_images/tess_clock1.png
'''
from turtle import *

def turtle(distancia):
    shape('turtle')
    speed(50)
    penup()
    forward(distancia)
    stamp()
    backward(distancia)

def linha(distancia):
    penup()
    forward(distancia-10)
    pendown()
    forward(10)
    penup()
    backward(distancia)
    hideturtle()

def relogio(distancia=90):
    ponteiros = 12
    for i in range(ponteiros):
        linha(distancia)
        turtle(distancia+25)
        right(30)
    stamp()

def main():
    relogio()
    mainloop()
    
if __name__ == '__main__':
    main()

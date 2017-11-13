#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com
# prg2-Estrela.py


'''
Faça um programa que desenhe uma estrela de cinco pontas, como esta:
http://openbookproject.net/thinkcs/python/english3e/_images/star.png
'''

from turtle import *

def estrela():
    hideturtle() # apaga tartaruga
    for i in range(6):
        if i <= 1 or i == 4:
            forward(400)
            if i == 1: right(140) 
            else: right(150)
        elif i == 2 or i == 3:
            forward(370)
            right(140)
        else:
            forward(50)
 
def main():
    title("Estrela de cinco pontas")
    estrela()

    mainloop()
    
if __name__ == '__main__':
    main()



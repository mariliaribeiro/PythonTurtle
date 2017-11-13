#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com
# prg2-matriz_pontos.py

'''
Escreva um programa que dados os valores de linha e coluna, desenha uma 
matriz de pontos. Opcionalmente, a função pode receber outros parâmetros, 
como distância entre os pontos, cor e tamanho dos pontos, etc.
'''

from turtle import *

def matriz(linhas=5, colunas=3, distancia=20, tamanho=5, cor='#000000'):
    color(cor)    
    width(tamanho)
    for linha in range(linhas):
        for coluna in range(colunas):
            dot()
            penup() 
            forward(distancia) 
        backward(distancia*colunas+1)
        left(90)  
        forward(distancia)
        right(90)  
        hideturtle()

def main():    
    print('Este programa desenha uma matriz preenchida por pontos.')
    
    linhas = int(input('Informe a quantidade de linhas: '))
    colunas = int(input('Informe a quantidade de colunas: '))
    distancia = int(input('Informe a distância entre os pontos: '))
    tamanho = int(input('Informe o tamanho dos pontos: '))
    cor = input('Informe a cor dos pontos: ')
    
    matriz(linhas, colunas, distancia, tamanho, cor)
    #matriz()
                
    mainloop()
    
if __name__ == '__main__':
    main()

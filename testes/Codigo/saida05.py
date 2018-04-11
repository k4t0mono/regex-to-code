#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def q0(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "'0'..'9'"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "'a'..'z'"):
        indice+=1
        return q2(codigo,indice)
    return False

def q1(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "'a'..'z'"):
        indice+=1
        return q3(codigo,indice)
    return False

def q2(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "'0'..'9'"):
        indice+=1
        return q3(codigo,indice)
    if(codigo[indice] == "'a'..'z'"):
        indice+=1
        return q3(codigo,indice)
    return False

def q3(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q4(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().splitlines()
    print(0(linhas[0], indice))
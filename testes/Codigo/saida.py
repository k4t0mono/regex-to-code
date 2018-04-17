#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def q0(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "e"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "c"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "a"):
        indice+=1
        return q3(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q4(codigo,indice)
    return False

def q1(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "l"):
        indice+=1
        return q10(codigo,indice)
    if(codigo[indice] == "x"):
        indice+=1
        return q11(codigo,indice)
    return False

def q2(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "l"):
        indice+=1
        return q5(codigo,indice)
    if(codigo[indice] == "h"):
        indice+=1
        return q6(codigo,indice)
    return False

def q3(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "b"):
        indice+=1
        return q15(codigo,indice)
    return False

def q4(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "f"):
        indice+=1
        return q7(codigo,indice)
    return False

def q5(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "a"):
        indice+=1
        return q12(codigo,indice)
    return False

def q6(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "a"):
        indice+=1
        return q8(codigo,indice)
    return False

def q7(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "("):
        indice+=1
        return q20(codigo,indice)
    return False

def q8(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "r"):
        indice+=1
        return q9(codigo,indice)
    return False

def q9(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q10(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "s"):
        indice+=1
        return q16(codigo,indice)
    return False

def q11(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "t"):
        indice+=1
        return q13(codigo,indice)
    return False

def q12(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "s"):
        indice+=1
        return q24(codigo,indice)
    return False

def q13(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "e"):
        indice+=1
        return q14(codigo,indice)
    return False

def q14(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "n"):
        indice+=1
        return q17(codigo,indice)
    return False

def q15(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "s"):
        indice+=1
        return q21(codigo,indice)
    return False

def q16(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "e"):
        indice+=1
        return q18(codigo,indice)
    return False

def q17(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "d"):
        indice+=1
        return q24(codigo,indice)
    return False

def q18(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "{"):
        indice+=1
        return q19(codigo,indice)
    return False

def q19(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "e"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "l"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "p"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "u"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "n"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "c"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "m"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "z"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "b"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "t"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "r"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "a"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "f"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "o"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "v"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "d"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "w"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "h"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "x"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "q"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "k"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "y"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "s"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "g"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q22(codigo,indice)
    if(codigo[indice] == "j"):
        indice+=1
        return q22(codigo,indice)
    return False

def q20(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "6"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "4"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "0"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "2"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "1"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "9"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "8"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "5"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "7"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "3"):
        indice+=1
        return q25(codigo,indice)
    return False

def q21(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "t"):
        indice+=1
        return q23(codigo,indice)
    return False

def q22(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "}"):
        indice+=1
        return q9(codigo,indice)
    return False

def q23(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "r"):
        indice+=1
        return q26(codigo,indice)
    return False

def q24(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "s"):
        indice+=1
        return q9(codigo,indice)
    return False

def q25(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "6"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "4"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "0"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "2"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "1"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "9"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "8"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == ">"):
        indice+=1
        return q27(codigo,indice)
    if(codigo[indice] == "5"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "7"):
        indice+=1
        return q25(codigo,indice)
    if(codigo[indice] == "3"):
        indice+=1
        return q25(codigo,indice)
    return False

def q26(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "a"):
        indice+=1
        return q28(codigo,indice)
    return False

def q27(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "6"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "4"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "0"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "2"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "1"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "9"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "8"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "5"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "7"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "3"):
        indice+=1
        return q29(codigo,indice)
    return False

def q28(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "c"):
        indice+=1
        return q30(codigo,indice)
    return False

def q29(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "6"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "4"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "0"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "2"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "1"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "9"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == ")"):
        indice+=1
        return q9(codigo,indice)
    if(codigo[indice] == "8"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "5"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "7"):
        indice+=1
        return q29(codigo,indice)
    if(codigo[indice] == "3"):
        indice+=1
        return q29(codigo,indice)
    return False

def q30(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "t"):
        indice+=1
        return q9(codigo,indice)
    return False


def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().strip().splitlines()
    for lin in linhas:
        print(q0(lin, indice))
        
main(sys.argv)
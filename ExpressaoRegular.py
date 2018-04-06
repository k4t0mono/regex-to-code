#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Automato import Automato
from Noh import Noh

class ER:
    simbolosEspeciais = None
    variaveis = None
    expressao = None

    def __init__(self):
        self.simbolosEspeciais = {
            "*" : "*",
            "+" : "+",
            "|" : "|",
            "(" : "(",
            ")" : ")",
            "[" : "[",
            "]" : "]",
            "-" : "-",
            "." : "."
        }

        self.variaveis = {}
        self.expressao = []

    # Recebe o nome do arquivo com a expressao regular
    def lerArquivo(self, nomeArquivo):
        arquivo = open(nomeArquivo, 'r')
        linhas = arquivo.read().splitlines()
        self.lerVariaveis(linhas)
        self.lerExpressao(linhas)

    # Le as "variaveis" da expressao
    def lerVariaveis(self, linhas):
        posLinha = 0
        while(linhas[posLinha] != "{"):
            linha = linhas[posLinha]
            indice = ""
            posCaractere = 0
            while(posCaractere < len(linha) and linha[posCaractere] != " "):
                indice += linha[posCaractere]
                posCaractere += 1

            while(posCaractere < len(linha) and linha[posCaractere] == " "):
                posCaractere += 1

            posCaractere += 1
            while (posCaractere < len(linha) and linha[posCaractere] == " "):
                posCaractere += 1

            valor = ""
            while (posCaractere < len(linha)):
                valor += linha[posCaractere]
                posCaractere += 1
            self.variaveis[indice] = valor

            posLinha += 1

    # Le a expressao em si, eliminando espacos inuteis
    def lerExpressao(self, linhas):
        posLinha = 0
        while (linhas[posLinha] != "{"):
            posLinha += 1

        posLinha += 1
        ex = ""
        while(linhas[posLinha] != "}"):
            i = 0
            while(linhas[posLinha][i] == " " or linhas[posLinha][i] == "\t"):
                i += 1
            cont = 0
            while (i < len(linhas[posLinha])):
                if (linhas[posLinha][i] == "\t"):
                    l = list(linhas[posLinha])
                    l[i] = ' '
                    linhas[posLinha] = ''.join(l)
                if(linhas[posLinha][i] != " " and linhas[posLinha][i] != "\t"):
                    cont = 0
                else:
                    cont += 1
                if(cont < 2):
                    ex += linhas[posLinha][i]
                i += 1
            if(linhas[posLinha + 1] != "}"):
                ex += " "
            posLinha += 1
            self.expressao = ex

    def criarAFND(self, indice):
        lista = []
        parenteses = {}
        self.inicializaListas(parenteses)
        self.iniciaEstruturas(lista, parenteses)
        saida = "{ \n"
        for noh in lista:
            saida += "inicio : " + str(noh.inicio) + ", fim : " + str(noh.fim) + " peso : " + str(noh.peso) + "\n"

        print(saida + "}")
        print(parenteses)





    # Inicializa o dicionario de matrizes e gera a heap maxima de nos
    def iniciaEstruturas(self, lista, parenteses):
        peso = 0
        i = 0
        while(i < len(self.expressao)):
            if(self.expressao[i] == "("):
                peso += 1
                parenteses[peso].append([i, -1])
            elif(self.expressao[i] == ")"):
                pos = self.buscaPrimeiroNone(parenteses, peso)
                parenteses[peso][pos][1] = i
                peso -= 1
            elif(self.expressao[i] != "." and self.expressao[i] != " " and
                 self.expressao[i] != "+" and self.expressao[i] != "*"  and
                 self.expressao[i] != "|"):
                inicio = i
                fim = self.pegaFimPalavra(inicio)
                noh = Noh(inicio, fim - 1, peso)
                lista.append(noh)
                i = fim - 1
            i += 1


    # Busca o primeiro parenteses nao balanceado com indice igual ao peso passado por parametro
    def buscaPrimeiroNone(self, parenteses, peso):
        lista = parenteses[peso]
        for i in range(len(lista)):
            if(lista[i][1] == -1):
                return i

    # Descobre a ultima posicao da letra de uma palavra a partir de seu indice de inicio
    def pegaFimPalavra(self, inicio):
        j = inicio
        while(j < len(self.expressao)):
            if(self.expressao[j] == "." or self.expressao[j] == " " or
               self.expressao[j] == "+" or self.expressao[j] == "*"  or
               self.expressao[j] == "|" or self.expressao[j] == "(" or
               self.expressao[j] == ")"):
                return (j)
            j += 1

        return (j)

    def inicializaListas(self, parenteses):
        cont = 0
        pesoMax = 0
        for caractere in self.expressao:
            if(caractere == "("):
                cont += 1
                if(cont > pesoMax):
                    pesoMax = cont
            elif(caractere == ")"):
                cont -= 1
        for i in range(pesoMax + 1):
            parenteses[i] = []

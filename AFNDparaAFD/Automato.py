#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AFNDparaAFD.LeituraEscrita import Arquivo
from AFNDparaAFD.AutomatoFD import AutomatoFD

class Automato:
    estados = None                  #lista de estados do automato
    estadosDic = None               #dicionario que referencia os estados
    alfabeto = None
    inicial = None
    finais = None                   #dicionario de estados finais
    
    pilha = None

    #cria um dicionario de estados para o automato

    def __init__(self, nomeArq = None):
        self.pilha = []
        
        if(nomeArq == None):        #se nao for passado o nome do arquivo por parametro, cria-se um automato vazio
            self.estados = []
            self.estadosDic = {}
            self.alfabeto = []
            self.finais = {}
            
          

        arquivo = Arquivo(nomeArq, 'r')         #instancia um objeto da classe arquivo (no arquivo LeituraEscrita)

        #operacoes de leitura do arquivo
        self.estados = arquivo.leEstados()
        self.estadosDic = self.criaDicionario(self.estados)
        self.alfabeto = arquivo.leAlfabeto()
        arquivo.leTransicoes(self)
        self.inicial = arquivo.leInicial()
        self.finais = arquivo.leFinais()

        #marca os estados finais
        for i in range(len(self.estados)):
            if(self.estados[i].idEstado in self.finais):
                self.estados[i].final = True
    
    def criaDicionario(self, estados):
        estadosDic = {}
        for i in range(len(estados)):
            estadosDic[estados[i].idEstado] = estados[i]
        return estadosDic
        
    def getAlcancaveis(self,estado):
        if(estado.cor == "P"):
            return estado.estadosAlcancaveis
            
        if(estado.cor == "B"):
            self.pilha.append(estado)
            estado.cor = "C"
            estado.estadosAlcancaveis.add(estado)
            for transicao in estado.transicoes:
                if(transicao.letra == "λ"):
                    destino = transicao.destino
                    if(destino.cor == "C"):
                        i = 1
                        aux = self.pilha[-i]
                        iguais = []
                        while(aux != destino):
                            iguais.append(aux)
                            i+=1
                            aux = self.pilha[-i]
                        for item in iguais:
                            for alcancavel in item.estadosAlcancaveis:
                                destino.estadosAlcancaveis.add(alcancavel)
                            item.estadosAlcancaveis = destino.estadosAlcancaveis
                        
                    else:
                        alcancaveisDoDestino = self.getAlcancaveis(destino)
                        for alcancavel in alcancaveisDoDestino:
                            estado.estadosAlcancaveis.add(alcancavel)
            self.pilha.remove(estado)
            estado.cor = "P"
            return estado.estadosAlcancaveis


    def tranformaEmAFD(self):

        automatoFD = AutomatoFD()
        estadoInicial = self.estadosDic[self.inicial]
        vetorEstadosIniciais = estadoInicial.estadosAlcancaveis
        PEinicial = automatoFD.fundirEstadosSeNaoForamFundidos(vetorEstadosIniciais)

        automatoFD.adicionaPE(PEinicial)
        automatoFD.inicial = PEinicial

        while(not automatoFD.acabou()):
            for PE in automatoFD.PErestantes:
                for letra in self.alfabeto:
                    if(letra != "λ"):
                        vetorEstados = []
                        for transicao in PE.transicoes:
                            if(transicao.letra == letra):
                                if(transicao.destino not in vetorEstados):
                                    for estado in transicao.destino.estadosAlcancaveis:
                                        vetorEstados.append(estado)
                        PEdestino = automatoFD.fundirEstadosSeNaoForamFundidos(vetorEstados)
                        if(PEdestino is not None):
                            automatoFD.adicionaPE(PEdestino)
                            PE.criarTransicaoReal(letra, PEdestino)
                PE.verificado = True
                automatoFD.PErestantes.remove(PE)
        automatoFD.renomearEstados()
        #~ self.setFinais(automatFD)
        automatoFD.alfabeto = self.alfabeto
        return automatoFD

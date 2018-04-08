#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
class Noh:
    indice = None
    inicio = None
    fim = None
    peso = None
    pilhaParenteses = None

    def __init__(self, indice, inicio, fim, peso, pilhaParenteses):
        self.indice = indice
        self.inicio = inicio
        self.fim = fim
        self.peso = peso
        self.pilhaParenteses = copy.copy(pilhaParenteses)
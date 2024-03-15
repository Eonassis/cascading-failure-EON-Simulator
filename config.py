#!/usr/bin/env python
# -*- coding: utf-8 -*-

#sementes random 
RANDOM_SEED = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

#tempo maximo de simulacao
MAX_TIME = 10000000  

#ERLANG_MIN = 300
ERLANG_MIN = 550

#ERLANG_MAX = 380
ERLANG_MAX = 850

#pabrao 20
ERLANG_INC = 50

#quantidade de repeticoes padrao 10
REP = 10

#numero de requisicoes padrao 100.000 100000
NUM_OF_REQUESTS = 100000

#tramanho das bandas >>>>>> MEXER NO CODIGO AO ALTERAR BANDAS >>>>
BANDWIDTH = [100, 150, 200, 250, 300, 350, 400]

#classes de trafego
CLASS_TYPE = [1, 2, 3]

#divisao do trafego por classes
CLASS_WEIGHT = [0.15, 0.25, 0.60]

#topologia
TOPOLOGY = 'usa'

##### aki aumenta o tarfego, reduzindo o tempo por requisicao ########
#tempo por requisicao padrao 1.0
HOLDING_TIME = 1.0


#quantidade slot Eon 400
SLOTS = 400

#tamanho do slot ghz
SLOT_SIZE = 12.5

#N_PATH 15
N_PATH = 10

#tempo inicio do desastre 3600
TIME_CASC_INI = 0.03600

#tempo entre os desastres 
TIME_CASC = 0.03600

#duracao do desastre
TIME_DESAS = 14400 #43200

#pontos de falha = pontoA, pontoB, tempo para falhar 
			 #[[6,9,1],[9,11,3],[7,9,6],[9,12,6],[9,10,9],[6,7,9],[11,12,9]]
LINK_POINTS = [[6,9,1],[9,11,10],[7,9,20],[9,12,20],[9,10,30],[6,7,30],[11,12,30]]

#pontos de falha = no, tempo [[4,2], [2,5]]
NODE_POINTS = [[9,31]]

#alpha 
ALPHA = [1 , 0.5 , 0.4, 0.3, 0.1]

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
REP = 2

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
HOLDING_TIME = 8.6400


#quantidade slot Eon 400
SLOTS = 80

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

#pontos de falha = pontoA, pontoB, tempo para falhar [[1,2,1], [1,4,2]]
LINK_POINTS = [[6,9,1],[9,11,3],[7,9,6],[9,12,6],[9,10,9],[6,7,9],[11,12,9]]

#pontos de falha = no, tempo [[4,2], [2,5]]
NODE_POINTS = [[9,9]]




import simpy
import random
import numpy as np
import networkx as nx
import math
import time
from itertools import islice
import csv
import pickle
import sys
from random import *

topology = nx.read_weighted_edgelist('topology/' + TOPOLOGY, nodetype=int)

k_paths = {}

#zera os slots
for u, v in list(topology.edges):
	topology[u][v]['capacity'] = [0] * SLOTS
	topology[u][v]['failed'] = False
	topology[u][v]['fallprob'] = 0


#Calcula os k-menores caminhos entre pares o-d
def k_shortest_paths(G, source, target, k, weight='weight'):
	return list(islice(nx.shortest_simple_paths(G, source, target, weight=weight), k))


#pre-processamento dos caminhos mais curtos
for i in list(topology.nodes()):
	for j in list(topology.nodes()):
		if i!= j:
			k_paths[i,j] = k_shortest_paths(topology, i, j, N_PATH, weight='weight')

# Calcula a distância do caminho de acordo com os pesos das arestas               
def Distance(path):
	global topology 
	soma = 0
	for i in range(0, (len(path)-1)):
		soma += topology[path[i]][path[i+1]]['weight']
	return (soma)


















def DSSP_paths(src, dst, bandwidth):
    slot_map = []

    # Obtém uma lista de 5 caminhos
    new_paths_N_PATH = k_paths[src, dst][:N_PATH]
    #percorre todos os 5 caminhos
    for i_path in new_paths_N_PATH:
        all_bandwidth, all_slots  = PreAlocacao_DSSP(i_path,bandwidth)
        bandwidth = bandwidth - all_bandwidth
        slot_map.append(i_path, all_slots)
        #fistfit chama numero requisicao,slot-inicial,slot-final,caminho

    return slot_map


def PreAlocacao_DSSP(i_path,bandwidth):
	FreeSlots, FreeSlotsMatrix, INSlotsfreeMatrix = free_slots(i_path)
	fator_bw = Mod_band(int(Distance(i_path)))
	all_bandwidth = FreeSlots / fator_bw
	all_slots = FreeSlotsMatrix
	return all_bandwidth, all_slots

# Calcula o formato de modulação de acordo com a distância do caminho    
def Mod_band(dist):
	if dist <= 500:
		return float(4 * SLOT_SIZE)
	elif 500 < dist <= 1000:
		return float(3 * SLOT_SIZE)
	elif 1000 < dist <= 2000:
		return float(2 * SLOT_SIZE)
	else:
		return float(1 * SLOT_SIZE)

# Calcula slots livres no caminho
def free_slots(path):
    global topology
    current_consecutive = []  # Lista temporária para armazenar o conjunto atual de slots consecutivos
    for slot in range(len(topology[path[0]][path[1]]['capacity'])):
        if topology[path[0]][path[1]]['capacity'][slot] == 0:
            k = 0
            for ind in range(len(path) - 1):
                if topology[path[ind]][path[ind + 1]]['capacity'][slot] == 0:
                    k += 1
            if k == len(path) - 1:
                current_consecutive.append(slot)
    grupos = []
    IFgrupos = []
    grupo_atual = []

    for numero in current_consecutive:
        # Se o grupo atual estiver vazio ou se o número for igual ao último número + 1, adicione-o ao grupo atual.
        if not grupo_atual or numero == grupo_atual[-1] + 1:
            grupo_atual.append(numero)
        else:
            # Caso contrário, termine o grupo atual e comece um novo grupo.
            grupos.append(grupo_atual)
            IFgrupos.append([grupo_atual[0], grupo_atual[-1]])
            grupo_atual = [numero]

    # Certifique-se de adicionar o último grupo à lista de grupos.
    if grupo_atual:
        grupos.append(grupo_atual)
        IFgrupos.append([grupo_atual[0], grupo_atual[-1]])

    #print(grupos)
    #print(IFgrupos)
	#FreeSlots, FreeSlotsMatrix, INSlotsfreeMatrix
    return current_consecutive, grupos, IFgrupos


#recebe a distancia do caminho
distance = int(Distance(i_path))
fator_bw = Mod_ba
FirstFit(count, self.check_path[1],self.check_path[2],paths[i])
spectro = [self.check_path[1], self.check_path[2]]
processo = env.process(Desalocate(count,paths[i],spectro,holding_time, env.now))
# Tabela de requisições aceitas com n° da req, classe ,num_slots, path, posição no spectro, inicio ,holding_time, frac_ht, hops, distancia_km, bandwidth
req_accepts.append([count, class_type, num_slots, paths[i], spectro, env.now , holding_time, 0, len(paths[i])-1, distance, bandwidth , processo])
ativo[count] = 1




# Exemplo de uso:
src = 3
dst = 6
bandwidth = 200

resultado = DSSP_paths(src, dst, bandwidth)
print(resultado)  # Isso imprimirá: 200

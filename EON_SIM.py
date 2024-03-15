#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('..')  # Adicione o diretório pai ao sys.path
from config import *


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


# Estrutura de dados para manter o registro de solicitações
solicitacoes_em_andamento = []
req_accepts = []
ativo = {}
k_paths = {}
LINK_POINTSF = []
NODE_POINTSF = []
Simfim = False

restauradasF = 0
afetadasF = 0
sum_time_up = 0
sum_ht = 0
NumReqBlocked2x = 0
Vet_NumReqBlocked2x = []
Numsaltos = 0
Qtd_sol_Numsaltos = 0 

desalocateReq1 = []
desalocateReq2 = []
desalocateReqRerr = []
desalocateReqRerr2 = []

NumReqBlocked = 0 
cont_req = 0
NumReq_100 = 0 
NumReq_150 = 0 
NumReq_200 = 0 
NumReq_250 = 0 
NumReq_300 = 0 
NumReq_350 = 0 
NumReq_400 = 0 
NumReq_classe1 = 0 
NumReq_classe2 = 0 
NumReq_classe3 = 0 
NumReqBlocked_100 = 0
NumReqBlocked_150 = 0
NumReqBlocked_200 = 0
NumReqBlocked_250 = 0
NumReqBlocked_300 = 0
NumReqBlocked_350 = 0
NumReqBlocked_400 = 0
NumReqBlocked_classe1 = 0
NumReqBlocked_classe2 = 0
NumReqBlocked_classe3 = 0

#NOVAS
bloqueio_rerroteamento_pr = 0
bloqueio_rerroteamento_cos1_pr = 0 
bloqueio_rerroteamento_cos2_pr = 0
bloqueio_rerroteamento_cos3_pr = 0
bloqueio_rerroteamento_100_pr = 0
bloqueio_rerroteamento_150_pr = 0
bloqueio_rerroteamento_200_pr = 0
bloqueio_rerroteamento_250_pr = 0
bloqueio_rerroteamento_300_pr = 0
bloqueio_rerroteamento_350_pr = 0
bloqueio_rerroteamento_400_pr = 0

total_req_afetadas = 0
total_req_afetadas_od = 0
total_req_afetadas_od_cos1 = 0
total_req_afetadas_od_cos2 = 0
total_req_afetadas_od_cos3 = 0
total_req_afetadas_od_100 = 0
total_req_afetadas_od_150 = 0
total_req_afetadas_od_200 = 0
total_req_afetadas_od_250 = 0
total_req_afetadas_od_300 = 0
total_req_afetadas_od_350 = 0
total_req_afetadas_od_400 = 0
total_req_restauradas = 0

mensagem_impressa = False

# variaveis pr 
bloqueio_rerroteamento_pr_pr = 0
bloqueio_rerroteamento_pr_ahp_pr = 0
bloqueio_rerroteamento_pr_ahp_dg_pr = 0
total_req_restauradas_pr_pr = 0
total_req_afetadas_od_pr = 0
aceitas_pr = 0
bloqueadas_pr = 0
afetadas_pr = []
restauradas_pr = 0
nao_restauradas_pr = []
rr_nao_restauradas_pr = []


#zera os slots
for u, v in list(topology.edges):
	topology[u][v]['capacity'] = [0] * SLOTS
	topology[u][v]['failed'] = False
	topology[u][v]['fallprob'] = 0



def Simulador(self, rate):
		global topology, solicitacoes_em_andamento, req_accepts, ativo, k_paths, Simfim
		self.random = Random()
		self.nodes = list(topology.nodes())

		global NumReqBlocked
		global cont_req
		global NumReq_100
		global NumReq_150
		global NumReq_200
		global NumReq_250
		global NumReq_300
		global NumReq_350
		global NumReq_400
		global NumReq_classe1
		global NumReq_classe2
		global NumReq_classe3
		global NumReqBlocked_100
		global NumReqBlocked_150
		global NumReqBlocked_200
		global NumReqBlocked_250
		global NumReqBlocked_300
		global NumReqBlocked_350
		global NumReqBlocked_400
		global NumReqBlocked_classe1
		global NumReqBlocked_classe2
		global NumReqBlocked_classe3
		
		
		#NOVAS METRICAS
		global bloqueio_rerroteamento_pr
		global bloqueio_rerroteamento_cos1_pr 
		global bloqueio_rerroteamento_cos2_pr
		global bloqueio_rerroteamento_cos3_pr
		global bloqueio_rerroteamento_100_pr
		global bloqueio_rerroteamento_150_pr
		global bloqueio_rerroteamento_200_pr
		global bloqueio_rerroteamento_250_pr
		global bloqueio_rerroteamento_300_pr
		global bloqueio_rerroteamento_350_pr
		global bloqueio_rerroteamento_400_pr
		global total_req_afetadas
		global total_req_afetadas_od
		global total_req_afetadas_od_cos1
		global total_req_afetadas_od_cos2
		global total_req_afetadas_od_cos3
		global total_req_afetadas_od_100
		global total_req_afetadas_od_150
		global total_req_afetadas_od_200
		global total_req_afetadas_od_250
		global total_req_afetadas_od_300
		global total_req_afetadas_od_350
		global total_req_afetadas_od_400
		global total_req_restauradas
		global sum_time_up, sum_ht, Numsaltos , Qtd_sol_Numsaltos, Vet_NumReqBlocked2x

		#pre-processamento dos caminhos mais curtos
		for i in list(topology.nodes()):
			for j in list(topology.nodes()):
				if i!= j:
					k_paths[i,j] = k_shortest_paths(topology, i, j, N_PATH, weight='weight')
		
		env.process(GerarFalhas())

		for count in range(1, NUM_OF_REQUESTS + 1):
			yield env.timeout(self.random.expovariate(rate))
			class_type = np.random.choice(CLASS_TYPE, p=CLASS_WEIGHT)
			src, dst = self.random.sample(self.nodes, 2)
			bandwidth = self.random.choice(BANDWIDTH)
			holding_time = self.random.expovariate(HOLDING_TIME)
			sum_ht += holding_time
			conta_requisicao_banda(bandwidth)
			conta_requisicao_classe(class_type)
			ConjSlots = 0
			#if topology[src][dst]['failed'] == True: # Verificar se o-d pode receber conexão
			if topology.has_edge(src, dst) and 'failed' in topology[src][dst] and topology[src][dst]['failed'] == True:
				total_req_afetadas_od += 1
				NumReqBlocked +=1
				Vet_NumReqBlocked2x.append(count)
				Bloqueio_falha_od_cos(class_type)
				Bloqueio_falha_od_banda(bandwidth)
			else:
				paths = k_paths[src,dst]
				flag = 0
				global contador
				for i in range(N_PATH):
					distance = int(Distance(paths[i]))
					num_slots = int(math.ceil(Modulation(distance, bandwidth)))
					self.check_path = PathIsAble(num_slots,paths[i])
					#print("banda solicitada ",bandwidth, "distance", distance , "num_slots", num_slots)
					#print(count, self.check_path[1],self.check_path[2],paths[i])
					#print(count, self.check_path[1],self.check_path[2],paths[i])
					if self.check_path[0] == True:
						cont_req += 1
						FirstFit(count, self.check_path[1],self.check_path[2],paths[i])
						spectro = [self.check_path[1], self.check_path[2]]
						processo = env.process(Desalocate(count,paths[i],spectro,holding_time, env.now))
						# Tabela de requisições aceitas com n° da req, classe ,num_slots, path, posição no spectro, inicio ,holding_time, frac_ht, hops, distancia_km, bandwidth
						req_accepts.append([count, class_type, num_slots, paths[i], spectro, env.now , holding_time, 0, len(paths[i])-1, distance, bandwidth , processo])
						ativo[count] = 1
						#print("Ativa count",count, class_type, num_slots, paths[i], spectro, env.now , holding_time, 0, len(paths[i])-1, distance, bandwidth , processo)
						#print(count, self.check_path[1],self.check_path[2],paths[i])
						#for u, v in list(topology.edges):
						#	print(topology[u][v]['capacity'])
						flag = 1
						ConjSlots += 1
						Numsaltos +=  len(paths[i])
						Qtd_sol_Numsaltos += 1
						break 
				if flag == 0:
						#print("O-D" , paths[i] ,"bloqueou ", bandwidth, "classe ", class_type , env.now)
						#contador += 1
						NumReqBlocked +=1
						#print("bloqueou3")
						Vet_NumReqBlocked2x.append(count)
						conta_bloqueio_requisicao_banda(bandwidth)
						conta_bloqueio_requisicao_classe(class_type)
						#pass
		Simfim =  True

def Bloqueio_falha_od_cos(cos):
	global total_req_afetadas_od_cos1
	global total_req_afetadas_od_cos2
	global total_req_afetadas_od_cos3
	if cos ==1:
		total_req_afetadas_od_cos1 += 1
	elif cos ==2:
		total_req_afetadas_od_cos2 += 1
	else:
		total_req_afetadas_od_cos3 += 1




def Bloqueio_falha_od_banda(banda):
	global total_req_afetadas_od_100
	global total_req_afetadas_od_150
	global total_req_afetadas_od_200
	global total_req_afetadas_od_250
	global total_req_afetadas_od_300
	global total_req_afetadas_od_350
	global total_req_afetadas_od_400
	if banda == 100:
		total_req_afetadas_od_100 += 1
	elif banda == 150:
		total_req_afetadas_od_150 += 1
	elif banda == 200:
		total_req_afetadas_od_200 += 1
	elif banda == 250:
		total_req_afetadas_od_250 += 1
	elif banda == 300:
		total_req_afetadas_od_300 += 1
	elif banda == 350:
		total_req_afetadas_od_350 += 1
	else:
		total_req_afetadas_od_400 +=1 

def MaxFlow(path):
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
    return current_consecutive, grupos, IFgrupos

# Calcula o formato de modulação de acordo com a distância do caminho    
def FatorModulation(dist):
	if dist <= 500:
		return (float(4 * SLOT_SIZE))
	elif 500 < dist <= 1000:
		return (float(3 * SLOT_SIZE))
	elif 1000 < dist <= 2000:
		return (float(2 * SLOT_SIZE)) 
	else:
		return (float(1 * SLOT_SIZE))
               
# Função para gerar falhas na rede
def GerarFalhas():
    global topology, LINK_POINTSF, NODE_POINTSF, Simfim, mensagem_impressa
    while True:
        for link_point in LINK_POINTS:
            if link_point not in LINK_POINTSF and env.now >= link_point[2]:
                # Falha no link entre link_point[0] e link_point[1]
                FalhaNoLink(link_point[0], link_point[1])
                LINK_POINTSF.append(link_point)
                print("falha gerada", link_point )
        for node_point in NODE_POINTS:
            if node_point not in NODE_POINTSF and env.now >= node_point[1]:
                # Falha no nó node_point[0]
                FalhaNoNo(node_point[0])
                NODE_POINTSF.append(node_point)
        if env.now >= TIME_DESAS:
            for u, v in list(topology.edges):
                topology[u][v]['failed'] = False
            if not mensagem_impressa:
                print ("links reestabelecidos")
                mensagem_impressa = True
		# Verifique se todas as requisições foram concluídas
        if Simfim == True:
            break  # Encerra o loop se todas as requisições foram concluídas
		
        yield env.timeout(1)  # Verifica a cada unidade de tempo
        #print("falha gerada")


# Função para lidar com falhas em links
def FalhaNoLink(node1, node2):
	global topology, sum_time_up

	# Verifique se o link entre node1 e node2 existe
	if topology.has_edge(node1, node2):
		# Marque o link como falho (você pode adicionar um atributo 'failed' ao link)
		topology[node1][node2]['failed'] = True
		reqfalhou = []
		reqfalhou = Quem_falhou_link(node1, node2)

		# Chame Desalocate para liberar slots de espectro nos links afetados
		for i in range(len(reqfalhou)):
			print("FalhaNoLink3")           
			process = reqfalhou[i][11]
			process.interrupt()
			Desalocate(reqfalhou[i][0],reqfalhou[i][3],reqfalhou[i][4],reqfalhou[i][6], reqfalhou[i][5])
			# Implemente aqui a lógica para o reroteamento do tráfego afetado
			Reroteamento(reqfalhou[i][0], reqfalhou[i][3], reqfalhou[i][4], reqfalhou[i][6], reqfalhou[i][3][0], reqfalhou[i][3][-1], reqfalhou[i][10], reqfalhou[i][1])

		# Imprima uma mensagem para indicar que o link falhou
		print(f"Falha no link entre os nós {node1} e {node2}")

	else:
		# O link não existe, imprima uma mensagem de erro
		print(f"Erro: O link entre os nós {node1} e {node2} não existe na topologia.")



########################################################################################
# Função para lidar com falhas em nós
def FalhaNoNo(node):
    global topology, sum_ht, sum_time_up

    # Verifique se o nó existe na topologia
    if node in topology.nodes:
        # Marque o nó como falho (você pode adicionar um atributo 'failed' ao nó)
        #topology.nodes[node]['failed'] = True

        # Itere sobre todos os links conectados ao nó falho
        for neighbor in topology.neighbors(node):
            # Verifique se o link ainda existe e marque-o como falho
            if topology.has_edge(node, neighbor):
                topology[node][neighbor]['failed'] = True
                reqfalhou = []
                reqfalhou = Quem_falhou_link(node, neighbor)

                # Chame Desalocate para liberar slots de espectro nos links afetados
                for i in range(len(reqfalhou)):
                    process = reqfalhou[i][11]
                    process.interrupt()
                    Desalocate(reqfalhou[i][0],reqfalhou[i][3],reqfalhou[i][4],reqfalhou[i][6],reqfalhou[i][5])
                    # Implemente aqui a lógica para o reroteamento do tráfego afetado
                    Reroteamento(reqfalhou[i][0], reqfalhou[i][3], reqfalhou[i][4], reqfalhou[i][6], reqfalhou[i][3][0], reqfalhou[i][3][-1], reqfalhou[i][10], reqfalhou[i][1])

                # Imprima uma mensagem para indicar que o link falhou
                print(f"Falha no link entre os nós {node} e {neighbor}")

        # Imprima uma mensagem para indicar que o nó falhou
        print(f"Falha no nó {node}")

    else:
        # O nó não existe, imprima uma mensagem de erro
        print(f"Erro: O nó {node} não existe na topologia.")

# Função para reroteamento após falha
#Reroteamento(count, path, spectro, holding_time, src, dst, bandwidth)
def Reroteamento(count, path, spectro, holding_time, src, dst, bandwidth, class_type):
    global topology, req_accepts, ativo, total_req_restauradas, bloqueio_rerroteamento_pr, restauradasF, afetadasF, ativo
    global contador, afetadas_pr, total_req_restauradas_pr_pr, restauradas_pr, nao_restauradas_pr, rr_nao_restauradas_pr, bloqueio_rerroteamento_pr_pr
    global sum_time_up, sum_ht, desalocateReqRerr, desalocateReqRerr2, NumReqBlocked , Numsaltos , Qtd_sol_Numsaltos, Vet_NumReqBlocked2x
    print("Reroteamento akii>>")
    if count not in desalocateReqRerr:
        afetadasF += 1
        sum_ht += holding_time
    
    afetadas_pr.append(count)
    
    if topology.has_edge(src, dst) and 'failed' in topology[src][dst] and topology[src][dst]['failed'] == True:
        #total_req_afetadas_od += 1
        #failure.Bloqueio_falha_od_cos(request[1])
        #failure.Bloqueio_falha_od_banda(request[10])
        #print("blockkkkk", count )
        #print("Reroteamento akii>> failed")
        NumReqBlocked +=1
        Vet_NumReqBlocked2x.append(count)
        Bloqueio_rerroteamento_cos_pr(class_type)
        Bloqueio_rerroteamento_banda_pr(bandwidth)
        bloqueio_rerroteamento_pr += 1
        #pass
    else:
        new_paths = k_paths[src,dst]
        capacity = 0
        Datapaths = []
        found = False
        #print("Reroteamento akii>> no failed")
        #print([topology[u][v]['capacity'] for u, v in topology.edges])
        for i in range(N_PATH):
            distance = int(Distance(new_paths[i]))  # Calcule a distância
            Fatormodulation = FatorModulation(distance)
            FreeSlots, FreeSlotsMatrix, INSlotsfreeMatrix = MaxFlow(new_paths[i])
            FreeSlotsSun = len(FreeSlots)
            capacityCalc = Fatormodulation * FreeSlotsSun
            capacity += capacityCalc
            num_slots = int(math.ceil(Modulation(distance, bandwidth)))
            Datapaths.append([new_paths[i], distance, Fatormodulation, FreeSlotsSun , capacityCalc, FreeSlotsMatrix, FreeSlots, INSlotsfreeMatrix , num_slots ])
        Contbandwidth = bandwidth
        #print("banda solicitada ",Contbandwidth)
        ConjSlots = 0
        if capacity >= bandwidth:
            for sublista in Datapaths:
                coluna_7 = sublista[7]
                for pathsAble in coluna_7:
                    #print(f"{sublista[3]}  {sublista[2]} {sublista[0]} { pathsAble [0]} { pathsAble [1]} { sublista[8]}")
                    Transporte = sublista[2] *(pathsAble[1]-pathsAble[0]+1)
                    DadosSOL = [sublista[0], pathsAble [0],pathsAble[1]]
                    if Transporte > Contbandwidth:
                        Transporte = Contbandwidth
                        DadosSOL = [sublista[0], pathsAble[0], pathsAble[0] + int(math.ceil(Modulation(sublista[1], Contbandwidth)))-1]
                    Contbandwidth -= Transporte
                    #print(count, DadosSOL[1], DadosSOL[2], DadosSOL[0])
                    ##print("antes da alocacao: ", count , "slots:",  sublista[5])
                    ##print("requisicao: ", count , "origem destino:", src, dst, "numero slots:", DadosSOL[1], DadosSOL[2], )
                    if count not in desalocateReqRerr:
                        ##sum_ht += holding_time
                        desalocateReqRerr.append(count)
                        total_req_restauradas += 1
                        restauradasF +=1
                        #print("rerout_sum_ht>>>>>", sum_ht, holding_time)
                        #print("rerout_1sum_ht>>>>>>", env.now , count, env.now, sum_time_up, holding_time)
                    FirstFit(count, DadosSOL[1], DadosSOL[2], DadosSOL[0])
                    ##print("depois da alocacao: ", count , "slots:", sublista[5]  )
                    New_spectro = [DadosSOL[1], DadosSOL[2]]
                    processo = env.process(Desalocate(count,DadosSOL[0],New_spectro,holding_time, env.now))
                    # Tabela de requisições aceitas com n° da req, classe ,num_slots, path, posição no spectro, inicio ,holding_time, frac_ht, hops, distancia_km, bandwidth
                    req_accepts.append([count, class_type, num_slots, DadosSOL[0], New_spectro, env.now , holding_time, 0, len(new_paths[i])-1, distance, bandwidth, processo])
                    ativo[count] = 1
                    Numsaltos +=  len(DadosSOL[0])
                    Qtd_sol_Numsaltos += 1 
                    #total_req_restauradas += 1
                    #restauradasF +=1
                    # Imprima uma mensagem para indicar o sucesso do reroteamento
                    ##print(f"Reroteamento da requisição {count} após a falha.")
                    

                    ConjSlots += 1
                    #print(f"conjuntos de slots {ConjSlots}: Carregados {Transporte}. restantes: {Contbandwidth}")
                    if Contbandwidth == 0:
                        found = True
                        break
                if found:
                    break
            #print(f"Total de conjuntos de slots necessarios: {ConjSlots}")
            total_req_restauradas_pr_pr += 1
            #restauradas_pr.append(count)
            #print("Reroteamento akii>> REROTEOU ")
            #print([topology[u][v]['capacity'] for u, v in topology.edges])
            #input()
        else:
            bloqueio_rerroteamento_pr += 1
            Bloqueio_rerroteamento_cos_pr(class_type)
            Bloqueio_rerroteamento_banda_pr(bandwidth)
            NumReqBlocked +=1
            Vet_NumReqBlocked2x.append(count)
            bloqueio_rerroteamento_pr_pr += 1
            rr_nao_restauradas_pr.append(count)
            nao_restauradas_pr.append(count)
            #print("Reroteamento akii>> BLOCK")
			# Se nenhum novo caminho foi encontrado, a requisição é bloqueada
            ##print("Falha no reroteamento da requisição ", count)
            #contador += 1
            #pass

def Bloqueio_rerroteamento_cos_pr( cos):
	global bloqueio_rerroteamento_cos1_pr
	global bloqueio_rerroteamento_cos2_pr
	global bloqueio_rerroteamento_cos3_pr
	if cos == 1:
		bloqueio_rerroteamento_cos1_pr += 1
	elif cos == 2:
		bloqueio_rerroteamento_cos2_pr += 1
	else:
		bloqueio_rerroteamento_cos3_pr += 1



def Bloqueio_rerroteamento_banda_pr( banda):
	global bloqueio_rerroteamento_100_pr
	global bloqueio_rerroteamento_150_pr
	global bloqueio_rerroteamento_200_pr
	global bloqueio_rerroteamento_250_pr
	global bloqueio_rerroteamento_300_pr
	global bloqueio_rerroteamento_350_pr
	global bloqueio_rerroteamento_400_pr

	if banda == 100:
		bloqueio_rerroteamento_100_pr +=1
	elif banda == 150:
		bloqueio_rerroteamento_150_pr +=1
	elif banda == 200:
		bloqueio_rerroteamento_200_pr +=1
	elif banda == 250:
		bloqueio_rerroteamento_250_pr +=1
	elif banda == 300:
		bloqueio_rerroteamento_300_pr +=1
	elif banda == 350:
		bloqueio_rerroteamento_350_pr +=1
	else:
		bloqueio_rerroteamento_400_pr += 1



def Quem_falhou_link(pontaa, pontab):
	global topology, ativo, req_accepts
	ativo2 = []
	#print("Quem_falhou_link" , ativo)
	for i in range(len(ativo)):
		if i in ativo and ativo[i] == 1:
			ativo2.append(i)
	entradas_filtradas = [
	entrada for entrada in req_accepts
	if entrada[0] in ativo2 and (any(entrada[3][i] == pontaa and entrada[3][i + 1] == pontab for i in range(len(entrada[3]) - 1)) or any(entrada[3][i] == pontab and entrada[3][i + 1] == pontaa for i in range(len(entrada[3]) - 1)))
	]
	#####
	#print("req_accepts" , req_accepts)
	#print("env.now" , env.now, pontaa, pontab)
	#entradas_filtradas = [e for e in req_accepts if ((pontaa, pontab) in zip(e[3], e[3][1:]) or (pontab, pontaa) in zip(e[3], e[3][1:])) and (e[5]+e[6] >= env.now)]
	#print("entradas_filtradas" , entradas_filtradas)
	#input()
	return entradas_filtradas

#desaloca espectro ao finalizar 
def Desalocate(count, path, spectro, holding_time, inicio):
	global topology, sum_time_up, sum_ht, desalocateReq1, desalocateReq2, ativo
	try:
		yield env.timeout(holding_time)
		for i in range(0, (len(path)-1)):
			#print("Antes ===", topology[path[i]][path[i+1]]['capacity'])
			for slot in range(spectro[0],spectro[1]+1):
				topology[path[i]][path[i+1]]['capacity'][slot] = 0
			#print("depois ===",topology[path[i]][path[i+1]]['capacity'])
			#input()
		ativo[count] = 0
		if count not in desalocateReq1:
			sum_time_up += (env.now - inicio)
			desalocateReq1.append(count)
	except simpy.Interrupt as interrupt:
		for i in range(0, (len(path)-1)):
			for slot in range(spectro[0],spectro[1]+1):
				topology[path[i]][path[i+1]]['capacity'][slot] = 0
		if count not in desalocateReq2:
			sum_time_up += (env.now - inicio)
			desalocateReq2.append(count)
			#print("2>>>>>>", env.now , count, inicio, sum_time_up, holding_time)
		ativo[count] = 0
		#input()
		pass


# Calcula a distância do caminho de acordo com os pesos das arestas               
def Distance(path):
	global topology 
	soma = 0
	for i in range(0, (len(path)-1)):
		soma += topology[path[i]][path[i+1]]['weight']
	return (soma)

#Calcula os k-menores caminhos entre pares o-d
def k_shortest_paths(G, source, target, k, weight='weight'):
	return list(islice(nx.shortest_simple_paths(G, source, target, weight=weight), k))

# Calcula o formato de modulação de acordo com a distância do caminho    
def Modulation(dist, demand):
	if dist <= 500:
		return (float(demand) / float(4 * SLOT_SIZE))
	elif 500 < dist <= 1000:
		return (float(demand) / float(3 * SLOT_SIZE))
	elif 1000 < dist <= 2000:
		return (float(demand) / float(2 * SLOT_SIZE)) 
	else:
		return (float(demand) / float(1 * SLOT_SIZE))

#Realiza a alocação de espectro utilizando First-fit
def FirstFit(count,i,j,path):
	global topology
	inicio = i 
	fim =j
	for i in range(0,len(path)-1):
		for slot in range(inicio,fim):
			topology[path[i]][path[i+1]]['capacity'][slot] = count
		topology[path[i]][path[i+1]]['capacity'][fim] = 'GB'

# Verifica se o caminho escolhido possui espectro disponível para a demanda requisitada
def PathIsAble(nslots,path):
	global topology
	cont = 0
	t = 0
	for slot in range (0,len(topology[path[0]][path[1]]['capacity'])):
		if topology[path[0]][path[1]]['capacity'][slot] == 0:
			k = 0
			for ind in range(0,len(path)-1):
				if topology[path[ind]][path[ind+1]]['capacity'][slot] == 0:
					k += 1
			if k == len(path)-1:
				cont += 1
				if cont == 1:
					i = slot
				if cont > nslots:
					j = slot
					return [True,i,j]
				if slot == len(topology[path[0]][path[1]]['capacity'])-1:
						return [False,0,0]
			else:
				cont = 0
				if slot == len(topology[path[0]][path[1]]['capacity'])-1:
					return [False,0,0]
		else:
			cont = 0
			if slot == len(topology[path[0]][path[1]]['capacity'])-1:
				return [False,0,0]
 

 


def CalculaIntervalo(amostra):
	# calcula média e intervalo de confiança de uma amostra (t de Student) 95%. 
	media = np.mean(amostra)
	desvio = np.std(amostra, ddof=1)
	intervalo = (desvio/len(amostra))*1.833
	return [media,intervalo]


def conta_requisicao_banda(banda):
	#[100, 150, 200, 250, 300, 350, 400]
	global NumReq_100
	global NumReq_150
	global NumReq_200
	global NumReq_250
	global NumReq_300
	global NumReq_350
	global NumReq_400
	if banda == 100:
		NumReq_100 +=1
	elif banda == 150:
		NumReq_150 +=1
	elif banda == 200: 
		NumReq_200 +=1
	elif banda == 250: 
		NumReq_250 +=1
	elif banda == 300:
		NumReq_300 += 1 
	elif banda == 350:
		NumReq_350 += 1
	else:
		NumReq_400 += 1

# Computa numero de bloqueio por banda
def conta_bloqueio_requisicao_banda(banda):
	#[100, 150, 200, 250, 300, 350, 400] NumReqBlocked_100
	global NumReqBlocked_100
	global NumReqBlocked_150
	global NumReqBlocked_200
	global NumReqBlocked_250
	global NumReqBlocked_300
	global NumReqBlocked_350
	global NumReqBlocked_400
	if banda == 100:
		NumReqBlocked_100 +=1
	elif banda == 150:
		NumReqBlocked_150 +=1
	elif banda == 200: 
		NumReqBlocked_200 +=1
	elif banda == 250: 
		NumReqBlocked_250 +=1
	elif banda == 300:
		NumReqBlocked_300 += 1 
	elif banda == 350:
		NumReqBlocked_350 += 1
	else:
		NumReqBlocked_400 += 1


# Computa o numero de requisicoes por classe
def conta_requisicao_classe(classe):
	global NumReq_classe1
	global NumReq_classe2
	global NumReq_classe3
	if classe == 1:
		NumReq_classe1 +=1
	elif classe == 2:
		NumReq_classe2 +=1
	else:
		NumReq_classe3 +=1

# Computa numero de requisicoes bloqueadas por classe
def conta_bloqueio_requisicao_classe(classe):
	global NumReqBlocked_classe1
	global NumReqBlocked_classe2
	global NumReqBlocked_classe3
	if classe == 1:
		NumReqBlocked_classe1 +=1
	elif classe == 2:
		NumReqBlocked_classe2 +=1
	else: 
		NumReqBlocked_classe3 +=1


	


topologia = TOPOLOGY
arquivo2  = open('out/'+topologia+'/bloqueio_100'+'.dat', 'w')
arquivo3  = open('out/'+topologia+'/bloqueio_150'+'.dat', 'w')
arquivo4  = open('out/'+topologia+'/bloqueio_200'+'.dat', 'w')
arquivo5  = open('out/'+topologia+'/bloqueio_250'+'.dat', 'w')
arquivo6  = open('out/'+topologia+'/bloqueio_300'+'.dat', 'w')
arquivo7  = open('out/'+topologia+'/bloqueio_350'+'.dat', 'w')
arquivo8  = open('out/'+topologia+'/bloqueio_400'+'.dat', 'w')
arquivo9  = open('out/'+topologia+'/bloqueio_classe1'+'.dat', 'w')
arquivo10  = open('out/'+topologia+'/bloqueio_classe2'+'.dat', 'w')
arquivo11  = open('out/'+topologia+'/bloqueio_classe3'+'.dat', 'w')
arquivo12  = open('out/'+topologia+'/bloqueio_banda'+'.dat', 'w')
arquivo1  = open('out/'+topologia+'/bloqueio'+'.dat', 'w') # bloqueio = nao restauradas
arquivo13  = open('out/'+topologia+'/restorability'+'.dat', 'w')
arquivo14  = open('out/'+topologia+'/availability'+'.dat', 'w')
arquivo15  = open('out/'+topologia+'/afetadas'+'.dat', 'w')
arquivo16  = open('out/'+topologia+'/re_afetadas'+'.dat', 'w')
arquivo17  = open('out/'+topologia+'/saltos'+'.dat', 'w')




for e in range(ERLANG_MIN, ERLANG_MAX+1, ERLANG_INC):

	Bloqueio = []
	interrupcoes_serv = []
	Bloqueio_10 = []
	Bloqueio_20 = []
	Bloqueio_40 = []
	Bloqueio_80 = []
	Bloqueio_160 = []
	Bloqueio_200 = []
	Bloqueio_400 = []
	Bloqueio_classe1 = []
	Bloqueio_classe2 = []
	Bloqueio_classe3 = []
	Bloqueio_banda = []
	Restorability = []
	Availability = []
	afetadas = []
	afetadas2x = []
	saltos = []




	for rep in range(REP):

		solicitacoes_em_andamento = []
		req_accepts = []
		ativo = {}
		k_paths = {}
		LINK_POINTSF = []
		NODE_POINTSF = []
		Simfim = False
		desalocateReq1 = []
		desalocateReq2 = []
		desalocateReqRerr = []
		desalocateReqRerr2 = []
		Vet_NumReqBlocked2x = []

		NumReqBlocked = 0 
		cont_req = 0
		NumReq_100 = 0 
		NumReq_150 = 0 
		NumReq_200 = 0 
		NumReq_250 = 0 
		NumReq_300 = 0 
		NumReq_350 = 0 
		NumReq_400 = 0 
		NumReq_classe1 = 0 
		NumReq_classe2 = 0 
		NumReq_classe3 = 0 
		NumReqBlocked_100 = 0
		NumReqBlocked_150 = 0
		NumReqBlocked_200 = 0
		NumReqBlocked_250 = 0
		NumReqBlocked_300 = 0
		NumReqBlocked_350 = 0
		NumReqBlocked_400 = 0
		NumReqBlocked_classe1 = 0
		NumReqBlocked_classe2 = 0
		NumReqBlocked_classe3 = 0
		#NOVAS
		bloqueio_rerroteamento_pr = 0
		bloqueio_rerroteamento_cos1_pr = 0 
		bloqueio_rerroteamento_cos2_pr = 0
		bloqueio_rerroteamento_cos3_pr = 0
		bloqueio_rerroteamento_100_pr = 0
		bloqueio_rerroteamento_150_pr = 0
		bloqueio_rerroteamento_200_pr = 0
		bloqueio_rerroteamento_250_pr = 0
		bloqueio_rerroteamento_300_pr = 0
		bloqueio_rerroteamento_350_pr = 0
		bloqueio_rerroteamento_400_pr = 0
		restauradasF = 0
		afetadasF = 0 
		sum_time_up = 0
		sum_ht = 0
		NumReqBlocked2x = 0
		Numsaltos = 0
		Qtd_sol_Numsaltos = 0 

		mensagem_impressa = False

		#zera os slots
		for u, v in list(topology.edges):
			topology[u][v]['capacity'] = [0] * SLOTS
			topology[u][v]['failed'] = False
		

		rate = e / HOLDING_TIME
		seed(RANDOM_SEED[rep])


		# Crie o ambiente SimPy
		env = simpy.Environment()

		# Adicione o processo de geração de requisições ao ambiente
		env.process(Simulador(env,rate))

		# Inicie a simulação
		env.run(until=MAX_TIME)



		#report final 
		print("Erlang", e, "Simulacao...", rep)
		print("bloqueadas", NumReqBlocked, "de", NUM_OF_REQUESTS)
		#print(restauradasF, afetadasF)
		##print(sum_time_up / sum_ht )
		#print(desalocateReq1)
		#print(desalocateReq2)
		#print(desalocateReqRerr)
		#input()





		
		Bloqueio_10.append(NumReqBlocked_100/float(NumReq_100))
		Bloqueio_20.append(NumReqBlocked_150/float(NumReq_150))
		Bloqueio_40.append(NumReqBlocked_200/float(NumReq_200))
		Bloqueio_80.append(NumReqBlocked_250/float(NumReq_250))
		Bloqueio_160.append(NumReqBlocked_300/float(NumReq_300))
		Bloqueio_200.append(NumReqBlocked_350/float(NumReq_350))
		Bloqueio_400.append(NumReqBlocked_400/float(NumReq_400))
		Bloqueio_classe1.append(NumReqBlocked_classe1/float(NumReq_classe1))
		Bloqueio_classe2.append(NumReqBlocked_classe2/float(NumReq_classe2))
		Bloqueio_classe3.append(NumReqBlocked_classe3/float(NumReq_classe3))
		BD_solicitada = ((NumReq_100)*100+(NumReq_150)*150+(NumReq_200)*200+(NumReq_250)*250+(NumReq_300)*300+(NumReq_350)*350+(NumReq_400)*400)
		BD_bloqueada = ((NumReqBlocked_100)*100+(NumReqBlocked_150)*150+(NumReqBlocked_200)*200+(NumReqBlocked_250)*250+(NumReqBlocked_300)*300+(NumReqBlocked_350)*350+(NumReqBlocked_400)*400)
		Bloqueio_banda.append(BD_bloqueada/float(BD_solicitada))



		#print(sum_time_up,  sum_ht ) 
		if restauradasF == 0 or afetadasF == 0:
			Restorability.append(0)
		else:
			Restorability.append(restauradasF/afetadasF)
		Availability.append(sum_time_up / sum_ht ) 
		afetadas.append(afetadasF)

		Bloqueio.append(NumReqBlocked / float(NUM_OF_REQUESTS)) 
		afetadas.append(NumReqBlocked)
		saltos.append(Numsaltos/Qtd_sol_Numsaltos)

		contagem = {}
		for numero in Vet_NumReqBlocked2x:
			if numero in contagem:
				contagem[numero] += 1
			else:
				contagem[numero] = 1
		NumReqBlocked2x = sum(contador > 1 for contador in contagem.values())

		afetadas2x.append(NumReqBlocked2x)



	intervalo_10 = CalculaIntervalo(Bloqueio_10)
	intervalo_20 = CalculaIntervalo(Bloqueio_20)
	intervalo_40 = CalculaIntervalo(Bloqueio_40)
	intervalo_80 = CalculaIntervalo(Bloqueio_80)
	intervalo_160 = CalculaIntervalo(Bloqueio_160)
	intervalo_200 = CalculaIntervalo(Bloqueio_200)
	intervalo_400 = CalculaIntervalo(Bloqueio_400)
	intervalo_classe1 = CalculaIntervalo(Bloqueio_classe1)
	intervalo_classe2 = CalculaIntervalo(Bloqueio_classe2)
	intervalo_classe3 = CalculaIntervalo(Bloqueio_classe3)
	intervalo_bloqueio_banda = CalculaIntervalo(Bloqueio_banda)
	intervalo_restorability = CalculaIntervalo(Restorability)
	intervalo_availability = CalculaIntervalo(Availability)
	
	intervalo = CalculaIntervalo(Bloqueio)
	intervalo_afetadas = CalculaIntervalo(afetadas)
	intervalo_afetadas2x = CalculaIntervalo(afetadas2x)
	intervalo_saltos = CalculaIntervalo(saltos)






	arquivo1.write(str(e))
	arquivo1.write("\t")
	arquivo1.write(str(intervalo[0]))
	arquivo1.write("\t")
	arquivo1.write(str(intervalo[0]-intervalo[1]))
	arquivo1.write("\t")
	arquivo1.write(str(intervalo[0]+intervalo[1]))
	arquivo1.write("\n")

	arquivo2.write(str(e))
	arquivo2.write("\t")
	arquivo2.write(str(intervalo_10[0]))
	arquivo2.write("\t")
	arquivo2.write(str(intervalo_10[0]-intervalo_10[1]))
	arquivo2.write("\t")
	arquivo2.write(str(intervalo_10[0]+intervalo_10[1]))
	arquivo2.write("\n")

	arquivo3.write(str(e))
	arquivo3.write("\t")
	arquivo3.write(str(intervalo_20[0]))
	arquivo3.write("\t")
	arquivo3.write(str(intervalo_20[0]-intervalo_20[1]))
	arquivo3.write("\t")
	arquivo3.write(str(intervalo_20[0]+intervalo_20[1]))
	arquivo3.write("\n")

	arquivo4.write(str(e))
	arquivo4.write("\t")
	arquivo4.write(str(intervalo_40[0]))
	arquivo4.write("\t")
	arquivo4.write(str(intervalo_40[0]-intervalo_40[1]))
	arquivo4.write("\t")
	arquivo4.write(str(intervalo_40[0]+intervalo_40[1]))
	arquivo4.write("\n")

	arquivo5.write(str(e))
	arquivo5.write("\t")
	arquivo5.write(str(intervalo_80[0]))
	arquivo5.write("\t")
	arquivo5.write(str(intervalo_80[0]-intervalo_80[1]))
	arquivo5.write("\t")
	arquivo5.write(str(intervalo_80[0]+intervalo_80[1]))
	arquivo5.write("\n")

	arquivo6.write(str(e))
	arquivo6.write("\t")
	arquivo6.write(str(intervalo_160[0]))
	arquivo6.write("\t")
	arquivo6.write(str(intervalo_160[0]-intervalo_160[1]))
	arquivo6.write("\t")
	arquivo6.write(str(intervalo_160[0]+intervalo_160[1]))
	arquivo6.write("\n")

	arquivo7.write(str(e))
	arquivo7.write("\t")
	arquivo7.write(str(intervalo_200[0]))
	arquivo7.write("\t")
	arquivo7.write(str(intervalo_200[0]-intervalo_200[1]))
	arquivo7.write("\t")
	arquivo7.write(str(intervalo_200[0]+intervalo_200[1]))
	arquivo7.write("\n")

	arquivo8.write(str(e))
	arquivo8.write("\t")
	arquivo8.write(str(intervalo_400[0]))
	arquivo8.write("\t")
	arquivo8.write(str(intervalo_400[0]-intervalo_400[1]))
	arquivo8.write("\t")
	arquivo8.write(str(intervalo_400[0]+intervalo_400[1]))
	arquivo8.write("\n")

	arquivo9.write(str(e))
	arquivo9.write("\t")
	arquivo9.write(str(intervalo_classe1[0]))
	arquivo9.write("\t")
	arquivo9.write(str(intervalo_classe1[0]-intervalo_classe1[1]))
	arquivo9.write("\t")
	arquivo9.write(str(intervalo_classe1[0]+intervalo_classe1[1]))
	arquivo9.write("\n")

	arquivo10.write(str(e))
	arquivo10.write("\t")
	arquivo10.write(str(intervalo_classe2[0]))
	arquivo10.write("\t")
	arquivo10.write(str(intervalo_classe2[0]-intervalo_classe2[1]))
	arquivo10.write("\t")
	arquivo10.write(str(intervalo_classe2[0]+intervalo_classe2[1]))
	arquivo10.write("\n")

	arquivo11.write(str(e))
	arquivo11.write("\t")
	arquivo11.write(str(intervalo_classe3[0]))
	arquivo11.write("\t")
	arquivo11.write(str(intervalo_classe3[0]-intervalo_classe3[1]))
	arquivo11.write("\t")
	arquivo11.write(str(intervalo_classe3[0]+intervalo_classe3[1]))
	arquivo11.write("\n")

	arquivo12.write(str(e))
	arquivo12.write("\t")
	arquivo12.write(str(intervalo_bloqueio_banda[0]))
	arquivo12.write("\t")
	arquivo12.write(str(intervalo_bloqueio_banda[0]-intervalo_bloqueio_banda[1]))
	arquivo12.write("\t")
	arquivo12.write(str(intervalo_bloqueio_banda[0]+intervalo_bloqueio_banda[1]))
	arquivo12.write("\n")


	#restorability
	arquivo13.write(str(e))
	arquivo13.write("\t")
	arquivo13.write(str(intervalo_restorability[0]))
	arquivo13.write("\t")
	arquivo13.write(str(intervalo_restorability[0]-intervalo_restorability[1]))
	arquivo13.write("\t")
	arquivo13.write(str(intervalo_restorability[0]+intervalo_restorability[1]))
	arquivo13.write("\n")

	#availability
	arquivo14.write(str(e))
	arquivo14.write("\t")
	arquivo14.write(str(intervalo_availability[0]))
	arquivo14.write("\t")
	arquivo14.write(str(intervalo_availability[0]-intervalo_availability[1]))
	arquivo14.write("\t")
	arquivo14.write(str(intervalo_availability[0]+intervalo_availability[1]))
	arquivo14.write("\n")

	#afetadas
	arquivo15.write(str(e))
	arquivo15.write("\t")
	arquivo15.write(str(intervalo_afetadas[0]))
	arquivo15.write("\t")
	arquivo15.write(str(intervalo_afetadas[0]-intervalo_afetadas[1]))
	arquivo15.write("\t")
	arquivo15.write(str(intervalo_afetadas[0]+intervalo_afetadas[1]))
	arquivo15.write("\n")

	#afetadas
	arquivo16.write(str(e))
	arquivo16.write("\t")
	arquivo16.write(str(intervalo_afetadas2x[0]))
	arquivo16.write("\t")
	arquivo16.write(str(intervalo_afetadas2x[0]-intervalo_afetadas2x[1]))
	arquivo16.write("\t")
	arquivo16.write(str(intervalo_afetadas2x[0]+intervalo_afetadas2x[1]))
	arquivo16.write("\n")

	#saltos
	arquivo17.write(str(e))
	arquivo17.write("\t")
	arquivo17.write(str(intervalo_saltos[0]))
	arquivo17.write("\t")
	arquivo17.write(str(intervalo_saltos[0]-intervalo_saltos[1]))
	arquivo17.write("\t")
	arquivo17.write(str(intervalo_saltos[0]+intervalo_saltos[1]))
	arquivo17.write("\n")


arquivo1.close()
arquivo2.close()
arquivo3.close()
arquivo4.close()
arquivo5.close()
arquivo6.close()
arquivo7.close()
arquivo8.close()
arquivo10.close()
arquivo11.close()
arquivo12.close()
arquivo13.close()
arquivo14.close()
arquivo15.close()
arquivo16.close()
arquivo17.close()

 




 

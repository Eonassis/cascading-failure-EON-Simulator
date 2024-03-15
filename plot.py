#!/usr/bin/env python
# -*- coding: utf-8 -*-



#tramanho das bandas
BANDWIDTH = [100, 150, 200, 250, 300, 350, 400]


######################## Graficos #######################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # Importe o módulo necessário
import matplotlib.cm as cm
import matplotlib.colors as mcolors



#local_DSSP = 'EON_SIM_DSSP\\out\\usa\\'
#local_PRPA_AO = 'EON_SIM_PRPA\\out\\usa\\A0\\'
#local_PRPA_A1 = 'EON_SIM_PRPA\\out\\usa\\A1\\'
#local_PRPA_A2 = 'EON_SIM_PRPA\\out\\usa\\A2\\'
#local_PRPA_A3 = 'EON_SIM_PRPA\\out\\usa\\A3\\'
#local_PRPA_A4 = 'EON_SIM_PRPA\\out\\usa\\A4\\'
#local_PRWR = 'EON_SIM_PRWR\\out\\usa\\'

local_DSSP = 'EON_SIM_DSSP\\out\\usa\\'
local_PRPA_AO = 'EON_SIM_PRPA\\out\\usa\\A0\\'
local_PRPA_A1 = 'EON_SIM_PRPA\\out\\usa\\A0\\'
local_PRPA_A2 = 'EON_SIM_PRPA\\out\\usa\\A0\\'
local_PRPA_A3 = 'EON_SIM_PRPA\\out\\usa\\A0\\'
local_PRPA_A4 = 'EON_SIM_PRPA\\out\\usa\\A0\\'
local_PRWR = 'EON_SIM_PRPA\\out\\usa\\A0\\'

local_path = 'plots\\'
labelss=['DSSP', 'PRPA_AO', 'PRPA_A1', 'PRPA_A2', 'PRPA_A3' , 'PRPA_A4' , 'PRWR']


###################################################################

fig = plt.figure()
fig.add_subplot(121)

data_DSSP = np.loadtxt(local_DSSP + "availability.dat")
data_PRPA_AO = np.loadtxt(local_PRPA_AO + "availability.dat")
data_PRPA_A1 = np.loadtxt(local_PRPA_A1 + "availability.dat")
data_PRPA_A2 = np.loadtxt(local_PRPA_A2 + "availability.dat")
data_PRPA_A3 = np.loadtxt(local_PRPA_A3 + "availability.dat")
data_PRPA_A4 = np.loadtxt(local_PRPA_A4 + "availability.dat")
data_PRWR = np.loadtxt(local_PRWR + "availability.dat")


data_PD_DSSP = pd.DataFrame(data_DSSP, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_AO = pd.DataFrame(data_PRPA_AO, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A1 = pd.DataFrame(data_PRPA_A1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A2 = pd.DataFrame(data_PRPA_A2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A3 = pd.DataFrame(data_PRPA_A3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A4 = pd.DataFrame(data_PRPA_A4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRWR = pd.DataFrame(data_PRWR, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


data_PD_DSSP['Medio'] *= 100
data_PD_PRPA_AO['Medio'] *= 100
data_PD_PRPA_A1['Medio'] *= 100
data_PD_PRPA_A2['Medio'] *= 100
data_PD_PRPA_A3['Medio'] *= 100
data_PD_PRPA_A4['Medio'] *= 100
data_PD_PRWR['Medio'] *= 100

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio'], marker='o', color='r', label=labelss[0])
ax.plot(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio'], marker='X', color='b', label=labelss[1])
ax.plot(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio'], marker='D', color='g', label=labelss[2])
ax.plot(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio'], marker='d', color='c', label=labelss[3])
ax.plot(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio'], marker='>', color='m', label=labelss[4])
ax.plot(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio'], marker='^', color='y', label=labelss[5])
ax.plot(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio'], marker='<', color='k', label=labelss[6])




#texto abaixo das marcacoes
for x, y in zip(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)    
for x, y in zip(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)


ax.set_xticks(data_PD_DSSP['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('Average Availability [%]')
ax.set_title('Availability all')
ax.legend(labels=labelss)

plt.savefig(local_path + 'availability.png', bbox_inches='tight')



###################################################################

fig = plt.figure()
fig.add_subplot(121)

data_DSSP = np.loadtxt(local_DSSP + "restorability.dat")
data_PRPA_AO = np.loadtxt(local_PRPA_AO + "restorability.dat")
data_PRPA_A1 = np.loadtxt(local_PRPA_A1 + "restorability.dat")
data_PRPA_A2 = np.loadtxt(local_PRPA_A2 + "restorability.dat")
data_PRPA_A3 = np.loadtxt(local_PRPA_A3 + "restorability.dat")
data_PRPA_A4 = np.loadtxt(local_PRPA_A4 + "restorability.dat")
data_PRWR = np.loadtxt(local_PRWR + "restorability.dat")


data_PD_DSSP = pd.DataFrame(data_DSSP, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_AO = pd.DataFrame(data_PRPA_AO, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A1 = pd.DataFrame(data_PRPA_A1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A2 = pd.DataFrame(data_PRPA_A2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A3 = pd.DataFrame(data_PRPA_A3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A4 = pd.DataFrame(data_PRPA_A4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRWR = pd.DataFrame(data_PRWR, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


data_PD_DSSP['Medio'] *= 100
data_PD_PRPA_AO['Medio'] *= 100
data_PD_PRPA_A1['Medio'] *= 100
data_PD_PRPA_A2['Medio'] *= 100
data_PD_PRPA_A3['Medio'] *= 100
data_PD_PRPA_A4['Medio'] *= 100
data_PD_PRWR['Medio'] *= 100

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio'], marker='o', color='r', label=labelss[0])
ax.plot(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio'], marker='X', color='b', label=labelss[1])
ax.plot(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio'], marker='D', color='g', label=labelss[2])
ax.plot(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio'], marker='d', color='c', label=labelss[3])
ax.plot(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio'], marker='>', color='m', label=labelss[4])
ax.plot(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio'], marker='^', color='y', label=labelss[5])
ax.plot(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio'], marker='<', color='k', label=labelss[6])




#texto abaixo das marcacoes
for x, y in zip(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)    
for x, y in zip(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)

ax.set_xticks(data_PD_DSSP['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('Average restorability [%]')
ax.set_title('restorability all')
ax.legend(labels=labelss)

plt.savefig(local_path + 'restorability.png', bbox_inches='tight')


###################################################################

fig = plt.figure()
fig.add_subplot(121)

data_DSSP = np.loadtxt(local_DSSP + "bloqueio.dat")
data_PRPA_AO = np.loadtxt(local_PRPA_AO + "bloqueio.dat")
data_PRPA_A1 = np.loadtxt(local_PRPA_A1 + "bloqueio.dat")
data_PRPA_A2 = np.loadtxt(local_PRPA_A2 + "bloqueio.dat")
data_PRPA_A3 = np.loadtxt(local_PRPA_A3 + "bloqueio.dat")
data_PRPA_A4 = np.loadtxt(local_PRPA_A4 + "bloqueio.dat")
data_PRWR = np.loadtxt(local_PRWR + "bloqueio.dat")


data_PD_DSSP = pd.DataFrame(data_DSSP, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_AO = pd.DataFrame(data_PRPA_AO, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A1 = pd.DataFrame(data_PRPA_A1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A2 = pd.DataFrame(data_PRPA_A2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A3 = pd.DataFrame(data_PRPA_A3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A4 = pd.DataFrame(data_PRPA_A4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRWR = pd.DataFrame(data_PRWR, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


data_PD_DSSP['Medio'] *= 100
data_PD_PRPA_AO['Medio'] *= 100
data_PD_PRPA_A1['Medio'] *= 100
data_PD_PRPA_A2['Medio'] *= 100
data_PD_PRPA_A3['Medio'] *= 100
data_PD_PRPA_A4['Medio'] *= 100
data_PD_PRWR['Medio'] *= 100

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio'], marker='o', color='r', label=labelss[0])
ax.plot(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio'], marker='X', color='b', label=labelss[1])
ax.plot(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio'], marker='D', color='g', label=labelss[2])
ax.plot(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio'], marker='d', color='c', label=labelss[3])
ax.plot(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio'], marker='>', color='m', label=labelss[4])
ax.plot(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio'], marker='^', color='y', label=labelss[5])
ax.plot(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio'], marker='<', color='k', label=labelss[6])




#texto abaixo das marcacoes
for x, y in zip(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)    
for x, y in zip(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)


ax.set_xticks(data_PD_DSSP['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('% Nao Restauradas')
ax.set_title('Req. Nao Restauradas')
ax.legend(labels=labelss)

plt.savefig(local_path + 'bloqueio.png', bbox_inches='tight')


###################################################################
fig = plt.figure()
fig.add_subplot(121)

data_DSSP = np.loadtxt(local_DSSP + "afetadas.dat")
data_PRPA_AO = np.loadtxt(local_PRPA_AO + "afetadas.dat")
data_PRPA_A1 = np.loadtxt(local_PRPA_A1 + "afetadas.dat")
data_PRPA_A2 = np.loadtxt(local_PRPA_A2 + "afetadas.dat")
data_PRPA_A3 = np.loadtxt(local_PRPA_A3 + "afetadas.dat")
data_PRPA_A4 = np.loadtxt(local_PRPA_A4 + "afetadas.dat")
data_PRWR = np.loadtxt(local_PRWR + "afetadas.dat")


data_PD_DSSP = pd.DataFrame(data_DSSP, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_AO = pd.DataFrame(data_PRPA_AO, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A1 = pd.DataFrame(data_PRPA_A1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A2 = pd.DataFrame(data_PRPA_A2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A3 = pd.DataFrame(data_PRPA_A3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A4 = pd.DataFrame(data_PRPA_A4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRWR = pd.DataFrame(data_PRWR, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


ax = fig.add_axes([0, 0, 1, 1])

ax.plot(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio'], marker='o', color='r', label=labelss[0])
ax.plot(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio'], marker='X', color='b', label=labelss[1])
ax.plot(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio'], marker='D', color='g', label=labelss[2])
ax.plot(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio'], marker='d', color='c', label=labelss[3])
ax.plot(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio'], marker='>', color='m', label=labelss[4])
ax.plot(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio'], marker='^', color='y', label=labelss[5])
ax.plot(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio'], marker='<', color='k', label=labelss[6])




#texto abaixo das marcacoes
for x, y in zip(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)    
for x, y in zip(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)


ax.set_xticks(data_PD_DSSP['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('QTD. Afetadas')
ax.set_title('Afetadas (QTD. Media de Req. Afetadas bloqueio ou quedas)')
ax.legend(labels=labelss)

plt.savefig(local_path + 'afetadas.png', bbox_inches='tight')


###################################################################

fig = plt.figure()
fig.add_subplot(121)

data_DSSP = np.loadtxt(local_DSSP + "saltos.dat")
data_PRPA_AO = np.loadtxt(local_PRPA_AO + "saltos.dat")
data_PRPA_A1 = np.loadtxt(local_PRPA_A1 + "saltos.dat")
data_PRPA_A2 = np.loadtxt(local_PRPA_A2 + "saltos.dat")
data_PRPA_A3 = np.loadtxt(local_PRPA_A3 + "saltos.dat")
data_PRPA_A4 = np.loadtxt(local_PRPA_A4 + "saltos.dat")
data_PRWR = np.loadtxt(local_PRWR + "saltos.dat")


data_PD_DSSP = pd.DataFrame(data_DSSP, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_AO = pd.DataFrame(data_PRPA_AO, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A1 = pd.DataFrame(data_PRPA_A1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A2 = pd.DataFrame(data_PRPA_A2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A3 = pd.DataFrame(data_PRPA_A3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A4 = pd.DataFrame(data_PRPA_A4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRWR = pd.DataFrame(data_PRWR, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


data_PD_DSSP['Medio'] = data_PD_DSSP['Medio'].round()
data_PD_PRPA_AO['Medio'] = data_PD_PRPA_AO['Medio'].round()
data_PD_PRPA_A1['Medio'] = data_PD_PRPA_A1['Medio'].round()
data_PD_PRPA_A2['Medio'] = data_PD_PRPA_A2['Medio'].round()
data_PD_PRPA_A3['Medio'] = data_PD_PRPA_A3['Medio'].round()
data_PD_PRPA_A4['Medio'] = data_PD_PRPA_A4['Medio'].round()
data_PD_PRWR['Medio'] = data_PD_PRWR['Medio'].round()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio'], marker='o', color='r', label=labelss[0])
ax.plot(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio'], marker='X', color='b', label=labelss[1])
ax.plot(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio'], marker='D', color='g', label=labelss[2])
ax.plot(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio'], marker='d', color='c', label=labelss[3])
ax.plot(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio'], marker='>', color='m', label=labelss[4])
ax.plot(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio'], marker='^', color='y', label=labelss[5])
ax.plot(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio'], marker='<', color='k', label=labelss[6])




#texto abaixo das marcacoes
for x, y in zip(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)    
for x, y in zip(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)


ax.set_xticks(data_PD_DSSP['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('QTD. Saltos')
ax.set_title('QTD. Saltos')
ax.legend(labels=labelss)

plt.savefig(local_path + 'saltos.png', bbox_inches='tight')



######################################################################


fig = plt.figure()
fig.add_subplot(121)

data_DSSP = np.loadtxt(local_DSSP + "re_afetadas.dat")
data_PRPA_AO = np.loadtxt(local_PRPA_AO + "re_afetadas.dat")
data_PRPA_A1 = np.loadtxt(local_PRPA_A1 + "re_afetadas.dat")
data_PRPA_A2 = np.loadtxt(local_PRPA_A2 + "re_afetadas.dat")
data_PRPA_A3 = np.loadtxt(local_PRPA_A3 + "re_afetadas.dat")
data_PRPA_A4 = np.loadtxt(local_PRPA_A4 + "re_afetadas.dat")
data_PRWR = np.loadtxt(local_PRWR + "re_afetadas.dat")


data_PD_DSSP = pd.DataFrame(data_DSSP, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_AO = pd.DataFrame(data_PRPA_AO, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A1 = pd.DataFrame(data_PRPA_A1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A2 = pd.DataFrame(data_PRPA_A2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A3 = pd.DataFrame(data_PRPA_A3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A4 = pd.DataFrame(data_PRPA_A4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRWR = pd.DataFrame(data_PRWR, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


data_PD_DSSP['Medio'] = data_PD_DSSP['Medio'].round()
data_PD_PRPA_AO['Medio'] = data_PD_PRPA_AO['Medio'].round()
data_PD_PRPA_A1['Medio'] = data_PD_PRPA_A1['Medio'].round()
data_PD_PRPA_A2['Medio'] = data_PD_PRPA_A2['Medio'].round()
data_PD_PRPA_A3['Medio'] = data_PD_PRPA_A3['Medio'].round()
data_PD_PRPA_A4['Medio'] = data_PD_PRPA_A4['Medio'].round()
data_PD_PRWR['Medio'] = data_PD_PRWR['Medio'].round()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio'], marker='o', color='r', label=labelss[0])
ax.plot(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio'], marker='X', color='b', label=labelss[1])
ax.plot(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio'], marker='D', color='g', label=labelss[2])
ax.plot(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio'], marker='d', color='c', label=labelss[3])
ax.plot(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio'], marker='>', color='m', label=labelss[4])
ax.plot(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio'], marker='^', color='y', label=labelss[5])
ax.plot(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio'], marker='<', color='k', label=labelss[6])




#texto abaixo das marcacoes
for x, y in zip(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)    
for x, y in zip(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio']):
    ax.text(x, y-0.19, f'{y:.0f}', ha='center', va='bottom', fontsize=8)


ax.set_xticks(data_PD_DSSP['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('QTD. Re-Afetadas')
ax.set_title('QTD. Re-Afetadas')
ax.legend(labels=labelss)

plt.savefig(local_path + 're_afetadas.png', bbox_inches='tight')


#######################################################################################################################

fig = plt.figure()
fig.add_subplot(121)

data_DSSP = np.loadtxt(local_DSSP + "bloqueio_banda.dat")
data_PRPA_AO = np.loadtxt(local_PRPA_AO + "bloqueio_banda.dat")
data_PRPA_A1 = np.loadtxt(local_PRPA_A1 + "bloqueio_banda.dat")
data_PRPA_A2 = np.loadtxt(local_PRPA_A2 + "bloqueio_banda.dat")
data_PRPA_A3 = np.loadtxt(local_PRPA_A3 + "bloqueio_banda.dat")
data_PRPA_A4 = np.loadtxt(local_PRPA_A4 + "bloqueio_banda.dat")
data_PRWR = np.loadtxt(local_PRWR + "bloqueio_banda.dat")


data_PD_DSSP = pd.DataFrame(data_DSSP, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_AO = pd.DataFrame(data_PRPA_AO, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A1 = pd.DataFrame(data_PRPA_A1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A2 = pd.DataFrame(data_PRPA_A2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A3 = pd.DataFrame(data_PRPA_A3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRPA_A4 = pd.DataFrame(data_PRPA_A4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_PD_PRWR = pd.DataFrame(data_PRWR, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


data_PD_DSSP['Medio'] *= 100
data_PD_PRPA_AO['Medio'] *= 100
data_PD_PRPA_A1['Medio'] *= 100
data_PD_PRPA_A2['Medio'] *= 100
data_PD_PRPA_A3['Medio'] *= 100
data_PD_PRPA_A4['Medio'] *= 100
data_PD_PRWR['Medio'] *= 100

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio'], marker='o', color='r', label=labelss[0])
ax.plot(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio'], marker='X', color='b', label=labelss[1])
ax.plot(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio'], marker='D', color='g', label=labelss[2])
ax.plot(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio'], marker='d', color='c', label=labelss[3])
ax.plot(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio'], marker='>', color='m', label=labelss[4])
ax.plot(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio'], marker='^', color='y', label=labelss[5])
ax.plot(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio'], marker='<', color='k', label=labelss[6])




#texto abaixo das marcacoes
for x, y in zip(data_PD_DSSP['Erlangs'], data_PD_DSSP['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_AO['Erlangs'], data_PD_PRPA_AO['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A1['Erlangs'], data_PD_PRPA_A1['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A2['Erlangs'], data_PD_PRPA_A2['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A3['Erlangs'], data_PD_PRPA_A3['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_PD_PRPA_A4['Erlangs'], data_PD_PRPA_A4['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)    
for x, y in zip(data_PD_PRWR['Erlangs'], data_PD_PRWR['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)


ax.set_xticks(data_PD_DSSP['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('% Nao Restauradas')
ax.set_title('Banda Nao Restauradas')
ax.legend(labels=labelss)

plt.savefig(local_path + 'bloqueio_banda.png', bbox_inches='tight')



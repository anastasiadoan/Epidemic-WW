# -*- coding: utf-8 -*-
"""Network Model  (Config, Social Circles, IID Weights).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lW7JOEb9FyyMzoV7fAoOqU1_r5BElPS-
"""

import networkx as nx
import numpy as np
import random

n = 20000
mu = 100
std = 18

degseq = np.round(np.random.normal(loc = mu, scale = std, size = n)).astype(int)

degseq = np.maximum(degseq, 0)

A = []
B = []
C = []
D = []

for i in range(n):
    A.append(round(degseq[i]/30))
    B.append(round(degseq[i]/15))
    C.append(round(degseq[i]*7/30))
    if degseq[i] == round(degseq[i]/30)+round(degseq[i]/15)+round(degseq[i]*7/30)+round(degseq[i]*2/3):
        D.append(round(degseq[i]*2/3))
    elif degseq[i] == round(degseq[i]/30)+round(degseq[i]/15)+round(degseq[i]*7/30)+round(degseq[i]*2/3)-1:
        D.append(round(degseq[i]*2/3)-1)
    elif degseq[i] == round(degseq[i]/30)+round(degseq[i]/15)+round(degseq[i]*7/30)+round(degseq[i]*2/3)+1:
        D.append(round(degseq[i]*2/3)+1)

TA = np.sum(A)
TB = np.sum(B)
TC = np.sum(C)
TD = np.sum(D)

if TA%2 == 1:
    random_node = random.randint(0,n-1)
    A[random_node] += 1
    TA += 1

if TB%2 == 1:
    random_node = random.randint(0,n-1)
    B[random_node] += 1
    TB += 1

if TC%2 == 1:
    random_node = random.randint(0,n-1)
    C[random_node] += 1
    TC += 1

if TD%2 == 1:
    random_node = random.randint(0,n-1)
    D[random_node] += 1
    TD += 1

HEA = []
HEB = []
HEC = []
HED = []

for node, degree in enumerate(A):
    HEA.extend([node] * degree)

for node, degree in enumerate(B):
    HEB.extend([node] * degree)

for node, degree in enumerate(C):
    HEC.extend([node] * degree)

for node, degree in enumerate(D):
    HED.extend([node] * degree)

random.shuffle(HEA)
random.shuffle(HEB)
random.shuffle(HEC)
random.shuffle(HED)

G = nx.Graph()

G.add_nodes_from(range(n))

while HEA:
    u = HEA.pop()
    v = HEA.pop()
    G.add_edge(u, v, Circle="A")

while HEB:
    u = HEB.pop()
    v = HEB.pop()
    G.add_edge(u, v, Circle="B")

while HED:
    u = HED.pop()
    v = HED.pop()
    G.add_edge(u, v, Circle="C")

while HEC:
    u = HEC.pop()
    v = HEC.pop()
    G.add_edge(u, v, Circle="D")
'''
print(nx.get_edge_attributes(G,"Circle"))
'''

for (i, j) in G.edges:
    if G.edges[i, j]['Circle'] == 'A':
        G.edges[i, j]['weight'] = np.maximum(np.random.normal(loc = 0.2, scale = 0.05, size = 1),0.001)
    if G.edges[i, j]['Circle'] == 'B':
        G.edges[i, j]['weight'] = np.maximum(np.random.normal(loc = 0.06, scale = 0.02, size = 1),0.001)
    if G.edges[i, j]['Circle'] == 'C':
        G.edges[i, j]['weight'] = np.maximum(np.random.normal(loc = 0.011, scale = 0.0045, size = 1),0.001)
    if G.edges[i, j]['Circle'] == 'D':
        G.edges[i, j]['weight'] = np.maximum(np.random.normal(loc = 0.001, scale = 0.0005, size = 1),0.001)
'''
print(nx.get_edge_attributes(G,"weight"))
'''

import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

# Initialize the network as provided
n = 150
mu = 15
std = 2

degseq = np.round(np.random.normal(loc=mu, scale=std, size=n)).astype(int)
degseq = np.maximum(degseq, 0)

A, B, C, D = [], [], [], []

for i in range(n):
    A.append(round(degseq[i] / 30))
    B.append(round(degseq[i] / 15))
    C.append(round(degseq[i] * 7 / 30))
    if degseq[i] == round(degseq[i] / 30) + round(degseq[i] / 15) + round(degseq[i] * 7 / 30) + round(degseq[i] * 2 / 3):
        D.append(round(degseq[i] * 2 / 3))
    elif degseq[i] == round(degseq[i] / 30) + round(degseq[i] / 15) + round(degseq[i] * 7 / 30) + round(degseq[i] * 2 / 3) - 1:
        D.append(round(degseq[i] * 2 / 3) - 1)
    elif degseq[i] == round(degseq[i] / 30) + round(degseq[i] / 15) + round(degseq[i] * 7 / 30) + round(degseq[i] * 2 / 3) + 1:
        D.append(round(degseq[i] * 2 / 3) + 1)

TA, TB, TC, TD = np.sum(A), np.sum(B), np.sum(C), np.sum(D)

if TA % 2 == 1:
    A[random.randint(0, n - 1)] += 1
    TA += 1

if TB % 2 == 1:
    B[random.randint(0, n - 1)] += 1
    TB += 1

if TC % 2 == 1:
    C[random.randint(0, n - 1)] += 1
    TC += 1

if TD % 2 == 1:
    D[random.randint(0, n - 1)] += 1
    TD += 1

HEA, HEB, HEC, HED = [], [], [], []

for node, degree in enumerate(A):
    HEA.extend([node] * degree)

for node, degree in enumerate(B):
    HEB.extend([node] * degree)

for node, degree in enumerate(C):
    HEC.extend([node] * degree)

for node, degree in enumerate(D):
    HED.extend([node] * degree)

random.shuffle(HEA)
random.shuffle(HEB)
random.shuffle(HEC)
random.shuffle(HED)

G = nx.Graph()
G.add_nodes_from(range(n))

while HEA:
    u = HEA.pop()
    v = HEA.pop()
    G.add_edge(u, v, Circle="A")

while HEB:
    u = HEB.pop()
    v = HEB.pop()
    G.add_edge(u, v, Circle="B")

while HED:
    u = HED.pop()
    v = HED.pop()
    G.add_edge(u, v, Circle="C")

while HEC:
    u = HEC.pop()
    v = HEC.pop()
    G.add_edge(u, v, Circle="D")

G.remove_edges_from(nx.selfloop_edges(G))

circle_params = {'A': {'mu': 1800, 'std': 300}, 'B': {'mu': 500, 'std': 100}, 'C': {'mu': 420, 'std': 70}, 'D': {'mu': 100, 'std': 25}}

for node in G.nodes:
    G.nodes[node]['weight'] = {}
    for circle, params in circle_params.items():
        w = np.random.normal(params['mu'], params['std'])
        G.nodes[node]['weight'][circle] = w

for u, v, data in G.edges(data=True):
    circle = data['Circle']
    weight = round((G.nodes[u]['weight'][circle] + G.nodes[v]['weight'][circle]) / 2)
    G.edges[u, v]['weight'] = weight

ghost_node = 'G'
G.add_node(ghost_node)

for node in G.nodes:
    if node != ghost_node:
        weight = random.randint(1, 1500)
        G.add_edge(ghost_node, node, weight=weight)

# SIR Model Parameters
beta_A = 0.3  # Infection rate for Circle A
beta_B = 0.2  # Infection rate for Circle B
beta_C = 0.1  # Infection rate for Circle C
beta_D = 0.05 # Infection rate for Circle D
delta = 0.1   # Recovery rate

# Initial States
S = {node: 1 for node in G.nodes}  # All nodes start as susceptible
I = {node: 0 for node in G.nodes}
R = {node: 0 for node in G.nodes}

# Randomly infect a few nodes
initial_infected = random.sample(G.nodes, 5)
for node in initial_infected:
    S[node] = 0
    I[node] = 1

# Simulation
time_steps = 100
S_history = []
I_history = []
R_history = []

for t in range(time_steps):
    new_S = S.copy()
    new_I = I.copy()
    new_R = R.copy()

    for node in G.nodes:
        if S[node] == 1:
            # Susceptible node can get infected
            neighbors = G.neighbors(node)
            infection_prob = 1
            for neighbor in neighbors:
                if I[neighbor] == 1:
                    edge_data = G.get_edge_data(node, neighbor)
                    if 'Circle' in edge_data:  # Check if 'Circle' key exists
                        circle = edge_data['Circle']
                        weight = edge_data['weight']
                        beta = {
                            'A': beta_A,
                            'B': beta_B,
                            'C': beta_C,
                            'D': beta_D
                        }[circle]
                        infection_prob *= (1 - beta * weight / 1000)
            infection_prob = 1 - infection_prob
            if random.random() < infection_prob:
                new_S[node] = 0
                new_I[node] = 1
        elif I[node] == 1:
            # Infected node can recover
            if random.random() < delta:
                new_I[node] = 0
                new_R[node] = 1

    S, I, R = new_S, new_I, new_R
    S_history.append(sum(S.values()))
    I_history.append(sum(I.values()))
    R_history.append(sum(R.values()))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(S_history, label='Susceptible')
plt.plot(I_history, label='Infected')
plt.plot(R_history, label='Recovered')
plt.xlabel('Time Steps')
plt.ylabel('Number of Individuals')
plt.legend()
plt.title('SIR Model Simulation on Weighted Network')
plt.show()

import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

# Initialize the network as provided
n = 150
mu = 15
std = 2

degseq = np.round(np.random.normal(loc=mu, scale=std, size=n)).astype(int)
degseq = np.maximum(degseq, 0)

A, B, C, D = [], [], [], []

for i in range(n):
    A.append(round(degseq[i] / 30))
    B.append(round(degseq[i] / 15))
    C.append(round(degseq[i] * 7 / 30))
    if degseq[i] == round(degseq[i] / 30) + round(degseq[i] / 15) + round(degseq[i] * 7 / 30) + round(degseq[i] * 2 / 3):
        D.append(round(degseq[i] * 2 / 3))
    elif degseq[i] == round(degseq[i] / 30) + round(degseq[i] / 15) + round(degseq[i] * 7 / 30) + round(degseq[i] * 2 / 3) - 1:
        D.append(round(degseq[i] * 2 / 3) - 1)
    elif degseq[i] == round(degseq[i] / 30) + round(degseq[i] / 15) + round(degseq[i] * 7 / 30) + round(degseq[i] * 2 / 3) + 1:
        D.append(round(degseq[i] * 2 / 3) + 1)

TA, TB, TC, TD = np.sum(A), np.sum(B), np.sum(C), np.sum(D)

if TA % 2 == 1:
    A[random.randint(0, n - 1)] += 1
    TA += 1

if TB % 2 == 1:
    B[random.randint(0, n - 1)] += 1
    TB += 1

if TC % 2 == 1:
    C[random.randint(0, n - 1)] += 1
    TC += 1

if TD % 2 == 1:
    D[random.randint(0, n - 1)] += 1
    TD += 1

HEA, HEB, HEC, HED = [], [], [], []

for node, degree in enumerate(A):
    HEA.extend([node] * degree)

for node, degree in enumerate(B):
    HEB.extend([node] * degree)

for node, degree in enumerate(C):
    HEC.extend([node] * degree)

for node, degree in enumerate(D):
    HED.extend([node] * degree)

random.shuffle(HEA)
random.shuffle(HEB)
random.shuffle(HEC)
random.shuffle(HED)

G = nx.Graph()
G.add_nodes_from(range(n))

while HEA:
    u = HEA.pop()
    v = HEA.pop()
    G.add_edge(u, v, Circle="A")

while HEB:
    u = HEB.pop()
    v = HEB.pop()
    G.add_edge(u, v, Circle="B")

while HED:
    u = HED.pop()
    v = HED.pop()
    G.add_edge(u, v, Circle="C")

while HEC:
    u = HEC.pop()
    v = HEC.pop()
    G.add_edge(u, v, Circle="D")

G.remove_edges_from(nx.selfloop_edges(G))

circle_params = {'A': {'mu': 1800, 'std': 300}, 'B': {'mu': 500, 'std': 100}, 'C': {'mu': 420, 'std': 70}, 'D': {'mu': 100, 'std': 25}}

for node in G.nodes:
    G.nodes[node]['weight'] = {}
    for circle, params in circle_params.items():
        w = np.random.normal(params['mu'], params['std'])
        G.nodes[node]['weight'][circle] = w

for u, v, data in G.edges(data=True):
    circle = data['Circle']
    weight = round((G.nodes[u]['weight'][circle] + G.nodes[v]['weight'][circle]) / 2)
    G.edges[u, v]['weight'] = weight

ghost_node = 'G'
G.add_node(ghost_node)

for node in G.nodes:
    if node != ghost_node:
        weight = random.randint(1, 1500)
        G.add_edge(ghost_node, node, weight=weight)

# SIR Model Parameters
beta_A = 0.3  # Infection rate for Circle A
beta_B = 0.2  # Infection rate for Circle B
beta_C = 0.1  # Infection rate for Circle C
beta_D = 0.05 # Infection rate for Circle D
delta = 0.1   # Recovery rate

# Initial States
S = {node: 1 for node in G.nodes}  # All nodes start as susceptible
I = {node: 0 for node in G.nodes}
R = {node: 0 for node in G.nodes}

# Randomly infect a few nodes
initial_infected = random.sample(G.nodes, 5)
for node in initial_infected:
    S[node] = 0
    I[node] = 1

# Monte Carlo Simulation Parameters
num_simulations = 1000
time_steps = 100

S_simulation_results = []
I_simulation_results = []
R_simulation_results = []

for sim in range(num_simulations):
    S = {node: 1 for node in G.nodes}
    I = {node: 0 for node in G.nodes}
    R = {node: 0 for node in G.nodes}

    for node in initial_infected:
        S[node] = 0
        I[node] = 1

    S_history = []
    I_history = []
    R_history = []

    for t in range(time_steps):
        new_S = S.copy()
        new_I = I.copy()
        new_R = R.copy()

        for node in G.nodes:
            if S[node] == 1:
                # Susceptible node can get infected
                neighbors = G.neighbors(node)
                infection_prob = 1
                for neighbor in neighbors:
                    if I[neighbor] == 1:
                        edge_data = G.get_edge_data(node, neighbor)
                        if 'Circle' in edge_data:  # Check if 'Circle' key exists
                            circle = edge_data['Circle']
                            weight = edge_data['weight']
                            beta = {
                                'A': beta_A,
                                'B': beta_B,
                                'C': beta_C,
                                'D': beta_D
                            }[circle]
                            infection_prob *= (1 - beta * weight / 1000)
                infection_prob = 1 - infection_prob
                if random.random() < infection_prob:
                    new_S[node] = 0
                    new_I[node] = 1
            elif I[node] == 1:
                # Infected node can recover
                if random.random() < delta:
                    new_I[node] = 0
                    new_R[node] = 1

        S, I, R = new_S, new_I, new_R
        S_history.append(sum(S.values()))
        I_history.append(sum(I.values()))
        R_history.append(sum(R.values()))

    S_simulation_results.append(S_history)
    I_simulation_results.append(I_history)
    R_simulation_results.append(R_history)

# Calculate mean and standard deviation of results
S_mean = np.mean(S_simulation_results, axis=0)
I_mean = np.mean(I_simulation_results, axis=0)
R_mean = np.mean(R_simulation_results, axis=0)

S_std = np.std(S_simulation_results, axis=0)
I_std = np.std(I_simulation_results, axis=0)
R_std = np.std(R_simulation_results, axis=0)

# Plotting the results with confidence intervals
plt.figure(figsize=(10, 6))
plt.plot(S_mean, label='Susceptible', color='blue')
plt.fill_between(range(time_steps), S_mean - S_std, S_mean + S_std, color='blue', alpha=0.3)
plt.plot(I_mean, label='Infected', color='red')
plt.fill_between(range(time_steps), I_mean - I_std, I_mean + I_std, color='red', alpha=0.3)
plt.plot(R_mean, label='Recovered', color='green')
plt.fill_between(range(time_steps), R_mean - R_std, R_mean + R_std, color='green', alpha=0.3)
plt.xlabel('Time Steps')
plt.ylabel('Number of Individuals')
plt.legend()
plt.title('SIR Model Simulation on Weighted Network with Monte Carlo Simulation')
plt.show()

# Incorporate Martingale Adjustment (simple example)
# Dynamic adjustment of beta based on Martingale properties
def adjust_beta(current_beta, S, I, R):
    total_population = S + I + R
    return current_beta * (total_population / (S + I))

beta_A_adjusted = adjust_beta(beta_A, sum(S.values()), sum(I.values()), sum(R.values()))
beta_B_adjusted = adjust_beta(beta_B, sum(S.values()), sum(I.values()), sum(R.values()))
beta_C_adjusted = adjust_beta(beta_C, sum(S.values()), sum(I.values()), sum(R.values()))
beta_D_adjusted = adjust_beta(beta_D, sum(S.values()), sum(I.values()), sum(R.values()))

print(f"Adjusted betas - A: {beta_A_adjusted}, B: {beta_B_adjusted}, C: {beta_C_adjusted}, D: {beta_D_adjusted}")
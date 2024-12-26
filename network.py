# -*- coding: utf-8 -*-
"""Nobel notebook.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C5oLcKcM-PMuBjGBt9rr9CAkGycFyPzf
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy as sp


n=100
k=15
r=0.2

#Building the network
def watts_strogatz_graph(n, k, r):
    graph = nx.Graph()
    nodes = range(n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            graph.add_edge(node, (node + neighbor) % n)
            graph.add_edge(node, (node - neighbor) % n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            if np.random.rand() < r:
                diff_node = node
                while diff_node == node or graph.has_edge(node, diff_node):
                    diff_node = np.random.choice(nodes)
                graph.remove_edge(node, (node + neighbor) % n)
                graph.add_edge(node, diff_node)
    return graph
Graph= watts_strogatz_graph(n,k,r)
Edge_width=0.2
nx.draw(Graph,with_labels=False, node_color='blue', edge_color='grey',node_size=10,font_size=7,width=Edge_width)
plt.show()

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

#Parameters
n=100
k=15
r=0.2
beta=0.52
gamma=0.41
initial_infected=[random.choice(range(n))]

def watts_strogatz_graph(n, k, r):
    graph = nx.Graph()
    nodes = range(n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            graph.add_edge(node, (node + neighbor) % n)
            graph.add_edge(node, (node - neighbor) % n)

    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            if np.random.rand() < r:
                diff_node = node
                while diff_node == node or graph.has_edge(node, diff_node):
                    diff_node = np.random.choice(nodes)
                graph.remove_edge(node, (node + neighbor) % n)
                graph.add_edge(node, diff_node)

    return graph

def node_color(status):
    if status == 'S':
        return 'blue'
    elif status == 'I':
        return 'red'
    elif status == 'R':
        return 'green'


def draw_graph(graph, statuses):
    pos = nx.spring_layout(graph) #Position nodes using Fruchterman-Reingold force-directed algorithm
    Edge_width=0.2
    for node in graph.nodes():
        node_colors = node_color(statuses[node])
    nx.draw(graph, pos, with_labels=False, node_color=node_colors, edge_color='black', node_size=5,font_size=7,width=Edge_width)
    plt.show()


def SIR_simulation(graph, beta, gamma, initial_infected):
    # Initialize the statuses
    statuses={node:'S' for node in graph.nodes()}
    for node in initial_infected:
        statuses[node] = 'I'



    susceptible_count = [list(statuses.values()).count('S')]
    infected_count = [list(statuses.values()).count('I')]
    recovered_count = [list(statuses.values()).count('R')]

    while 'I' in statuses.values():
        new_statuses = statuses.copy()
        for node in graph.nodes():
            if statuses[node] == 'I':
                # Infect neighbors
                for neighbor in graph.neighbors(node):
                    if statuses[neighbor] == 'S' and np.random.uniform() < beta:
                        new_statuses[neighbor] = 'I'
                # Recover
                if np.random.uniform() < gamma:
                    new_statuses[node] = 'R'

        statuses = new_statuses
        susceptible_count.append(list(statuses.values()).count('S'))
        infected_count.append(list(statuses.values()).count('I'))
        recovered_count.append(list(statuses.values()).count('R'))

    return susceptible_count, infected_count, recovered_count, statuses

#Create the Watts-Strogatz graph
Graph = watts_strogatz_graph(n, k, r)

# Simulate SIR model
susceptible_count, infected_count, recovered_count, final_statuses = SIR_simulation(Graph, beta, gamma,initial_infected)

# Draw the final state of the graph
draw_graph(Graph, final_statuses)

# Plot the results
plt.title('Watts Strogatz SIR simulation')
plt.plot(susceptible_count,label='Susceptible')
plt.plot(infected_count,label='Infected')
plt.plot(recovered_count,label='Recovered')
plt.xlabel('Time').set_color('White')
plt.ylabel('Number of Nodes').set_color('White')
plt.legend()
plt.show()

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

n = 50
k = 6
r = 0.38
beta = 0.52
gamma = 0.13
initial_infected = [random.choice(range(n))]
alpha_dist = 1
beta_dist = 1

def watts_strogatz_graph(n, k, r):
    random_graph = nx.Graph()
    nodes = range(n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            random_graph.add_edge(node, (node + neighbor) % n)
            random_graph.add_edge(node, (node - neighbor) % n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            if np.random.rand() < r:
                diff_node = node
                while diff_node == node or random_graph.has_edge(node, diff_node):
                    diff_node = np.random.choice(nodes)
                random_graph.remove_edge(node, (node + neighbor) % n)
                random_graph.add_edge(node, diff_node)

    weights = {}
    for node in random_graph.nodes():
        neighbors = list(random_graph.neighbors(node))
        if neighbors:
            weights1 = np.random.beta(alpha_dist, beta_dist, size=len(neighbors))
            weights2 = weights1 / np.sum(weights1)
            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                weight = weights2[i]
                if node < neighbor:
                    weights[(node, neighbor)] = weight
                else:
                    weights[(neighbor, node)] = weight
        for (u, v) in random_graph.edges():
            weight = weights.get((u, v))
            if weight is None:
                weight = weights.get((v, u), 0)
            random_graph.edges[u, v]['weight'] = weight

        if not random_graph.edges():
            print("There exists no edge")

    return random_graph

def node_color(status):
    if status == 'S':
        return 'blue'
    elif status == 'I':
        return 'red'
    elif status == 'R':
        return 'green'

def draw_graph(graph, statuses):
    plt.figure(figsize=(15, 15))
    pos = nx.spring_layout(graph)
    node_colors = [node_color(statuses[node]) for node in graph.nodes()]
    labels = {node: statuses[node] for node in graph.nodes()}
    edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in graph.edges(data=True)}
    nx.draw(graph, pos, labels=labels, node_color=node_colors, edge_color='black', node_size=20,font_size=12)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)
    plt.show()

def SIR_simulation(graph, beta, gamma, initial_infected):
    statuses = {node: 'S' for node in graph.nodes()}
    for node in initial_infected:
        statuses[node] = 'I'
    susceptible_counts = [list(statuses.values()).count('S')]
    infected_counts = [list(statuses.values()).count('I')]
    recovered_counts = [list(statuses.values()).count('R')]
    while 'I' in statuses.values():
        new_statuses = statuses.copy()
        for node in graph.nodes():
            if statuses[node] == 'I':
                # Infect neighbors
                for neighbor in graph.neighbors(node):
                    if statuses[neighbor] == 'S':
                        # Infection happens with probability proportional to the weight
                        if np.random.rand() < beta * graph.edges[node, neighbor]['weight']:
                            new_statuses[neighbor] = 'I'
                # Recover
                if np.random.rand() < gamma:
                    new_statuses[node] = 'R'

        statuses = new_statuses
        susceptible_counts.append(list(statuses.values()).count('S'))
        infected_counts.append(list(statuses.values()).count('I'))
        recovered_counts.append(list(statuses.values()).count('R'))

    return susceptible_counts, infected_counts, recovered_counts, statuses

Graph = watts_strogatz_graph(n, k, r)
susceptible_counts, infected_counts, recovered_counts, final_statuses = SIR_simulation(Graph, beta, gamma,initial_infected)
draw_graph(Graph, final_statuses)

plt.plot(susceptible_counts, label='Susceptible')
plt.plot(infected_counts, label='Infected')
plt.plot(recovered_counts, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of Nodes')
plt.legend()
plt.show()

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

n = 100
k = 6
r = 0.24
beta = 0.36
gamma = 0.27
initial_infected = [random.choice(range(n))]

def watts_strogatz_graph(n, k, r):
    graph = nx.Graph()
    nodes = range(n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            graph.add_edge(node, (node + neighbor) % n)
            graph.add_edge(node, (node - neighbor) % n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            if np.random.rand() < r:
                diff_node = node
                while diff_node == node or graph.has_edge(node, diff_node):
                    diff_node = np.random.choice(nodes)
                graph.remove_edge(node, (node + neighbor) % n)
                graph.add_edge(node, diff_node)
    return graph

def node_color(status):
    if status == 'S':
        return 'blue'
    elif status == 'I':
        return 'red'
    elif status == 'R':
        return 'green'

def draw_graph(graph, statuses):
    pos = nx.spring_layout(graph)
    node_colors = [node_color(statuses[node]) for node in graph.nodes()]
    Edge_width=0.15
    for node in graph.nodes():
        labels = {node: statuses[node]}
    nx.draw(graph, pos, with_labels=False, node_color=node_colors, edge_color='black', node_size=17, font_size=7,width=Edge_width)
    plt.show()

def SIR_simulation(graph, beta, gamma, initial_infected):
    statuses = {node: 'S' for node in graph.nodes()}
    for node in initial_infected:
        statuses[node] = 'I'
    susceptible_counts = [list(statuses.values()).count('S')]
    infected_counts = [list(statuses.values()).count('I')]
    recovered_counts = [list(statuses.values()).count('R')]
    while 'I' in statuses.values():
        new_statuses = statuses.copy()
        for node in graph.nodes():
            if statuses[node] == 'I':
                for neighbor in graph.neighbors(node):
                    if statuses[neighbor] == 'S':
                        # Infection
                        if np.random.rand() < beta :
                            new_statuses[neighbor] = 'I'
                # Recovery
                if np.random.rand() < gamma:
                    new_statuses[node] = 'R'

        statuses = new_statuses
        susceptible_counts.append(list(statuses.values()).count('S'))
        infected_counts.append(list(statuses.values()).count('I'))
        recovered_counts.append(list(statuses.values()).count('R'))

    return susceptible_counts, infected_counts, recovered_counts, statuses

Graph = watts_strogatz_graph(n, k, r)
susceptible_counts, infected_counts, recovered_counts, final_statuses = SIR_simulation(Graph, beta, gamma, initial_infected)
draw_graph(Graph, final_statuses)

#Use plt.style.use('default') to remove the black background
plt.plot(susceptible_counts, label='Susceptible')
plt.plot(infected_counts, label='Infected')
plt.plot(recovered_counts, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of Nodes')
plt.legend()
plt.show()

degrees = [Graph.degree(p) for p in Graph.nodes()]
unique_degrees = list(set(degrees))
degree_counts = [degrees.count(q) for q in unique_degrees]

plt.style.use('default')
plt.figure(figsize=(7, 6))
plt.title("Degree Distribution")
plt.bar(unique_degrees, degree_counts, width=0.80, color='purple')
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import random
import sys

# Parameters
n = 400
k = 6
r = 0.38
beta = 0.52
gamma = 0.13
initial_infected = [random.choice(range(n))]

def watts_strogatz_graph(n, k, r):
    graph = nx.Graph()
    nodes = range(n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            graph.add_edge(node, (node + neighbor) % n)
            graph.add_edge(node, (node - neighbor) % n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            if np.random.rand() < r:
                diff_node = node
                while diff_node == node or graph.has_edge(node, diff_node):
                    diff_node = np.random.choice(nodes)
                graph.remove_edge(node, (node + neighbor) % n)
                graph.add_edge(node, diff_node)
    return graph

def node_color(status):
    if status == 'S':
        return 'blue'
    elif status == 'I':
        return 'red'
    elif status == 'R':
        return 'green'


def draw_graph(graph, statuses):
    pos = nx.spring_layout(graph)
    edge_width = 0.2
    for node in graph.nodes():
        node_colors = node_color(statuses[node])
    labels = {node: statuses[node] for node in graph.nodes()}
    nx.draw(graph, pos, with_labels=False, node_color=node_colors, edge_color='black', node_size=17, font_size=7,width=edge_width)
    plt.show()


def SIR_simulation(graph, beta, gamma, initial_infected):
    statuses = {node: 'S' for node in graph.nodes()}
    for node in initial_infected:
        statuses[node] = 'I'
    susceptible_counts = [list(statuses.values()).count('S')]
    infected_counts = [list(statuses.values()).count('I')]
    recovered_counts = [list(statuses.values()).count('R')]
    while 'I' in statuses.values():
        new_statuses = statuses.copy()
        for node in graph.nodes():
            if statuses[node] == 'I':
                for neighbor in graph.neighbors(node):
                    if statuses[neighbor] == 'S':
                        if np.random.rand() < beta:
                            new_statuses[neighbor] = 'I'
                if np.random.rand() < gamma:
                    new_statuses[node] = 'R'

        statuses = new_statuses
        susceptible_counts.append(list(statuses.values()).count('S'))
        infected_counts.append(list(statuses.values()).count('I'))
        recovered_counts.append(list(statuses.values()).count('R'))

    return susceptible_counts, infected_counts, recovered_counts, statuses

Graph = watts_strogatz_graph(n, k, r)

susceptible_counts, infected_counts, recovered_counts, final_statuses = SIR_simulation(Graph, beta, gamma,initial_infected)

draw_graph(Graph, final_statuses)

plt.plot(susceptible_counts, label='Susceptible')
plt.plot(infected_counts, label='Infected')
plt.plot(recovered_counts, label='Recovered')
plt.xlabel('Time').set_color('White')
plt.ylabel('Number of Nodes').set_color('White')
plt.legend()
plt.show()


degree_centrality = nx.degree_centrality(Graph)
betweenness_centrality = nx.betweenness_centrality(Graph)
closeness_centrality = nx.closeness_centrality(Graph)
eigenvector_centrality = nx.eigenvector_centrality(Graph)


centrality_measures = {
    'Degree Centrality': degree_centrality,
    'Betweenness Centrality': betweenness_centrality,
    'Closeness Centrality': closeness_centrality,
    'Eigenvector Centrality': eigenvector_centrality
}
for measure_name, centrality in centrality_measures.items():
    plt.figure(figsize=(15, 12))
    pos = nx.spring_layout(Graph)


    centrality_values = np.array(list(centrality.values()))
    min_centrality, max_centrality = min(centrality_values), max(centrality_values)
    node_sizes = 1000 * (centrality_values - min_centrality) / (max_centrality - min_centrality)

    node_colors = [centrality[node] for node in Graph.nodes()]
    nodes = nx.draw_networkx_nodes(Graph, pos, node_color=node_colors, node_size=node_sizes, cmap=plt.cm.plasma)
    nx.draw_networkx_edges(Graph, pos, edge_color='black', width=0.2)
    nx.draw_networkx_labels(Graph, pos, font_size=8)
    plt.title(f"{measure_name}")
    cbar = plt.colorbar(nodes, ax=plt.gca(), label=measure_name)
    plt.show()

with PdfPages('centrality_measures.pdf') as pdf:
    for measure_name, centrality in centrality_measures.items():
        plt.figure(figsize=(15, 12))
        pos = nx.spring_layout(Graph)

        # Normalize centrality values to get node sizes
        centrality_values = np.array(list(centrality.values()))
        min_centrality, max_centrality = min(centrality_values), max(centrality_values)
        node_sizes = 1000 * (centrality_values - min_centrality) / (max_centrality - min_centrality)

        node_colors = [centrality[node] for node in Graph.nodes()]
        nodes = nx.draw_networkx_nodes(Graph, pos, node_color=node_colors, node_size=node_sizes, cmap=plt.cm.plasma)
        nx.draw_networkx_edges(Graph, pos, edge_color='black', width=0.2)
        nx.draw_networkx_labels(Graph, pos, font_size=8)
        plt.title(f"{measure_name}")
        cbar = plt.colorbar(nodes, ax=plt.gca(), label=measure_name)
        pdf.savefig()
        plt.close()

import networkx as nx
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import seaborn as sns
import random
import sys

n = 100
k = 6
r = 0.16
beta = 0.48
gamma = 0.35
initial_infected = [random.choice(range(n))]

def watts_strogatz_graph(n, k, r):
    graph = nx.Graph()
    nodes = range(n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            graph.add_edge(node, (node + neighbor) % n)
            graph.add_edge(node, (node - neighbor) % n)
    for node in nodes:
        for neighbor in range(1, k // 2 + 1):
            if np.random.rand() < r:
                diff_node = node
                while diff_node == node or graph.has_edge(node, diff_node):
                    diff_node = np.random.choice(nodes)
                graph.remove_edge(node, (node + neighbor) % n)
                graph.add_edge(node, diff_node)
    return graph

def node_color(status):
    if status == 'S':
        return 'blue'
    elif status == 'I':
        return 'red'
    elif status == 'R':
        return 'green'
def draw_graph(graph, statuses):
    pos = nx.spring_layout(graph)
    node_colors = [node_color(statuses[node]) for node in graph.nodes()]
    labels = {node: statuses[node] for node in graph.nodes()}
    nx.draw(graph, pos, labels=labels, node_color=node_colors, edge_color='black', node_size=17,font_size=7)
    plt.show()
def SIR_simulation(graph, beta, gamma, initial_infected):
    statuses = {node: 'S' for node in graph.nodes()}
    for node in initial_infected:
        statuses[node] = 'I'
    susceptible_counts = [list(statuses.values()).count('S')]
    infected_counts = [list(statuses.values()).count('I')]
    recovered_counts = [list(statuses.values()).count('R')]
    while 'I' in statuses.values():
        new_statuses = statuses.copy()
        for node in graph.nodes():
            if statuses[node] == 'I':
                # Infect neighbors
                for neighbor in graph.neighbors(node):
                    if statuses[neighbor] == 'S':
                        # Infection
                        if np.random.rand() < beta:
                            new_statuses[neighbor] = 'I'
                # Recovery
                if np.random.rand() < gamma:
                    new_statuses[node] = 'R'

        statuses = new_statuses
        susceptible_counts.append(list(statuses.values()).count('S'))
        infected_counts.append(list(statuses.values()).count('I'))
        recovered_counts.append(list(statuses.values()).count('R'))

    return susceptible_counts, infected_counts, recovered_counts, statuses

Graph = watts_strogatz_graph(n, k, r)
susceptible_counts, infected_counts, recovered_counts, final_statuses = SIR_simulation(Graph, beta, gamma,initial_infected)
draw_graph(Graph, final_statuses)

plt.plot(susceptible_counts, label='Susceptible')
plt.plot(infected_counts, label='Infected')
plt.plot(recovered_counts, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of Nodes')
plt.legend()
plt.show()

shortest_path_lengths = dict(nx.all_pairs_shortest_path_length(Graph))
# Creating a distance matrix for the shortest path lengths
distance_matrix = np.zeros((n, n))
for source, paths in shortest_path_lengths.items():
    for target, length in paths.items():
        distance_matrix[source, target] = length

#We then plot the shortest path length using heatmap
plt.figure(figsize=(8,6))
sns.heatmap(distance_matrix, cmap='viridis', annot=False, cbar=True)
plt.title("Shortest Path Lengths Heatmap")
plt.xlabel("Target Node")
plt.ylabel("Source Node")
plt.show()
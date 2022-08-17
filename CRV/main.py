from graph import Transaction_Graph
import pandas as pd
import json

# Reads data from csv file
fp = open("CRV/08052022/1hour/crv_trans_data_1hour_080522.csv", 'r')
fulllines = fp.readlines()
lines = []
for line in fulllines:
    lines.append(line.strip())

# # Creates object instance of Transaction_Graph
tg = Transaction_Graph()
digraph = tg.create_graph(lines)
num_nodes, num_edges, num_self, strong_comp, dens, greedy, degree = tg.perform_calculations(
    digraph)

# Calculates number of nodes
# print("Number of nodes in graph: " + str(num_nodes))

# # Calculates number of edges
# print("Number of edges in graph: " + str(num_edges))

# # Calculates the number of self loops
# print("Number of self loops: " + str(num_self))

# # Calculates the number of strongly connected components
# print("Number of strongly connected components: " + str(num_self))

# # Calculates the density of the graph
# print("Density of graph: " + str(dens))

# # Find communities in the graph using greedy modularity maximization
# print("Greedy modularity commmunities" + str(greedy))

# # Calculates the eigenvector centrality
# # print("Eigenvector centrality" + str(eigen))

# # Calculates the degree of each node in the graph
# print("Degree of each node in the graph" + str(degree))

x = {
    "num_node": num_nodes,
    "num_edge": num_edges,
    "num_self_loops": num_self,
    "num_conn_comp": strong_comp,
    "density": dens,
}

y = json.dumps(x)
with open('crv.json', 'w') as f:
    json.dump(y, f, ensure_ascii=False)

# Read data in from csv and seperate data
data = pd.read_csv('CRV/08052022/1hour/crv_trans_data_1hour_080522.csv')
net1 = tg.create_pyvis_graph(data)
net2 = tg.create_pyvis_graph_minus(
    data, [r'\xf403c135812408bfbe8713b5a23a04b3d48aae31', r'\x989aeb4d175e16225e39e87d0d97a3360524ad80', r'\x8301ae4fc9c624d1d396cbdaa1ed877821d7c511', r'\x3fe65692bfcd0e6cf84cb1e7d24108e434a7587e', r'\x0000000000000000000000000000000000000000',
           r'\xcf50b810e57ac33b91dcf525c6ddd9881b139332', r'\x22f9dcf4647084d6c31b2765f6910cd85c178c18', r'\xad84693a21e0a1db73ae6c6e5aceb041a6c8b6b3', r'\x3cf54f3a1969be9916dad548f3c084331c4450b5', r'\x000000000dfde7deaf24138722987c9a6991e2d4',
           r'\xbeefbabeea323f07c59926295205d3b7a17e8638', r'\x7e880867363a7e321f5d260cade2b0bb2f717b02', r'\x9d5c5e364d81dab193b72db9e9be9d8ee669b652', r'\x085a2054c51ea5c91dbf7f90d65e728c0f2a270f', r'\xb900ef131301b307db5efcbed9dbb50a3e209b2e',
           r'\x835f69e58087e5b6bffef182fe2bf959fe253c3c', r'\x0392321e86f42c2f94fbb0c6853052487db521f0', r'\x58dc5a51fe44589beb22e8ce67720b5bc5378009', r'\xf2f400c138f9fb900576263af0bc7fcde2b1b8a8', r'\x28c6c06298d514db089934071355e5743bf21d60',
           r'\x919fa96e88d67499339577fa202345436bcdaf79', r'\x9445bd19767f73dcae6f2de90e6cd31192f62589'
           ])

# Show the graph
# net1.show("crv_trans_data_1hour_080522.html")
# net2.show("crv_trans_data_1hour_minus_dex_080522.html")

# Gets the frequencies of from addresses, to addresses, and both
from_addy, to_addy, all_addy = tg.freq_of_addresses(lines)
# Sorts list of from addresses by frequency (descending)
sorted_from_dict = dict(
    sorted(from_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for from address frequencies
df_from = pd.DataFrame({"From Address": sorted_from_dict.keys(),
                        "Frequency": sorted_from_dict.values()})

# Exports dataframe to excel sheet
df_from.to_excel(r'C:\Users\Student\transaction_graph\from_address_frequencies_1hour_080522.xlsx',
                 index=False, header=True)

# Sorts list of to addresses by frequency (descending)
sorted_to_dict = dict(
    sorted(to_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for to address frequencies
df_to = pd.DataFrame({"To Address": sorted_to_dict.keys(),
                      "Frequency": sorted_to_dict.values()})

# Exports dataframe to excel sheet
df_to.to_excel(r'C:\Users\Student\transaction_graph\to_address_frequencies_1hour_080522.xlsx',
               index=False, header=True)

# Sorts list of from and to addresses by frequency (descending)
sorted_all_dict = dict(
    sorted(all_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for from and to address frequencies
df_all = pd.DataFrame({"Address": sorted_all_dict.keys(),
                      "Frequency": sorted_all_dict.values()})

# Exports dataframe to excel sheet
df_all.to_excel(r'C:\Users\Student\transaction_graph\all_address_frequencies_1hour_080522.xlsx',
                index=False, header=True)

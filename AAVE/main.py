from graph import Transaction_Graph
import pandas as pd

# Reads data from csv file
fp = open("aave_trans_data_1hour_080822.csv", 'r')
fulllines = fp.readlines()
lines = []
for line in fulllines:
    lines.append(line.strip())

# # Creates object instance of Transaction_Graph
tg = Transaction_Graph()
digraph = tg.create_graph(lines)
# num_nodes, num_edges, num_self, strong_comp, dens, greedy, degree = tg.perform_calculations(
#     digraph)

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
# print("Greedy modularity commmunities" + str(greedy))html

# # Calculates the eigenvector centrality
# # print("Eigenvector centrality" + str(eigen))

# # Calculates the degree of each node in the graph
# print("Degree of each node in the graph" + str(degree))

# Read data in from csv and seperate data
data = pd.read_csv('aave_trans_data_1hour_080822.csv')
net1 = tg.create_pyvis_graph(data)
net2 = tg.create_pyvis_graph_minus(
    data, [r'\x5ab53ee1d50eef2c1dd3d5402789cd27bb52c1bb', r'\xc697051d1c6296c24ae3bcef39aca743861d9a81', r'\xdef171fe48cf0115b1d80b88dc8eab59176fee57', r'\x22f9dcf4647084d6c31b2765f6910cd85c178c18', r'\x288931fa76d7b0482f0fd0bca9a50bf0d22b9fef',
           r'\xd75ea151a61d06868e31f8988d28dfe5e9df57b4', r'\x1111111254fb6c44bac0bed2854e76f90643097d', r'\x3e66b66fd1d0b02fda6c811da9e0547970db2f21', r'\x28c6c06298d514db089934071355e5743bf21d60', r'\x9696f59e4d72e237be84ffd425dcad154bf96976',
           r'\xdfd5293d8e347dfe59e90efd55b2956a1343963d', r'\x283af0b28c62c092c9727f1ee09c02ca627eb7f5', r'\x21a31ee1afc51d94c2efccaa2092ad1028285549'
           ])

# Show the graph
net1.show("aave_trans_data_1hour_080822.html")
net2.show("aave_trans_data_1hour_minus_dex_080822.html")

# Gets the frequencies of from addresses, to addresses, and both
from_addy, to_addy, all_addy = tg.freq_of_addresses(lines)
# Sorts list of from addresses by frequency (descending)
sorted_from_dict = dict(
    sorted(from_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for from address frequencies
df_from = pd.DataFrame({"From Address": sorted_from_dict.keys(),
                        "Frequency": sorted_from_dict.values()})

# Exports dataframe to excel sheet
df_from.to_excel(r'C:\Users\Student\transaction_graph\from_address_frequencies_1hour_080822.xlsx',
                 index=False, header=True)

# Sorts list of to addresses by frequency (descending)
sorted_to_dict = dict(
    sorted(to_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for to address frequencies
df_to = pd.DataFrame({"To Address": sorted_to_dict.keys(),
                      "Frequency": sorted_to_dict.values()})

# Exports dataframe to excel sheet
df_to.to_excel(r'C:\Users\Student\transaction_graph\to_address_frequencies_1hour_080822.xlsx',
               index=False, header=True)

# Sorts list of from and to addresses by frequency (descending)
sorted_all_dict = dict(
    sorted(all_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for from and to address frequencies
df_all = pd.DataFrame({"Address": sorted_all_dict.keys(),
                      "Frequency": sorted_all_dict.values()})

# Exports dataframe to excel sheet
df_all.to_excel(r'C:\Users\Student\transaction_graph\all_address_frequencies_1hour_080822.xlsx',
                index=False, header=True)

from graph import Transaction_Graph
import pandas as pd

# Reads data from csv file
fp = open("mc_trans_data_1hour_080822.csv", 'r')
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
# print("Greedy modularity commmunities" + str(greedy))

# # Calculates the eigenvector centrality
# # print("Eigenvector centrality" + str(eigen))

# # Calculates the degree of each node in the graph
# print("Degree of each node in the graph" + str(degree))

# Read data in from csv and seperate data
data = pd.read_csv('mc_trans_data_1hour_080822.csv')
net1 = tg.create_pyvis_graph(data)
net2 = tg.create_pyvis_graph_minus(
    data, [r'\xccb63225a7b19dcf66717e4d40c9a72b39331d61', r'\x98c3d3183c4b8a650614ad179a1a98be0a8d6b8e', r'\x5c76ad4764a4607cd57644faa937a8ca16729e39', r'\xfeea44bc2161f2fe11d55e557ae4ec855e2d1168', r'\x44c01e5e4216f3162538914d9c7f5e6a0d87820e',
           r'\x1111111254fb6c44bac0bed2854e76f90643097d', r'\xe9e12db15d8a0ec338f148ffd9dc9606312a6b28', r'\x68b3465833fb72a70ecdf485e0e4c7bd8665fc45', r'\x28c6c06298d514db089934071355e5743bf21d60', r'\x9696f59e4d72e237be84ffd425dcad154bf96976',
           r'\xdfd5293d8e347dfe59e90efd55b2956a1343963d', r'\x283af0b28c62c092c9727f1ee09c02ca627eb7f5', r'\x21a31ee1afc51d94c2efccaa2092ad1028285549'
           ])

# Show the graph
net1.show("mc_trans_data_1hour_080822.html")
net2.show("mc_trans_data_1hour_minus_dex_080822.html")

# Gets the frequencies of from addresses, to addresses, and both
# from_addy, to_addy, all_addy = tg.freq_of_addresses(lines)
# # Sorts list of from addresses by frequency (descending)
# sorted_from_dict = dict(
#     sorted(from_addy.items(), key=lambda item: item[1], reverse=True))

# # Creates a dataframe for from address frequencies
# df_from = pd.DataFrame({"From Address": sorted_from_dict.keys(),
#                         "Frequency": sorted_from_dict.values()})

# # Exports dataframe to excel sheet
# df_from.to_excel(r'C:\Users\Student\transaction_graph\from_address_frequencies_1hour_080822.xlsx',
#                  index=False, header=True)

# # Sorts list of to addresses by frequency (descending)
# sorted_to_dict = dict(
#     sorted(to_addy.items(), key=lambda item: item[1], reverse=True))

# # Creates a dataframe for to address frequencies
# df_to = pd.DataFrame({"To Address": sorted_to_dict.keys(),
#                       "Frequency": sorted_to_dict.values()})

# # Exports dataframe to excel sheet
# df_to.to_excel(r'C:\Users\Student\transaction_graph\to_address_frequencies_1hour_080822.xlsx',
#                index=False, header=True)

# # Sorts list of from and to addresses by frequency (descending)
# sorted_all_dict = dict(
#     sorted(all_addy.items(), key=lambda item: item[1], reverse=True))

# # Creates a dataframe for from and to address frequencies
# df_all = pd.DataFrame({"Address": sorted_all_dict.keys(),
#                       "Frequency": sorted_all_dict.values()})

# # Exports dataframe to excel sheet
# df_all.to_excel(r'C:\Users\Student\transaction_graph\all_address_frequencies_1hour_080822.xlsx',
#                 index=False, header=True)

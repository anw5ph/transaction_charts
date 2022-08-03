from graph import Transaction_Graph
import pandas as pd

# Reads data from csv file
fp = open("mana_trans_data_1day_080222.csv", 'r')
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
print("Number of nodes in graph: " + str(num_nodes))

# Calculates number of edges
print("Number of edges in graph: " + str(num_edges))

# Calculates the number of self loops
print("Number of self loops: " + str(num_self))

# Calculates the number of strongly connected components
print("Number of strongly connected components: " + str(num_self))

# Calculates the density of the graph
print("Density of graph: " + str(dens))

# Find communities in the graph using greedy modularity maximization
# print("Greedy modularity commmunities" + str(greedy))

# # Calculates the eigenvector centrality
# print("Eigenvector centrality" + str(eigen))

# Calculates the degree of each node in the graph
# print("Degree of each node in the graph" + str(degree))

# Read data in from csv and seperate data
# data = pd.read_csv('mana_trans_data_1day_080222.csv')
# net1 = tg.create_pyvis_graph(data)
# net2 = tg.create_pyvis_graph_minus(
#     data, [r'\x495f8ef80e13e9e1e77d60d2f384bb49694823ef', r'\x28c6c06298d514db089934071355e5743bf21d60', r'\x74de5d4fcbf63e00296fd95d33236b9794016631', r'\x8661ae7918c0115af9e3691662f605e9c550ddc9', r'\x2faf487a4414fe77e2327f0bf4ae2a264a776ad2',
#            r'\x503828976d22510aad0201ac7ec88293211d23da', r'\xb011eeaab8bf0c6de75510128da95498e4b7e67f', r'\x71660c4005ba85c37ccec55d0c4493e66fe775d3', r'\x1bec4db6c3bc499f3dbf289f5499c30d541fec97', r'\x11b1f53204d03e5529f09eb3091939e4fd8c9cf3',
#            r'\x21a31ee1afc51d94c2efccaa2092ad1028285549', r'\xdfd5293d8e347dfe59e90efd55b2956a1343963d', r'\x000000000dfde7deaf24138722987c9a6991e2d4', r'\x6cc5f688a315f3dc28a7781717a9a798a59fda7b', r'\xf16e9b0d03470827a95cdfd0cb8a8a3b46969b91',
#            r'\xe66b31678d6c16e9ebf358268a790b763c133750', r'\x5f65f7b609678448494de4c87521cdf6cef1e932', r'\0x46340b20830761efd32832a74d7169b29feb9758'])

# # Show the graph
# net1.show("mana_trans_data_1day_080222.html")
# net2.show("mana_trans_data_1day_minus_dex_080222.html")

# # Gets the frequencies of from addresses, to addresses, and both
# from_addy, to_addy, all_addy = tg.freq_of_addresses(lines)
# # Sorts list of from addresses by frequency (descending)
# sorted_from_dict = dict(
#     sorted(from_addy.items(), key=lambda item: item[1], reverse=True))

# # Creates a dataframe for from address frequencies
# df_from = pd.DataFrame({"From Address": sorted_from_dict.keys(),
#                         "Frequency": sorted_from_dict.values()})

# # Exports dataframe to excel sheet
# df_from.to_excel(r'C:\Users\Student\transaction_graph\from_address_frequencies_1day_080222.xlsx',
#                  index=False, header=True)

# # Sorts list of to addresses by frequency (descending)
# sorted_to_dict = dict(
#     sorted(to_addy.items(), key=lambda item: item[1], reverse=True))

# # Creates a dataframe for to address frequencies
# df_to = pd.DataFrame({"To Address": sorted_to_dict.keys(),
#                       "Frequency": sorted_to_dict.values()})

# # Exports dataframe to excel sheet
# df_to.to_excel(r'C:\Users\Student\transaction_graph\to_address_frequencies_1day_080222.xlsx',
#                index=False, header=True)

# # Sorts list of from and to addresses by frequency (descending)
# sorted_all_dict = dict(
#     sorted(all_addy.items(), key=lambda item: item[1], reverse=True))

# # Creates a dataframe for from and to address frequencies
# df_all = pd.DataFrame({"Address": sorted_all_dict.keys(),
#                       "Frequency": sorted_all_dict.values()})

# # Exports dataframe to excel sheet
# df_all.to_excel(r'C:\Users\Student\transaction_graph\all_address_frequencies_1day_080222.xlsx',
#                 index=False, header=True)

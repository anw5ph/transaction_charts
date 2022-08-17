from graph import Transaction_Graph
import pandas as pd

# Reads data from csv file
fp = open("chz_trans_data_1hour_080822.csv", 'r')
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
data = pd.read_csv('chz_trans_data_1hour_080822.csv')
net1 = tg.create_pyvis_graph(data)
net2 = tg.create_pyvis_graph_minus(
    data, [r'\x6cc5f688a315f3dc28a7781717a9a798a59fda7b', r'\x28c6c06298d514db089934071355e5743bf21d60', r'\x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88', r'\xb0f4a77bde7fee134265307c5cc19abff0ba409b', r'\x325365ed8275f6a74cac98917b7f6face8da533b',
           r'\xff58711683be66dad6e0e20e0043af46fc7f5f49', r'\x0d0707963952f2fba59dd06f2b425ace40b492fe', r'\x5f65f7b609678448494de4c87521cdf6cef1e932', r'\x56eddb7aa87536c09ccc2793473599fd21a8b17f', r'\x9696f59e4d72e237be84ffd425dcad154bf96976',
           r'\xdfd5293d8e347dfe59e90efd55b2956a1343963d', r'\x21a31ee1afc51d94c2efccaa2092ad1028285549'
           ])

# Show the graph
net1.show("chz_trans_data_1hour_080822.html")
net2.show("chz_trans_data_1hour_minus_dex_080822.html")

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

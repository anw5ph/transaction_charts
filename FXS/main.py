from graph import Transaction_Graph
import pandas as pd

# Reads data from csv file
fp = open("fxs_trans_data_1hour_080422.csv", 'r')
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
data = pd.read_csv('fxs_trans_data_1hour_080422.csv')
net1 = tg.create_pyvis_graph(data)
net2 = tg.create_pyvis_graph_minus(
    data, [r'\x61eb53ee427ab4e007d78a9134aacb3101aadc23', r'\0x278dc748eda1d8efef1adfb518542612b49fcd34', r'\x1104b4df568fa7af90b1bed1d78a2f71e748dc8a', r'\x3cf54f3a1969be9916dad548f3c084331c4450b5', r'\x28120d9d49dbaeb5e34d6b809b842684c482ef27',
           r'\x4f3ad55d7b884cdc48add1e2451a13af17887f26', r'\x59cfcd384746ec3035299d90782be065e466800b', r'\x278dc748eda1d8efef1adfb518542612b49fcd34', r'\x35678017e1d252da1cdd6745b147e3e75d1f9c27', r'\x685b63cfe0179b3efb70a01dcb1d648549aa192d',
           r'\x61eb53ee427ab4e007d78a9134aacb3101a2dc23', r'\xcd8286b48936cdac20518247dbd310ab681a9fbf', r'\xc6764e58b36e26b08fd1d2aed4538c02171fa872', r'\xc8418af6358ffdda74e09ca9cc3fe03ca6adc5b0', r'\xd658a338613198204dca1143ac3f01a722b5d94a',
           r'\xda2c338350a0e59ce71cdced9679a3a590dd9bec'
           ])

# Show the graph
net1.show("fxs_trans_data_1hour_080422.html")
net2.show("fxs_trans_data_1hour_minus_dex_080422.html")

# Gets the frequencies of from addresses, to addresses, and both
# from_addy, to_addy, all_addy = tg.freq_of_addresses(lines)
# # Sorts list of from addresses by frequency (descending)
# sorted_from_dict = dict(
#     sorted(from_addy.items(), key=lambda item: item[1], reverse=True))

# # Creates a dataframe for from address frequencies
# df_from = pd.DataFrame({"From Address": sorted_from_dict.keys(),
#                         "Frequency": sorted_from_dict.values()})

# # Exports dataframe to excel sheet
# df_from.to_excel(r'C:\Users\Student\transaction_graph\from_address_frequencies_1hour_080422.xlsx',
#                  index=False, header=True)

# # Sorts list of to addresses by frequency (descending)
# sorted_to_dict = dict(
#     sorted(to_addy.items(), key=lambda item: item[1], reverse=True))

# # Creates a dataframe for to address frequencies
# df_to = pd.DataFrame({"To Address": sorted_to_dict.keys(),
#                       "Frequency": sorted_to_dict.values()})

# # Exports dataframe to excel sheet
# df_to.to_excel(r'C:\Users\Student\transaction_graph\to_address_frequencies_1hour_080422.xlsx',
#                index=False, header=True)

# # Sorts list of from and to addresses by frequency (descending)
# sorted_all_dict = dict(
#     sorted(all_addy.items(), key=lambda item: item[1], reverse=True))

# # Creates a dataframe for from and to address frequencies
# df_all = pd.DataFrame({"Address": sorted_all_dict.keys(),
#                       "Frequency": sorted_all_dict.values()})

# # Exports dataframe to excel sheet
# df_all.to_excel(r'C:\Users\Student\transaction_graph\all_address_frequencies_1hour_080422.xlsx',
#                 index=False, header=True)

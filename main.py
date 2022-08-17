from graph import Transaction_Graph
import pandas as pd
import json

# Reads data from csv file
fp = open("nouns_trans_data_1week_081522.csv", 'r')
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
# print("Number of strongly connected components: " + str(strong_comp))

# # Calculates the density of the graph
# print("Density of graph: " + str(dens))

x = {
    "num_node": num_nodes,
    "num_edge": num_edges,
    "num_self_loops": num_self,
    "num_conn_comp": strong_comp,
    "density": dens,
}

y = json.dumps(x)
with open('nouns.json', 'w') as f:
    json.dump(y, f, ensure_ascii=False)

# Find communities in the graph using greedy modularity maximization
# print("Greedy modularity commmunities" + str(greedy))

# Calculates the eigenvector centrality
# print("Eigenvector centrality" + str(eigen))

# Calculates the degree of each node in the graph
# print("Degree of each node in the graph" + str(degree))

# Read data in from csv and seperate data
data = pd.read_csv('nouns_trans_data_1week_081522.csv')
net1 = tg.create_pyvis_graph(data)
# net2 = tg.create_pyvis_graph_minus(
#     data, [r'\x4708713b4b6bd32e41bcb2f9c5901d74fedba447', r'\xe66b31678d6c16e9ebf358268a790b763c133750', r'\0x22f9dcf4647084d6c31b2765f6910cd85c178c18'
#            ])

# Show the graph
net1.show("nouns_trans_data_1week_081522.html")
# net2.show("noun_trans_data_1week_minus_dex_081522.html")

# Gets the frequencies of from addresses, to addresses, and both
from_addy, to_addy, all_addy = tg.freq_of_addresses(lines)
# Sorts list of from addresses by frequency (descending)
sorted_from_dict = dict(
    sorted(from_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for from address frequencies
df_from = pd.DataFrame({"From Address": sorted_from_dict.keys(),
                        "Frequency": sorted_from_dict.values()})

# Exports dataframe to excel sheet
df_from.to_excel(r'C:\Users\Student\transaction_graph\from_address_frequencies_1week_081522.xlsx',
                 index=False, header=True)

# Sorts list of to addresses by frequency (descending)
sorted_to_dict = dict(
    sorted(to_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for to address frequencies
df_to = pd.DataFrame({"To Address": sorted_to_dict.keys(),
                      "Frequency": sorted_to_dict.values()})

# Exports dataframe to excel sheet
df_to.to_excel(r'C:\Users\Student\transaction_graph\to_address_frequencies_1week_081522.xlsx',
               index=False, header=True)

# Sorts list of from and to addresses by frequency (descending)
sorted_all_dict = dict(
    sorted(all_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for from and to address frequencies
df_all = pd.DataFrame({"Address": sorted_all_dict.keys(),
                      "Frequency": sorted_all_dict.values()})

# Exports dataframe to excel sheet
df_all.to_excel(r'C:\Users\Student\transaction_graph\all_address_frequencies_1week_081522.xlsx',
                index=False, header=True)

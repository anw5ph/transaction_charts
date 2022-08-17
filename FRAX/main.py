from graph import Transaction_Graph
import pandas as pd
import json

# Reads data from csv file
fp = open("FRAX/08042022/1hour/frax_trans_data_1hour_080422.csv", 'r')
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
with open('frax.json', 'w') as f:
    json.dump(y, f, ensure_ascii=False)

# Read data in from csv and seperate data
data = pd.read_csv('FRAX/08042022/1hour/frax_trans_data_1hour_080422.csv')
net1 = tg.create_pyvis_graph(data)
net2 = tg.create_pyvis_graph_minus(
    data, [r'\x6021444f1706f15465bee85463bcc7d7cc17fc03', r'\x9a834b70c07C81a9fcd6f22e842bf002fbffbe4d', r'\x8300f0528e00ad33b218bb05d396f61a9fdd68cd', r'\x2dce0dda1c2f98e0f171de8333c3c6fe1bbf4877', r'\x97c4adc5d28a86f9470c70dd91dc6cc2f20d2d4d',
           r'\x8300f0528e00ad33b218bb05d396f61a9fdd68cd', r'\xc2a856c3aff2110c1171b8f942256d40e980c726', r'\x92c7b5ce4cb0e5483f3365c1449f21578ee9f21a', r'\x97e7d56a0408570ba1a7852de36350f7713906ec', r'\x8ce5796ef6b0c5918025bcf4f9ca908201b030b3',
           r'\xd632f22692fac7611d2aa1c0d552930d43caed3b'
           ])

# Show the graph
# net1.show("frax_trans_data_1hour_080422.html")
# net2.show("frax_trans_data_1hour_minus_dex_080422.html")

# Gets the frequencies of from addresses, to addresses, and both
from_addy, to_addy, all_addy = tg.freq_of_addresses(lines)
# Sorts list of from addresses by frequency (descending)
sorted_from_dict = dict(
    sorted(from_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for from address frequencies
df_from = pd.DataFrame({"From Address": sorted_from_dict.keys(),
                        "Frequency": sorted_from_dict.values()})

# Exports dataframe to excel sheet
df_from.to_excel(r'C:\Users\Student\transaction_graph\from_address_frequencies_1hour_080422.xlsx',
                 index=False, header=True)

# Sorts list of to addresses by frequency (descending)
sorted_to_dict = dict(
    sorted(to_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for to address frequencies
df_to = pd.DataFrame({"To Address": sorted_to_dict.keys(),
                      "Frequency": sorted_to_dict.values()})

# Exports dataframe to excel sheet
df_to.to_excel(r'C:\Users\Student\transaction_graph\to_address_frequencies_1hour_080422.xlsx',
               index=False, header=True)

# Sorts list of from and to addresses by frequency (descending)
sorted_all_dict = dict(
    sorted(all_addy.items(), key=lambda item: item[1], reverse=True))

# Creates a dataframe for from and to address frequencies
df_all = pd.DataFrame({"Address": sorted_all_dict.keys(),
                      "Frequency": sorted_all_dict.values()})

# Exports dataframe to excel sheet
df_all.to_excel(r'C:\Users\Student\transaction_graph\all_address_frequencies_1hour_080422.xlsx',
                index=False, header=True)

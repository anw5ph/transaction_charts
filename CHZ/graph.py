from cmath import nan
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd
from pyvis.network import Network
from networkx.algorithms.community import greedy_modularity_communities


class Transaction_Graph:
    # Constructor
    def __init__(self):
        self.from_address_freq = {}
        self.to_address_freq = {}
        self.all_address_freq = {}
        return

    def create_pyvis_graph(self, data):
        """
        Creates a graph in PyVis

        This function takes an input of data and uses that data to construct a directed network graph

        Parameters
        ---------
        self
        data: list
            The data points used for the graph construction

        Returns
        -------
        PyVis Network Graph object
            Constructed from the ``data`` inputted.
        """

        # Creates graph object
        net = Network(height='750px', width='100%',
                      notebook=False, directed=True)

        # List of from addresses (0th column)
        fro = data['address_from']

        # List of to addresses (1st column)
        to = data['address_to']

        # List of datatime transaction stamps (2nd column)
        date_time = data['date_time']

        # List of token amounts involved in transaction (3rd column)
        amount = data['amount']

        # Combines data into matrix
        edges_data = zip(fro, to, date_time, amount)

        # Iterate through all elements in the matrix
        for e in edges_data:

            # Node 1, source
            src = e[0]

            # Node 2, target
            tar = e[1]

            # Date time stamp of transaction
            dte = e[2]

            # Amount transferred
            amnt = e[3]

            if src == r'\x6cc5f688a315f3dc28a7781717a9a798a59fda7b':
                net.add_node(
                    src, title="OKEx", group=1)
            elif src == r'\x28c6c06298d514db089934071355e5743bf21d60':
                net.add_node(
                    src, title="Binance 14", group=2)
            elif src == r'\x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88':
                net.add_node(
                    src, title="MEXC: Mexc.com", group=3)
            elif src == r'\xb0f4a77bde7fee134265307c5cc19abff0ba409b':
                net.add_node(
                    src, title="Uniswap V3: CHZ-USDT", group=4)
            elif src == r'\x325365ed8275f6a74cac98917b7f6face8da533b':
                net.add_node(
                    src, title="Uniswap V3: CHZ", group=5)
            elif src == r'\xff58711683be66dad6e0e20e0043af46fc7f5f49':
                net.add_node(
                    src, title="Uniswap V2: CHZ 3", group=6)
            elif src == r'\x0d0707963952f2fba59dd06f2b425ace40b492fe':
                net.add_node(
                    src, title="Gate.io", group=7)
            elif src == r'\x5f65f7b609678448494de4c87521cdf6cef1e932':
                net.add_node(
                    src, title="Gemini 4", group=8)
            elif src == r'\x98c3d3183c4b8a650614ad179a1a98be0a8d6b8e':
                net.add_node(src, title="MEV Bot", group=9)
            elif src == r'\x56eddb7aa87536c09ccc2793473599fd21a8b17f':
                net.add_node(
                    src, title="Binance 17", group=10)
            elif src == r'\x9696f59e4d72e237be84ffd425dcad154bf96976':
                net.add_node(
                    src, title="Binance 18", group=11)
            elif src == r'\xdfd5293d8e347dfe59e90efd55b2956a1343963d':
                net.add_node(
                    src, title="Binance 16", group=12)
            elif src == r'\x21a31ee1afc51d94c2efccaa2092ad1028285549':
                net.add_node(
                    src, title="Binance 15", group=13)
            else:
                net.add_node(src, title=src, group=0)

            if tar == r'\x6cc5f688a315f3dc28a7781717a9a798a59fda7b':
                net.add_node(
                    tar, title="OKEx", group=1)
            elif tar == r'\x28c6c06298d514db089934071355e5743bf21d60':
                net.add_node(
                    tar, title="Binance 14", group=2)
            elif tar == r'\x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88':
                net.add_node(
                    tar, title="MEXC: Mexc.com", group=3)
            elif tar == r'\xb0f4a77bde7fee134265307c5cc19abff0ba409b':
                net.add_node(
                    tar, title="Uniswap V3: CHZ-USDT", group=4)
            elif tar == r'\x325365ed8275f6a74cac98917b7f6face8da533b':
                net.add_node(
                    tar, title="Uniswap V3: CHZ", group=5)
            elif tar == r'\xff58711683be66dad6e0e20e0043af46fc7f5f49':
                net.add_node(
                    tar, title="Uniswap V2: CHZ 3", group=6)
            elif tar == r'\x0d0707963952f2fba59dd06f2b425ace40b492fe':
                net.add_node(
                    tar, title="Gate.io", group=7)
            elif tar == r'\x5f65f7b609678448494de4c87521cdf6cef1e932':
                net.add_node(
                    tar, title="Gemini 4", group=8)
            elif tar == r'\x98c3d3183c4b8a650614ad179a1a98be0a8d6b8e':
                net.add_node(tar, title="MEV Bot", group=9)
            elif tar == r'\x56eddb7aa87536c09ccc2793473599fd21a8b17f':
                net.add_node(
                    tar, title="Binance 17", group=10)
            elif tar == r'\x9696f59e4d72e237be84ffd425dcad154bf96976':
                net.add_node(
                    tar, title="Binance 18", group=11)
            elif tar == r'\xdfd5293d8e347dfe59e90efd55b2956a1343963d':
                net.add_node(
                    tar, title="Binance 16", group=12)
            elif tar == r'\x21a31ee1afc51d94c2efccaa2092ad1028285549':
                net.add_node(
                    tar, title="Binance 15", group=13)
            else:
                # print(tar)
                net.add_node(tar, title=tar, group=0)

            net.add_edge(src, tar, title='Date: ' + str(dte) +
                         '\n Amount: ' + str(amnt) + ' tokens')

        # Get adjacency list for graph
        neighbor_map = net.get_adj_list()

        # Make more frequent nodes, be larger
        for node in net.nodes:
            node["value"] = len(neighbor_map[node["id"]])

        return net

    def create_pyvis_graph_minus(self, data, minus_addresses):
        """
        Creates a graph in PyVis

        This function takes an input of data and a list of addresses to hide from the graph and constructs a graph.

        Parameters
        ---------
        self
        data: list
            The data points used for the graph construction
        minus_addresses: list
            The wallet addresses ignored for the graph construction

        Returns
        -------
        PyVis Network Graph object
            Constructed from the ``data`` and ``minus_addresses`` inputted.
        """
        net = Network(height='750px', width='100%',
                      notebook=False, directed=True)

        fro = data['address_from']
        to = data['address_to']
        date_time = data['date_time']
        amount = data['amount']

        edges_data = zip(fro, to, date_time, amount)

        # Create the graph
        for e in edges_data:
            src = e[0]
            tar = e[1]

            if src not in minus_addresses and tar not in minus_addresses:
                net.add_node(src, title=src, group=0)
                net.add_node(tar, title=tar, group=0)
                net.add_edge(src, tar)

        # Get adjacency list for graph
        neighbor_map = net.get_adj_list()

        # Make nodes that appear more, be larger
        for node in net.nodes:
            node["value"] = len(neighbor_map[node["id"]])

        return net

    def create_graph(self, lines):
        """
        Creates a graph in NetworkX

        This function takes an input of data and uses that data to construct a directed network graph

        Parameters
        ---------
        self
        lines: list
            The data points used for the graph construction

        Returns
        -------
        NetworkX Graph object
            Constructed from the ``lines`` inputted.
        """

        # Remove the headings
        lines.pop(0)

        # Create NetworkX graph object
        DG = nx.DiGraph()

        # Iterate through data received and split at each comma, and seperate those values into their respective fields
        for line in lines:
            DG.add_edge(line.split(',')[0], line.split(',')[
                        1], timestamp=line.split(',')[2], amount=line.split(',')[3])

        return DG

    def freq_of_addresses(self, lines):
        """
        Creates dictionaries

        This function takes an input of data and uses that data to construct dictionaries which monitor the frequency of all wallet addresses in the provided transaction data.

        Parameters
        ---------
        self
        lines: list
            The data points used for the frequency counter construction

        Returns
        -------
        dict
            Three dictionaries that have the frequencies of wallet addresses for just from, just to, and all.
        """

        # Remove header from data
        lines.pop(0)

        # Iterate through data and only keep the first two values as they represent wallet addresses
        for line in lines:
            from_line = line.split(',')[0]
            to_line = line.split(',')[1]

            # Check if address is in the hash table of from addresses
            if from_line not in self.from_address_freq:
                self.from_address_freq[from_line] = 1
            elif from_line in self.from_address_freq:
                self.from_address_freq[from_line] += 1

            # Check if address is in the hash table of to addresses
            if to_line not in self.to_address_freq:
                self.to_address_freq[to_line] = 1
            elif to_line in self.to_address_freq:
                self.to_address_freq[to_line] += 1

            # Check if the from address is in the hash table of all addresses
            if from_line not in self.all_address_freq:
                self.all_address_freq[from_line] = 1
            elif from_line in self.all_address_freq:
                self.all_address_freq[from_line] += 1

            # Check if the to address is in the hash table of all addresses
            if to_line not in self.all_address_freq:
                self.all_address_freq[to_line] = 1
            elif to_line in self.all_address_freq:
                self.all_address_freq[to_line] += 1

        return self.from_address_freq, self.to_address_freq, self.all_address_freq

    def perform_calculations(self, digraph):
        """
        Performs calculations using graph data

        This function takes in a graph object and performs a series of computations on the graph before returning the results of the calculations.

        Parameters
        ---------
        self
        digraph: Graph object
            Used to perform further analysis
        """

        return nx.number_of_nodes(digraph), nx.number_of_edges(digraph), nx.number_of_selfloops(digraph), nx.number_strongly_connected_components(digraph), nx.density(digraph), greedy_modularity_communities(digraph), nx.degree(digraph)

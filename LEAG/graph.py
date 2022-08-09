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

            if src == r'\x0f8039283f1e02bf65d174493ff3d173c7d82e8f':
                net.add_node(
                    src, title="LeagueDAO CommunityVault Contract", group=1)
            elif src == r'\x53986d9ab11e53d491840007b3935d8a94e4b04b':
                net.add_node(
                    src, title="LeagueDAO Rewards Contract", group=2)
            elif src == r'\x4708713b4b6bd32e41bcb2f9c5901d74fedba447':
                net.add_node(
                    src, title="SushiSwap: LEAG-USDC", group=3)
            elif src == r'\x67f60da0f409ab8427e8a408efc4b137d0bd4e7b':
                net.add_node(
                    src, title="LeagueDAO Kernel", group=4)
            elif src == r'\xe66b31678d6c16e9ebf358268a790b763c133750':
                net.add_node(
                    src, title="0x: Coinbase Wallet Proxy", group=5)
            elif src == r'\x3f148612315aae2514ac630d6faf0d94b8cd8e33':
                net.add_node(
                    src, title="LeagueDAO Staking Contract", group=6)
            elif src == r'\0x22f9dcf4647084d6c31b2765f6910cd85c178c18':
                net.add_node(
                    src, title="0x: Exchange Proxy Flash Wallet", group=7)
            elif src == r'\0xcbfc6e810186d9f1cd2f52a1afabcee5ae855a54':
                net.add_node(
                    src, title="LeagueDAO: Vesting Contract", group=8)
            elif src == r'\x981958fcd64058d296608b4604ebc7a0c3662254':
                net.add_node(
                    src, title="LeagueDAO: TransparentUpgradeableProxy Contract", group=9)
            elif src == r'\x1f7683228ee9bc65335374ea5c92b81c74131404':
                net.add_node(
                    src, title="LeagueDAO: Proxy Contract", group=10)
            else:
                net.add_node(src, title=src, group=0)

            if tar == r'\x0f8039283f1e02bf65d174493ff3d173c7d82e8f':
                net.add_node(
                    tar, title="LeagueDAO CommunityVault Contract", group=1)
            elif tar == r'\x53986d9ab11e53d491840007b3935d8a94e4b04b':
                net.add_node(
                    tar, title="LeagueDAO Rewards Contract", group=2)
            elif tar == r'\x4708713b4b6bd32e41bcb2f9c5901d74fedba447':
                net.add_node(
                    tar, title="SushiSwap: LEAG-USDC", group=3)
            elif tar == r'\x67f60da0f409ab8427e8a408efc4b137d0bd4e7b':
                net.add_node(
                    tar, title="LeagueDAO Kernel", group=4)
            elif tar == r'\xe66b31678d6c16e9ebf358268a790b763c133750':
                net.add_node(
                    tar, title="0x: Coinbase Wallet Proxy", group=5)
            elif tar == r'\x3f148612315aae2514ac630d6faf0d94b8cd8e33':
                net.add_node(
                    tar, title="LeagueDAO Staking Contract", group=6)
            elif tar == r'\0x22f9dcf4647084d6c31b2765f6910cd85c178c18':
                net.add_node(
                    tar, title="0x: Exchange Proxy Flash Wallet", group=7)
            elif tar == r'\0xcbfc6e810186d9f1cd2f52a1afabcee5ae855a54':
                net.add_node(
                    tar, title="LeagueDAO: Vesting Contract", group=8)
            elif tar == r'\x981958fcd64058d296608b4604ebc7a0c3662254':
                net.add_node(
                    tar, title="LeagueDAO: TransparentUpgradeableProxy Contract", group=9)
            elif tar == r'\x1f7683228ee9bc65335374ea5c92b81c74131404':
                net.add_node(
                    tar, title="LeagueDAO: Proxy Contract", group=10)
            else:
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

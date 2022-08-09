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
        nft_id = data['id']

        # Combines data into matrix
        edges_data = zip(fro, to, date_time, nft_id)

        # Iterate through all elements in the matrix
        for e in edges_data:

            # Node 1, source
            src = e[0]

            # Node 2, target
            tar = e[1]

            # Date time stamp of transaction
            dte = e[2]

            # Amount transferred
            nft_id = e[3]

            if src == r'\x0bc3807ec262cb779b38d65b38158acc3bfede10':
                net.add_node(
                    src, title="Nouns DAO: Treasury", group=1)
            elif src == r'\x830bd73e4184cef73443c15111a1df14e495c706':
                net.add_node(
                    src, title="Nouns DAO: Nouns Auction House Proxy", group=2)
            elif src == r'\x0000000000000000000000000000000000000000':
                net.add_node(
                    src, title="Nouns DAO Mint Event", group=3)
            elif src == r'\x2573c60a6d127755aa2dc85e342f7da2378a0cc5' or src == r'\x2d7d54476738286552173b5957999664b9fbd467':
                net.add_node(
                    src, title="Gnosis Safe Multisig Proxy Contract", group=4)
            elif src == r'\x83c8f28c26bf6aaca652df1dbbe0e1b56f8baba2':
                net.add_node(
                    src, title="Gem: Gemswap 2 Contract", group=5)
            elif src == r'\xb98efe56decceb1bec9faeeaf62500deb0953474':
                net.add_node(
                    src, title="Nouns DAO: PWNVault Contract", group=6)
            elif src == r'\xf896527c49b44aab3cf22ae356fa3af8e331f280':
                net.add_node(
                    src, title="Nouns DAO: DirectLoanFixedOffer Contract", group=7)
            elif src == r'\x9e3421274fb4053a83917d62bd368332e9e71fe0':
                net.add_node(
                    src, title="Blockchain Capital: Oracle DAO Rewards", group=8)
            elif src == r'\x91dccaa260cc4616e1a6e6b693db7207c5e42937':
                net.add_node(
                    src, title="Eth2 Depositor", group=9)
            elif src == r'\xd5f279ff9eb21c6d40c8f345a66f2751c4eea1fb':
                net.add_node(
                    src, title="NounsDAOExecutor Contract", group=10)
            else:
                net.add_node(src, title=src, group=0)

            if tar == r'\x0bc3807ec262cb779b38d65b38158acc3bfede10':
                net.add_node(
                    tar, title="Nouns DAO: Treasury", group=1)
            elif tar == r'\x830bd73e4184cef73443c15111a1df14e495c706':
                net.add_node(
                    tar, title="Nouns DAO: Nouns Auction House Proxy", group=2)
            elif tar == r'\x0000000000000000000000000000000000000000':
                net.add_node(
                    tar, title="Nouns DAO Mint Event", group=3)
            elif tar == r'\x2573c60a6d127755aa2dc85e342f7da2378a0cc5' or tar == r'\x2d7d54476738286552173b5957999664b9fbd467':
                net.add_node(
                    tar, title="Gnosis Safe Multisig Proxy Contract", group=4)
            elif tar == r'\x83c8f28c26bf6aaca652df1dbbe0e1b56f8baba2':
                net.add_node(
                    tar, title="Gem: Gemswap 2 Contract", group=5)
            elif tar == r'\xb98efe56decceb1bec9faeeaf62500deb0953474':
                net.add_node(
                    tar, title="Nouns DAO: PWNVault Contract", group=6)
            elif tar == r'\xf896527c49b44aab3cf22ae356fa3af8e331f280':
                net.add_node(
                    tar, title="Nouns DAO: DirectLoanFixedOffer Contract", group=7)
            elif tar == r'\x9e3421274fb4053a83917d62bd368332e9e71fe0':
                net.add_node(
                    tar, title="Blockchain Capital: Oracle DAO Rewards", group=8)
            elif tar == r'\x91dccaa260cc4616e1a6e6b693db7207c5e42937':
                net.add_node(
                    tar, title="Eth2 Depositor", group=9)
            elif tar == r'\xd5f279ff9eb21c6d40c8f345a66f2751c4eea1fb':
                net.add_node(
                    tar, title="NounsDAOExecutor Contract", group=10)
            else:
                net.add_node(tar, title=tar, group=0)

            net.add_edge(src, tar, title='Date: ' + str(dte) +
                         '\n NFT DNA ID: ' + str(nft_id))

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
        nft_id = data['id']

        edges_data = zip(fro, to, date_time, nft_id)

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

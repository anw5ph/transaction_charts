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
        edges_data = zip(fro, to, amount, date_time)

        # Iterate through all elements in the matrix
        for e in edges_data:

            # Node 1, source
            src = e[0]

            # Node 2, target
            tar = e[1]

            # Date time stamp of transaction
            amnt = e[2]

            # Amount transferred
            dte = e[3]

            if src == r'\x231a07c825f052b895de5fd1513ce40d18e14af5':
                net.add_node(
                    src, title=src, group=1)
            elif src == r'\x020ca66c30bec2c4fe3861a94e4db4a498a35872':
                net.add_node(
                    src, title=src, group=2)
            elif src == r'\xb1c41c71d36cedea7ddcd5f8d5c5c32ba8f3cbfc':
                net.add_node(
                    src, title=src, group=3)
            elif src == r'\x2f8ab52fc3b40cef63ccc25f96d2dcf6b7a2b735':
                net.add_node(
                    src, title=src, group=4)
            elif src == r'\x177751396d8236569c5c7b04232c7b7281a3b9f3':
                net.add_node(
                    src, title=src, group=5)
            elif src == r'\xf1544ba9a1ad3c8c8b507de3e1f5243c3697e367':
                net.add_node(
                    src, title=src, group=6)
            elif src == r'\xe26d78c6bff297bbc2da3f80fea9a42028a4260f':
                net.add_node(
                    src, title=src, group=7)
            elif src == r'\x9e2003d83e63d09432b5b1d7af22cf7b6c5b84a9':
                net.add_node(
                    src, title=src, group=8)
            elif src == r'\x4754b7e3dede42d71d6c92978f25f306176ec7e9':
                net.add_node(
                    src, title=src, group=9)
            elif src == r'\x7fa020f063b3a06153ed755cee5923039efb86a3':
                net.add_node(
                    src, title=src, group=10)
            elif src == r'\xf476cd75be8fdd197ae0b466a2ec2ae44da41897':
                net.add_node(
                    src, title=src, group=11)
            elif src == r'\x2573c60a6d127755aa2dc85e342f7da2378a0cc5':
                net.add_node(
                    src, title=src, group=12)
            elif src == r'\xf6b6f07862a02c85628b3a9688beae07fea9c863':
                net.add_node(
                    src, title=src, group=13)
            elif src == r'\x6d40c2da94c6522e361904383c37c605f39b8e73':
                net.add_node(
                    src, title=src, group=14)
            elif src == r'\xf55c66079a5c5c2774400dd8b8e82a2d0ae0774e':
                net.add_node(
                    src, title=src, group=15)
            elif src == r'\xae7f458667f1b30746354abc3157907d9f6fd15e':
                net.add_node(
                    src, title=src, group=16)
            elif src == r'\xd5f279ff9eb21c6d40c8f345a66f2751c4eea1fb':
                net.add_node(
                    src, title=src, group=17)
            elif src == r'\xb88f61e6fbda83fbfffabe364112137480398018':
                net.add_node(
                    src, title=src, group=18)
            elif src == r'\x9290745a459a476e5a73f0c49276139a5aef2a84':
                net.add_node(
                    src, title=src, group=19)
            elif src == r'\x008c84421da5527f462886cec43d2717b686a7e4':
                net.add_node(
                    src, title=src, group=20)
            elif src == r'\xba93a6acac634551d49c5aab0f7a0eb2a6bd00a8':
                net.add_node(
                    src, title=src, group=21)
            elif src == r'\xd049b3064990869c9f73bd7896271d83325d2067':
                net.add_node(
                    src, title=src, group=22)
            elif src == r'\xa8b4367f09e63a5234abd14f5ef6868b1aed0e7d':
                net.add_node(
                    src, title=src, group=23)
            elif src == r'\x87757c7fd54d892176e9ecec6767bc16e04a06a8':
                net.add_node(
                    src, title=src, group=24)
            elif src == r'\xf8a065f287d91d77cd626af38ffa220d9b552a2b':
                net.add_node(
                    src, title=src, group=25)
            else:
                net.add_node(src, title=src, group=0)

            if tar == r'\x231a07c825f052b895de5fd1513ce40d18e14af5':
                net.add_node(
                    tar, title=tar, group=1)
            elif tar == r'\x020ca66c30bec2c4fe3861a94e4db4a498a35872':
                net.add_node(
                    tar, title=tar, group=2)
            elif tar == r'\xb1c41c71d36cedea7ddcd5f8d5c5c32ba8f3cbfc':
                net.add_node(
                    tar, title=tar, group=3)
            elif tar == r'\x2f8ab52fc3b40cef63ccc25f96d2dcf6b7a2b735':
                net.add_node(
                    tar, title=tar, group=4)
            elif tar == r'\x177751396d8236569c5c7b04232c7b7281a3b9f3':
                net.add_node(
                    tar, title=tar, group=5)
            elif tar == r'\xf1544ba9a1ad3c8c8b507de3e1f5243c3697e367':
                net.add_node(
                    tar, title=tar, group=6)
            elif tar == r'\xe26d78c6bff297bbc2da3f80fea9a42028a4260f':
                net.add_node(
                    tar, title=tar, group=7)
            elif tar == r'\x9e2003d83e63d09432b5b1d7af22cf7b6c5b84a9':
                net.add_node(
                    tar, title=tar, group=8)
            elif tar == r'\x4754b7e3dede42d71d6c92978f25f306176ec7e9':
                net.add_node(
                    tar, title=tar, group=9)
            elif tar == r'\x7fa020f063b3a06153ed755cee5923039efb86a3':
                net.add_node(
                    tar, title=tar, group=10)
            elif tar == r'\xf476cd75be8fdd197ae0b466a2ec2ae44da41897':
                net.add_node(
                    tar, title=tar, group=11)
            elif tar == r'\x2573c60a6d127755aa2dc85e342f7da2378a0cc5':
                net.add_node(
                    tar, title=tar, group=12)
            elif tar == r'\xf6b6f07862a02c85628b3a9688beae07fea9c863':
                net.add_node(
                    tar, title=tar, group=13)
            elif tar == r'\x6d40c2da94c6522e361904383c37c605f39b8e73':
                net.add_node(
                    tar, title=tar, group=14)
            elif tar == r'\xf55c66079a5c5c2774400dd8b8e82a2d0ae0774e':
                net.add_node(
                    tar, title=tar, group=15)
            elif tar == r'\xae7f458667f1b30746354abc3157907d9f6fd15e':
                net.add_node(
                    tar, title=tar, group=16)
            elif tar == r'\xd5f279ff9eb21c6d40c8f345a66f2751c4eea1fb':
                net.add_node(
                    tar, title=tar, group=17)
            elif tar == r'\xb88f61e6fbda83fbfffabe364112137480398018':
                net.add_node(
                    tar, title=tar, group=18)
            elif tar == r'\x9290745a459a476e5a73f0c49276139a5aef2a84':
                net.add_node(
                    tar, title=tar, group=19)
            elif tar == r'\x008c84421da5527f462886cec43d2717b686a7e4':
                net.add_node(
                    tar, title=tar, group=20)
            elif tar == r'\xba93a6acac634551d49c5aab0f7a0eb2a6bd00a8':
                net.add_node(
                    tar, title=tar, group=21)
            elif tar == r'\xd049b3064990869c9f73bd7896271d83325d2067':
                net.add_node(
                    tar, title=tar, group=22)
            elif tar == r'\xa8b4367f09e63a5234abd14f5ef6868b1aed0e7d':
                net.add_node(
                    tar, title=tar, group=23)
            elif tar == r'\x87757c7fd54d892176e9ecec6767bc16e04a06a8':
                net.add_node(
                    tar, title=tar, group=24)
            elif tar == r'\xf8a065f287d91d77cd626af38ffa220d9b552a2b':
                net.add_node(
                    tar, title=tar, group=25)
            else:
                net.add_node(tar, title=tar, group=0)

            net.add_edge(src, tar, title='Date: ' + str(dte) +
                         '\n Amount: ' + str(amnt))

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

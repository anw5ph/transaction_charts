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

            if src == r'\xf403c135812408bfbe8713b5a23a04b3d48aae31':
                net.add_node(
                    src, title="Convex Finance: Booster", group=1)
            elif src == r'\x989aeb4d175e16225e39e87d0d97a3360524ad80':
                net.add_node(
                    src, title="Convex Finance: Voter Proxy", group=2)
            elif src == r'\x8301ae4fc9c624d1d396cbdaa1ed877821d7c511' or src == r'\x3cf54f3a1969be9916dad548f3c084331c4450b5':
                net.add_node(
                    src, title="Curve Finance Vyper Contract", group=3)
            elif src == r'\x3fe65692bfcd0e6cf84cb1e7d24108e434a7587e':
                net.add_node(
                    src, title="Convex Finance: cvxCRV Rewards", group=4)
            elif src == r'\x0000000000000000000000000000000000000000':
                net.add_node(src, title="Burn/Mint Events", group=5)
            elif src == r'\xcf50b810e57ac33b91dcf525c6ddd9881b139332':
                net.add_node(src, title="Convex Finance: CVX Rewards", group=6)
            elif src == r'\x22f9dcf4647084d6c31b2765f6910cd85c178c18':
                net.add_node(
                    src, title="0x: Exchange Proxy Flash Wallet", group=7)
            elif src == r'\xad84693a21e0a1db73ae6c6e5aceb041a6c8b6b3':
                net.add_node(
                    src, title="Dexible: Settlement", group=8)
            elif src == r'\x000000000dfde7deaf24138722987c9a6991e2d4' or src == r'\xbeefbabeea323f07c59926295205d3b7a17e8638':
                net.add_node(src, title="MEV Bot", group=9)
            elif src == r'\x7e880867363a7e321f5d260cade2b0bb2f717b02' or src == r'\x9d5c5e364d81dab193b72db9e9be9d8ee669b652' or src == r'\x085a2054c51ea5c91dbf7f90d65e728c0f2a270f' or src == r'\xb900ef131301b307db5efcbed9dbb50a3e209b2e' or src == r'\x835f69e58087e5b6bffef182fe2bf959fe253c3c' or src == r'\x0392321e86f42c2f94fbb0c6853052487db521f0':
                net.add_node(
                    src, title="Convex Finance: BaseRewardPool", group=10)
            elif src == r'\x58dc5a51fe44589beb22e8ce67720b5bc5378009':
                net.add_node(src, title="SushiSwap: CRV", group=11)
            elif src == r'\xf2f400c138f9fb900576263af0bc7fcde2b1b8a8':
                net.add_node(
                    src, title="1inch: Aggregation Executor 1", group=12)
            elif src == r'\x28c6c06298d514db089934071355e5743bf21d60':
                net.add_node(src, title="Binance 14", group=13)
            elif src == r'\x919fa96e88d67499339577fa202345436bcdaf79':
                net.add_node(src, title="Uniswap V3: CRV", group=14)
            elif src == r'\x9445bd19767f73dcae6f2de90e6cd31192f62589':
                net.add_node(
                    src, title="Uniswap V3: USDC-CRV", group=15)
            else:
                net.add_node(src, title=src, group=0)

            if tar == r'\xf403c135812408bfbe8713b5a23a04b3d48aae31':
                net.add_node(
                    tar, title="Convex Finance: Booster", group=1)
            elif tar == r'\x989aeb4d175e16225e39e87d0d97a3360524ad80':
                net.add_node(
                    tar, title="Convex Finance: Voter Proxy", group=2)
            elif tar == r'\x8301ae4fc9c624d1d396cbdaa1ed877821d7c511' or tar == r'\x3cf54f3a1969be9916dad548f3c084331c4450b5':
                net.add_node(
                    tar, title="Curve Finance Vyper Contract", group=3)
            elif tar == r'\x3fe65692bfcd0e6cf84cb1e7d24108e434a7587e':
                net.add_node(
                    tar, title="Convex Finance: cvxCRV Rewards", group=4)
            elif tar == r'\x0000000000000000000000000000000000000000':
                net.add_node(tar, title="Burn/Mint Events", group=5)
            elif tar == r'\xcf50b810e57ac33b91dcf525c6ddd9881b139332':
                net.add_node(tar, title="Convex Finance: CVX Rewards", group=6)
            elif tar == r'\x22f9dcf4647084d6c31b2765f6910cd85c178c18':
                net.add_node(
                    tar, title="0x: Exchange Proxy Flash Wallet", group=7)
            elif tar == r'\xad84693a21e0a1db73ae6c6e5aceb041a6c8b6b3':
                net.add_node(
                    tar, title="Dexible: Settlement", group=8)
            elif tar == r'\x000000000dfde7deaf24138722987c9a6991e2d4' or tar == r'\xbeefbabeea323f07c59926295205d3b7a17e8638':
                net.add_node(tar, title="MEV Bot", group=9)
            elif tar == r'\x7e880867363a7e321f5d260cade2b0bb2f717b02' or tar == r'\x9d5c5e364d81dab193b72db9e9be9d8ee669b652' or tar == r'\x085a2054c51ea5c91dbf7f90d65e728c0f2a270f' or tar == r'\xb900ef131301b307db5efcbed9dbb50a3e209b2e' or tar == r'\x835f69e58087e5b6bffef182fe2bf959fe253c3c' or tar == r'\x0392321e86f42c2f94fbb0c6853052487db521f0':
                net.add_node(
                    tar, title="Convex Finance: BaseRewardPool", group=10)
            elif tar == r'\x58dc5a51fe44589beb22e8ce67720b5bc5378009':
                net.add_node(tar, title="SushiSwap: CRV", group=11)
            elif tar == r'\xf2f400c138f9fb900576263af0bc7fcde2b1b8a8':
                net.add_node(
                    tar, title="1inch: Aggregation Executor 1", group=12)
            elif tar == r'\x28c6c06298d514db089934071355e5743bf21d60':
                net.add_node(tar, title="Binance 14", group=13)
            elif tar == r'\x919fa96e88d67499339577fa202345436bcdaf79':
                net.add_node(tar, title="Uniswap V3: CRV", group=14)
            elif tar == r'\x9445bd19767f73dcae6f2de90e6cd31192f62589':
                net.add_node(
                    tar, title="Uniswap V3: USDC-CRV", group=15)
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

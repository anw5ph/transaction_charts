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

            if src == r'\x61eb53ee427ab4e007d78a9134aacb3101aadc23':
                net.add_node(
                    src, title="SushiSwap: FXS", group=1)
            elif src == r'\0x278dc748eda1d8efef1adfb518542612b49fcd34':
                net.add_node(
                    src, title="FraxGaugeFXSRewardsDistributor Contract", group=2)
            elif src == r'\x1104b4df568fa7af90b1bed1d78a2f71e748dc8a' or src == r'\x3cf54f3a1969be9916dad548f3c084331c4450b5':
                net.add_node(
                    src, title="TransparentUpgradeableProxy Contract", group=3)
            elif src == r'\x28120d9d49dbaeb5e34d6b809b842684c482ef27':
                net.add_node(
                    src, title="VirtualBalanceRewardPool Contract", group=4)
            elif src == r'\x4f3ad55d7b884cdc48add1e2451a13af17887f26':
                net.add_node(src, title="ExtraRewardStashV3 Contract", group=5)
            elif src == r'\x59cfcd384746ec3035299d90782be065e466800b':
                net.add_node(src, title="FraxVoterProxy", group=6)
            elif src == r'\x278dc748eda1d8efef1adfb518542612b49fcd34':
                net.add_node(
                    src, title="FraxGaugeFXSRewardsDistributor", group=7)
            elif src == r'\x35678017e1d252da1cdd6745b147e3e75d1f9c27':
                net.add_node(
                    src, title="FraxUnifiedFarm_ERC20_Fraxswap_FRAX_IQ", group=8)
            elif src == r'\x685b63cfe0179b3efb70a01dcb1d648549aa192d':
                net.add_node(src, title="AnyswapV5ERC20", group=9)
            elif src == r'\x61eb53ee427ab4e007d78a9134aacb3101a2dc23':
                net.add_node(src, title="SushiSwap: FXS", group=10)
            elif src == r'\xcd8286b48936cdac20518247dbd310ab681a9fbf':
                net.add_node(src, title="Uniswap V3: FXS 2", group=11)
            elif src == r'\xc6764e58b36e26b08fd1d2aed4538c02171fa872':
                net.add_node(src, title="veFXSYieldDistributorV4", group=12)
            elif src == r'\xc8418af6358ffdda74e09ca9cc3fe03ca6adc5b0':
                net.add_node(src, title="Frax Finance: veFXS", group=13)
            elif src == r'\xd658a338613198204dca1143ac3f01a722b5d94a':
                net.add_node(src, title="Vyper_contract", group=14)
            elif src == r'\xda2c338350a0e59ce71cdced9679a3a590dd9bec':
                net.add_node(
                    src, title="FRAX Finance: Staking FRAX-FXS", group=15)
            else:
                net.add_node(src, title=src, group=0)

            if tar == r'\x61eb53ee427ab4e007d78a9134aacb3101aadc23':
                net.add_node(
                    tar, title="SushiSwap: FXS", group=1)
            elif tar == r'\0x278dc748eda1d8efef1adfb518542612b49fcd34':
                net.add_node(
                    tar, title="FraxGaugeFXSRewardsDistributor Contract", group=2)
            elif tar == r'\x1104b4df568fa7af90b1bed1d78a2f71e748dc8a' or tar == r'\x3cf54f3a1969be9916dad548f3c084331c4450b5':
                net.add_node(
                    tar, title="TransparentUpgradeableProxy Contract", group=3)
            elif tar == r'\x28120d9d49dbaeb5e34d6b809b842684c482ef27':
                net.add_node(
                    tar, title="VirtualBalanceRewardPool Contract", group=4)
            elif tar == r'\x4f3ad55d7b884cdc48add1e2451a13af17887f26':
                net.add_node(tar, title="ExtraRewardStashV3 Contract", group=5)
            elif tar == r'\x59cfcd384746ec3035299d90782be065e466800b':
                net.add_node(tar, title="FraxVoterProxy", group=6)
            elif tar == r'\x278dc748eda1d8efef1adfb518542612b49fcd34':
                net.add_node(
                    tar, title="FraxGaugeFXSRewardsDistributor", group=7)
            elif tar == r'\x35678017e1d252da1cdd6745b147e3e75d1f9c27':
                net.add_node(
                    tar, title="FraxUnifiedFarm_ERC20_Fraxswap_FRAX_IQ", group=8)
            elif tar == r'\x685b63cfe0179b3efb70a01dcb1d648549aa192d':
                net.add_node(tar, title="AnyswapV5ERC20", group=9)
            elif tar == r'\x61eb53ee427ab4e007d78a9134aacb3101a2dc23':
                net.add_node(tar, title="SushiSwap: FXS", group=10)
            elif tar == r'\xcd8286b48936cdac20518247dbd310ab681a9fbf':
                net.add_node(tar, title="Uniswap V3: FXS 2", group=11)
            elif tar == r'\xc6764e58b36e26b08fd1d2aed4538c02171fa872':
                net.add_node(tar, title="veFXSYieldDistributorV4", group=12)
            elif tar == r'\xc8418af6358ffdda74e09ca9cc3fe03ca6adc5b0':
                net.add_node(tar, title="Frax Finance: veFXS", group=13)
            elif tar == r'\xd658a338613198204dca1143ac3f01a722b5d94a':
                net.add_node(tar, title="Vyper_contract", group=14)
            elif tar == r'\xda2c338350a0e59ce71cdced9679a3a590dd9bec':
                net.add_node(
                    tar, title="FRAX Finance: Staking FRAX-FXS", group=15)
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

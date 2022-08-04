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

            if src == r'\x6021444f1706f15465bee85463bcc7d7cc17fc03':
                net.add_node(
                    src, title="Temple Uniswap V2 Pair Contract", group=1)
            elif src == r'\x9a834b70c07C81a9fcd6f22e842bf002fbffbe4d':
                net.add_node(
                    src, title="Uniswap V3: FRAX-USDC 3 Contract", group=2)
            elif src == r'\x8300f0528e00ad33b218bb05d396f61a9fdd68cd':
                net.add_node(src, title="FraxswapPair", group=3)
            elif src == r'\x2dce0dda1c2f98e0f171de8333c3c6fe1bbf4877':
                net.add_node(src, title="Uniswap V2: OHM-FRAX", group=4)
            elif src == r'\x97c4adc5d28a86f9470c70dd91dc6cc2f20d2d4d':
                net.add_node(src, title="Uniswap V2: FRAX-USDC 2", group=5)
            elif src == r'\x8300f0528e00ad33b218bb05d396f61a9fdd68cd':
                net.add_node(src, title="FraxswapPair Contract", group=6)
            elif src == r'\xc2a856c3aff2110c1171b8f942256d40e980c726':
                net.add_node(src, title="Uniswap V3: FRAX-USDT", group=7)
            elif src == r'\x92c7b5ce4cb0e5483f3365c1449f21578ee9f21a':
                net.add_node(src, title="Uniswap V3: FRAX", group=8)
            elif src == r'\x97e7d56a0408570ba1a7852de36350f7713906ec':
                net.add_node(src, title="Uniswap V3: DAI-FRAX", group=9)
            elif src == r'\x8ce5796ef6b0c5918025bcf4f9ca908201b030b3':
                net.add_node(src, title="Uniswap V3: agEUR-FRAX", group=10)
            elif src == r'\xd632f22692fac7611d2aa1c0d552930d43caed3b':
                net.add_node(
                    src, title="Frax FinanceL FRAX3CRV-f Token", group=11)
            else:
                net.add_node(src, title=src, group=0)

            if tar == r'\x6021444f1706f15465bee85463bcc7d7cc17fc03':
                net.add_node(
                    tar, title="Temple Uniswap V2 Pair Contract", group=1)
            elif tar == r'\x9a834b70c07C81a9fcd6f22e842bf002fbffbe4d':
                net.add_node(
                    tar, title="Uniswap V3: FRAX-USDC 3 Contract", group=2)
            elif tar == r'\x8300f0528e00ad33b218bb05d396f61a9fdd68cd':
                net.add_node(tar, title="FraxswapPair", group=3)
            elif tar == r'\x2dce0dda1c2f98e0f171de8333c3c6fe1bbf4877':
                net.add_node(tar, title="Uniswap V2: OHM-FRAX", group=4)
            elif tar == r'\x97c4adc5d28a86f9470c70dd91dc6cc2f20d2d4d':
                net.add_node(tar, title="Uniswap V2: FRAX-USDC 2", group=5)
            elif tar == r'\x8300f0528e00ad33b218bb05d396f61a9fdd68cd':
                net.add_node(tar, title="FraxswapPair Contract", group=6)
            elif tar == r'\xc2a856c3aff2110c1171b8f942256d40e980c726':
                net.add_node(tar, title="Uniswap V3: FRAX-USDT", group=7)
            elif tar == r'\x92c7b5ce4cb0e5483f3365c1449f21578ee9f21a':
                net.add_node(tar, title="Uniswap V3: FRAX", group=8)
            elif tar == r'\x97e7d56a0408570ba1a7852de36350f7713906ec':
                net.add_node(tar, title="Uniswap V3: DAI-FRAX", group=9)
            elif tar == r'\x8ce5796ef6b0c5918025bcf4f9ca908201b030b3':
                net.add_node(tar, title="Uniswap V3: agEUR-FRAX", group=10)
            elif tar == r'\xd632f22692fac7611d2aa1c0d552930d43caed3b':
                net.add_node(
                    tar, title="Frax FinanceL FRAX3CRV-f Token", group=11)
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

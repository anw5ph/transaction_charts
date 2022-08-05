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

            if src == r'\xdac17f958d2ee523a2206206994597c13d831ec7':
                net.add_node(
                    src, title="Tether: USDT Stablecoin", group=1)
            elif src == r'\xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48':
                net.add_node(
                    src, title="Centre: USD Coin", group=2)
            elif src == r'\x00000000006c3852cbef3e08e8df289169ede581':
                net.add_node(
                    src, title="OpenSea: Seaport 1.1", group=3)
            elif src == r'\x46340b20830761efd32832a74d7169b29feb9758':
                net.add_node(
                    src, title="Crypto.com 2", group=4)
            elif src == r'\xdb7b094fdc04f51560a03a99f747044951b73727':
                net.add_node(src, title="Moonbirds2 Contract", group=5)
            elif src == r'\x0d8f1817c644101a915852841a3b5933b0b8dcc7':
                net.add_node(src, title="The Last Azaraks Contract", group=6)
            elif src == r'\x74312363e45dcaba76c59ec49a7aa8a65a67eed3':
                net.add_node(
                    src, title="X2Y2: Exchange", group=7)
            elif src == r'\x68b3465833fb72a70ecdf485e0e4c7bd8665fc45':
                net.add_node(
                    src, title="Uniswap V3: Router 2", group=8)
            elif src == r'\x28c6c06298d514db089934071355e5743bf21d60':
                net.add_node(src, title="Binance 14", group=9)
            elif src == r'\xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2':
                net.add_node(
                    src, title="Wrapped Ether", group=10)
            elif src == r'\x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88':
                net.add_node(src, title="MEXC: Mexc.com", group=11)
            elif src == r'\x9ec9d9fd1aa941ed171e7a3951d68e96137ed21e':
                net.add_node(
                    src, title="FlowerPower Contract", group=12)
            elif src == r'\x3cd751e6b0078be393132286c442345e5dc49699':
                net.add_node(src, title="Coinbase 4", group=13)
            elif src == r'\x267be1c1d684f78cb4f6a176c4911b741e4ffdc0':
                net.add_node(src, title="Kraken 4", group=14)
            elif src == r'\x7a250d5630b4cf539739df2c5dacb4c659f2488d':
                net.add_node(
                    src, title="Uniswap V2: Router 2", group=15)
            elif src == r'\xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511':
                net.add_node(
                    src, title="Coinbase 5", group=16)
            elif src == r'\x2faf487a4414fe77e2327f0bf4ae2a264a776ad2':
                net.add_node(
                    src, title="FTX Exchange", group=17)
            elif src == r'\x56eddb7aa87536c09ccc2793473599fd21a8b17f':
                net.add_node(
                    src, title="Binance 17", group=18)
            elif src == r'\x9696f59e4d72e237be84ffd425dcad154bf96976':
                net.add_node(
                    src, title="Binance 18", group=19)
            elif src == r'\xdfd5293d8e347dfe59e90efd55b2956a1343963d':
                net.add_node(
                    src, title="Binance 16", group=20)
            elif src == r'\x283af0b28c62c092c9727f1ee09c02ca627eb7f5':
                net.add_node(
                    src, title="ENS: ETH Registrar Controller", group=21)
            elif src == r'\x83c8f28c26bf6aaca652df1dbbe0e1b56f8baba2':
                net.add_node(
                    src, title="Gem: GemSwap 2", group=22)
            elif src == r'\xfbddadd80fe7bda00b901fbaf73803f2238ae655':
                net.add_node(
                    src, title="StrongBlock: Service", group=23)
            elif src == r'\xc098b2a3aa256d2140208c3de6543aaef5cd3a94':
                net.add_node(
                    src, title="FTX Exchange 2", group=24)
            elif src == r'\x881d40237659c251811cec9c364ef91dc08d300c':
                net.add_node(
                    src, title="Metamask Swap Router", group=25)
            elif src == r'\x15d4c048f83bd7e37d49ea4c83a07267ec4203da':
                net.add_node(
                    src, title="GALA: GALA Token", group=26)
            elif src == r'\x5041ed759dd4afc3a72b8192c143f72f4724081a':
                net.add_node(
                    src, title="OKEx 7", group=27)
            elif src == r'\x3845badade8e6dff049820680d1f14bd3903a5d0':
                net.add_node(
                    src, title="The Sandbox: SAND Token", group=28)
            elif src == r'\x9813037ee2218799597d83d4a5b6f3b6778218d9':
                net.add_node(
                    src, title="ShibaSwap: BONE Token", group=29)
            elif src == r'\x55fe002aeff02f77364de339a1292923a15844b8':
                net.add_node(
                    src, title="Circle", group=30)
            elif src == r'\x7d1afa7b718fb893db30a3abc0cfc608aacfebb0':
                net.add_node(
                    src, title="Polygon (Matic): Matic Token", group=31)
            elif src == r'\x21a31ee1afc51d94c2efccaa2092ad1028285549':
                net.add_node(
                    src, title="Binance 15", group=32)
            elif src == r'\xddfabcdc4d8ffc6d5beaf154f18b778f892a0740':
                net.add_node(
                    src, title="Coinbase 3", group=33)
            elif src == r'\x4fabb145d64652a948d72533023f6e7a623c7c53':
                net.add_node(
                    src, title="Binance: USD", group=34)
            elif src == r'\xa5409ec958c83c3f309868babaca7c86dcb077c1':
                net.add_node(
                    src, title="OpenSea: Registry", group=35)
            elif src == r'\x6b175474e89094c44da98b954eedeac495271d0f':
                net.add_node(
                    src, title="Maker: Dai Stablecoin", group=36)
            else:
                net.add_node(src, title=src, group=0)

            if tar == r'\xdac17f958d2ee523a2206206994597c13d831ec7':
                net.add_node(
                    tar, title="Tether: USDT Stablecoin", group=1)
            elif tar == r'\xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48':
                net.add_node(
                    tar, title="Centre: USD Coin", group=2)
            elif tar == r'\x00000000006c3852cbef3e08e8df289169ede581':
                net.add_node(
                    tar, title="OpenSea: Seaport 1.1", group=3)
            elif tar == r'\x46340b20830761efd32832a74d7169b29feb9758':
                net.add_node(
                    tar, title="Crypto.com 2", group=4)
            elif tar == r'\xdb7b094fdc04f51560a03a99f747044951b73727':
                net.add_node(tar, title="Moonbirds2 Contract", group=5)
            elif tar == r'\x0d8f1817c644101a915852841a3b5933b0b8dcc7':
                net.add_node(tar, title="The Last Azaraks Contract", group=6)
            elif tar == r'\x74312363e45dcaba76c59ec49a7aa8a65a67eed3':
                net.add_node(
                    tar, title="X2Y2: Exchange", group=7)
            elif tar == r'\x68b3465833fb72a70ecdf485e0e4c7bd8665fc45':
                net.add_node(
                    tar, title="Uniswap V3: Router 2", group=8)
            elif tar == r'\x28c6c06298d514db089934071355e5743bf21d60':
                net.add_node(tar, title="Binance 14", group=9)
            elif tar == r'\xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2':
                net.add_node(
                    tar, title="Wrapped Ether", group=10)
            elif tar == r'\x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88':
                net.add_node(tar, title="MEXC: Mexc.com", group=11)
            elif tar == r'\x9ec9d9fd1aa941ed171e7a3951d68e96137ed21e':
                net.add_node(
                    tar, title="FlowerPower Contract", group=12)
            elif tar == r'\x3cd751e6b0078be393132286c442345e5dc49699':
                net.add_node(tar, title="Coinbase 4", group=13)
            elif tar == r'\x267be1c1d684f78cb4f6a176c4911b741e4ffdc0':
                net.add_node(tar, title="Kraken 4", group=14)
            elif tar == r'\x7a250d5630b4cf539739df2c5dacb4c659f2488d':
                net.add_node(
                    tar, title="Uniswap V2: Router 2", group=15)
            elif tar == r'\xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511':
                net.add_node(
                    tar, title="Coinbase 5", group=16)
            elif tar == r'\x2faf487a4414fe77e2327f0bf4ae2a264a776ad2':
                net.add_node(
                    tar, title="FTX Exchange", group=17)
            elif tar == r'\x56eddb7aa87536c09ccc2793473599fd21a8b17f':
                net.add_node(
                    tar, title="Binance 17", group=18)
            elif tar == r'\x9696f59e4d72e237be84ffd425dcad154bf96976':
                net.add_node(
                    tar, title="Binance 18", group=19)
            elif tar == r'\xdfd5293d8e347dfe59e90efd55b2956a1343963d':
                net.add_node(
                    tar, title="Binance 16", group=20)
            elif tar == r'\x283af0b28c62c092c9727f1ee09c02ca627eb7f5':
                net.add_node(
                    tar, title="ENS: ETH Registrar Controller", group=21)
            elif tar == r'\x83c8f28c26bf6aaca652df1dbbe0e1b56f8baba2':
                net.add_node(
                    tar, title="Gem: GemSwap 2", group=22)
            elif tar == r'\xfbddadd80fe7bda00b901fbaf73803f2238ae655':
                net.add_node(
                    tar, title="StrongBlock: Service", group=23)
            elif tar == r'\xc098b2a3aa256d2140208c3de6543aaef5cd3a94':
                net.add_node(
                    tar, title="FTX Exchange 2", group=24)
            elif tar == r'\x881d40237659c251811cec9c364ef91dc08d300c':
                net.add_node(
                    tar, title="Metamask Swap Router", group=25)
            elif tar == r'\x15d4c048f83bd7e37d49ea4c83a07267ec4203da':
                net.add_node(
                    tar, title="GALA: GALA Token", group=26)
            elif tar == r'\x5041ed759dd4afc3a72b8192c143f72f4724081a':
                net.add_node(
                    tar, title="OKEx 7", group=27)
            elif tar == r'\x3845badade8e6dff049820680d1f14bd3903a5d0':
                net.add_node(
                    tar, title="The Sandbox: SAND Token", group=28)
            elif tar == r'\x9813037ee2218799597d83d4a5b6f3b6778218d9':
                net.add_node(
                    tar, title="ShibaSwap: BONE Token", group=29)
            elif tar == r'\x55fe002aeff02f77364de339a1292923a15844b8':
                net.add_node(
                    tar, title="Circle", group=30)
            elif tar == r'\x7d1afa7b718fb893db30a3abc0cfc608aacfebb0':
                net.add_node(
                    tar, title="Polygon (Matic): Matic Token", group=31)
            elif tar == r'\x21a31ee1afc51d94c2efccaa2092ad1028285549':
                net.add_node(
                    tar, title="Binance 15", group=32)
            elif tar == r'\xddfabcdc4d8ffc6d5beaf154f18b778f892a0740':
                net.add_node(
                    tar, title="Coinbase 3", group=33)
            elif tar == r'\x4fabb145d64652a948d72533023f6e7a623c7c53':
                net.add_node(
                    tar, title="Binance: USD", group=34)
            elif tar == r'\xa5409ec958c83c3f309868babaca7c86dcb077c1':
                net.add_node(
                    tar, title="OpenSea: Registry", group=35)
            elif tar == r'\x6b175474e89094c44da98b954eedeac495271d0f':
                net.add_node(
                    tar, title="Maker: Dai Stablecoin", group=36)
            elif tar == "None":
                net.add_node(
                    tar, title="No destination address", group=37)
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

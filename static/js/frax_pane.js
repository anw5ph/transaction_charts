setData();
function setData() {
    fetch('../../frax.json')
    .then(function(response) {
        if (response.status !== 200) {
            console.log(`Looks like there was a problem. Status code: ${response.status}`);
            return;
        }
        response.json().then(function(data) {

            console.log(data);
            data = JSON.parse(data);

            const node_num = document.getElementById("frax_node_num");
            node_num.innerText = data.num_node;

            const edge_num = document.getElementById("frax_edge_num");
            edge_num.innerText = data.num_edge;

            const self_loops_num = document.getElementById("frax_loop_num");
            self_loops_num.innerText = data.num_self_loops;

            const scc_num = document.getElementById("frax_scc_num");
            scc_num.innerText = data.num_conn_comp;

            const density = document.getElementById("frax_density_num");
            density.innerText = Math.round(data.density * 100000) / 100000;
        });
    })

    .catch(function(error) {
        console.log("Fetch error: " + error);
    });

}


// initialize global variables.
var edges;
var nodes;
var network; 
var container;
var options, data;


// This method is responsible for drawing the graph, returns the drawn network
function drawGraph() {
    var container = document.getElementById('frax_network');

    // parsing and collecting nodes and edges from the python
    nodes = new vis.DataSet([{"group": 0, "id": "\\x1c073d5045b1abb6924d5f0f8b2f667b1653a4c3", "label": "\\x1c073d5045b1abb6924d5f0f8b2f667b1653a4c3", "shape": "dot", "title": "\\x1c073d5045b1abb6924d5f0f8b2f667b1653a4c3", "value": 1}, {"group": 0, "id": "\\xc69ddcd4dfef25d8a793241834d4cc4b3668ead6", "label": "\\xc69ddcd4dfef25d8a793241834d4cc4b3668ead6", "shape": "dot", "title": "\\xc69ddcd4dfef25d8a793241834d4cc4b3668ead6", "value": 0}, {"group": 0, "id": "\\x2ce1a66f22a2dc6e410d9021d57aeb8d13d6bfef", "label": "\\x2ce1a66f22a2dc6e410d9021d57aeb8d13d6bfef", "shape": "dot", "title": "\\x2ce1a66f22a2dc6e410d9021d57aeb8d13d6bfef", "value": 1}, {"group": 0, "id": "\\x9a834b70c07c81a9fcd6f22e842bf002fbffbe4d", "label": "\\x9a834b70c07c81a9fcd6f22e842bf002fbffbe4d", "shape": "dot", "title": "\\x9a834b70c07c81a9fcd6f22e842bf002fbffbe4d", "value": 2}, {"group": 4, "id": "\\x2dce0dda1c2f98e0f171de8333c3c6fe1bbf4877", "label": "\\x2dce0dda1c2f98e0f171de8333c3c6fe1bbf4877", "shape": "dot", "title": "Uniswap V2: OHM-FRAX", "value": 1}, {"group": 5, "id": "\\x97c4adc5d28a86f9470c70dd91dc6cc2f20d2d4d", "label": "\\x97c4adc5d28a86f9470c70dd91dc6cc2f20d2d4d", "shape": "dot", "title": "Uniswap V2: FRAX-USDC 2", "value": 0}, {"group": 0, "id": "\\x3897f792662b6d708f94a3025c02373327c5765e", "label": "\\x3897f792662b6d708f94a3025c02373327c5765e", "shape": "dot", "title": "\\x3897f792662b6d708f94a3025c02373327c5765e", "value": 1}, {"group": 0, "id": "\\x5423a31ecdc46ac59a863c920446e410449e39e4", "label": "\\x5423a31ecdc46ac59a863c920446e410449e39e4", "shape": "dot", "title": "\\x5423a31ecdc46ac59a863c920446e410449e39e4", "value": 1}, {"group": 1, "id": "\\x6021444f1706f15465bee85463bcc7d7cc17fc03", "label": "\\x6021444f1706f15465bee85463bcc7d7cc17fc03", "shape": "dot", "title": "Temple Uniswap V2 Pair Contract", "value": 2}, {"group": 0, "id": "\\xc61f78b49d9906291a47e196766cdf85f7e88fb5", "label": "\\xc61f78b49d9906291a47e196766cdf85f7e88fb5", "shape": "dot", "title": "\\xc61f78b49d9906291a47e196766cdf85f7e88fb5", "value": 0}, {"group": 0, "id": "\\x913a5793eb4081e06aa6744ad0705f89d46999c3", "label": "\\x913a5793eb4081e06aa6744ad0705f89d46999c3", "shape": "dot", "title": "\\x913a5793eb4081e06aa6744ad0705f89d46999c3", "value": 1}, {"group": 0, "id": "\\x610bb423d080dbbb9ea5fb8bab100aad2d81bca4", "label": "\\x610bb423d080dbbb9ea5fb8bab100aad2d81bca4", "shape": "dot", "title": "\\x610bb423d080dbbb9ea5fb8bab100aad2d81bca4", "value": 1}, {"group": 3, "id": "\\x8300f0528e00ad33b218bb05d396f61a9fdd68cd", "label": "\\x8300f0528e00ad33b218bb05d396f61a9fdd68cd", "shape": "dot", "title": "FraxswapPair", "value": 1}, {"group": 7, "id": "\\xc2a856c3aff2110c1171b8f942256d40e980c726", "label": "\\xc2a856c3aff2110c1171b8f942256d40e980c726", "shape": "dot", "title": "Uniswap V3: FRAX-USDT", "value": 0}, {"group": 8, "id": "\\x92c7b5ce4cb0e5483f3365c1449f21578ee9f21a", "label": "\\x92c7b5ce4cb0e5483f3365c1449f21578ee9f21a", "shape": "dot", "title": "Uniswap V3: FRAX", "value": 1}, {"group": 9, "id": "\\x97e7d56a0408570ba1a7852de36350f7713906ec", "label": "\\x97e7d56a0408570ba1a7852de36350f7713906ec", "shape": "dot", "title": "Uniswap V3: DAI-FRAX", "value": 1}, {"group": 10, "id": "\\x8ce5796ef6b0c5918025bcf4f9ca908201b030b3", "label": "\\x8ce5796ef6b0c5918025bcf4f9ca908201b030b3", "shape": "dot", "title": "Uniswap V3: agEUR-FRAX", "value": 0}, {"group": 0, "id": "\\x9a22cdb1ca1cdd2371cd5bb5199564c4e89465eb", "label": "\\x9a22cdb1ca1cdd2371cd5bb5199564c4e89465eb", "shape": "dot", "title": "\\x9a22cdb1ca1cdd2371cd5bb5199564c4e89465eb", "value": 1}, {"group": 0, "id": "\\xc4f3a14f53669d732cf7249385163fb41e6176a1", "label": "\\xc4f3a14f53669d732cf7249385163fb41e6176a1", "shape": "dot", "title": "\\xc4f3a14f53669d732cf7249385163fb41e6176a1", "value": 0}, {"group": 11, "id": "\\xd632f22692fac7611d2aa1c0d552930d43caed3b", "label": "\\xd632f22692fac7611d2aa1c0d552930d43caed3b", "shape": "dot", "title": "Frax FinanceL FRAX3CRV-f Token", "value": 1}]);
    edges = new vis.DataSet([{"arrows": "to", "from": "\\x1c073d5045b1abb6924d5f0f8b2f667b1653a4c3", "title": "Date: 2022-08-04T19:30:40+00:00\n Amount: 32000.97909758708 tokens", "to": "\\xc69ddcd4dfef25d8a793241834d4cc4b3668ead6"}, {"arrows": "to", "from": "\\x2ce1a66f22a2dc6e410d9021d57aeb8d13d6bfef", "title": "Date: 2022-08-04T19:24:50+00:00\n Amount: 798.2364685059122 tokens", "to": "\\x9a834b70c07c81a9fcd6f22e842bf002fbffbe4d"}, {"arrows": "to", "from": "\\x2dce0dda1c2f98e0f171de8333c3c6fe1bbf4877", "title": "Date: 2022-08-04T18:45:27+00:00\n Amount: 56.10585539410743 tokens", "to": "\\x97c4adc5d28a86f9470c70dd91dc6cc2f20d2d4d"}, {"arrows": "to", "from": "\\x3897f792662b6d708f94a3025c02373327c5765e", "title": "Date: 2022-08-04T19:39:11+00:00\n Amount: 4266.20169727932 tokens", "to": "\\x9a834b70c07c81a9fcd6f22e842bf002fbffbe4d"}, {"arrows": "to", "from": "\\x5423a31ecdc46ac59a863c920446e410449e39e4", "title": "Date: 2022-08-04T19:24:09+00:00\n Amount: 2474.6381397351606 tokens", "to": "\\x9a834b70c07c81a9fcd6f22e842bf002fbffbe4d"}, {"arrows": "to", "from": "\\x6021444f1706f15465bee85463bcc7d7cc17fc03", "title": "Date: 2022-08-04T18:50:35+00:00\n Amount: 458.78593426173467 tokens", "to": "\\xc61f78b49d9906291a47e196766cdf85f7e88fb5"}, {"arrows": "to", "from": "\\x6021444f1706f15465bee85463bcc7d7cc17fc03", "title": "Date: 2022-08-04T19:29:59+00:00\n Amount: 3807.6174787414743 tokens", "to": "\\x913a5793eb4081e06aa6744ad0705f89d46999c3"}, {"arrows": "to", "from": "\\x610bb423d080dbbb9ea5fb8bab100aad2d81bca4", "title": "Date: 2022-08-04T18:55:34+00:00\n Amount: 50000.0 tokens", "to": "\\x6021444f1706f15465bee85463bcc7d7cc17fc03"}, {"arrows": "to", "from": "\\x8300f0528e00ad33b218bb05d396f61a9fdd68cd", "title": "Date: 2022-08-04T19:40:04+00:00\n Amount: 5080.676723592622 tokens", "to": "\\x9a834b70c07c81a9fcd6f22e842bf002fbffbe4d"}, {"arrows": "to", "from": "\\x913a5793eb4081e06aa6744ad0705f89d46999c3", "title": "Date: 2022-08-04T19:33:37+00:00\n Amount: 3807.6174787414743 tokens", "to": "\\xc2a856c3aff2110c1171b8f942256d40e980c726"}, {"arrows": "to", "from": "\\x92c7b5ce4cb0e5483f3365c1449f21578ee9f21a", "title": "Date: 2022-08-04T19:39:11+00:00\n Amount: 4266.20169727932 tokens", "to": "\\x3897f792662b6d708f94a3025c02373327c5765e"}, {"arrows": "to", "from": "\\x97e7d56a0408570ba1a7852de36350f7713906ec", "title": "Date: 2022-08-04T19:18:44+00:00\n Amount: 20193.985434706225 tokens", "to": "\\x8ce5796ef6b0c5918025bcf4f9ca908201b030b3"}, {"arrows": "to", "from": "\\x9a22cdb1ca1cdd2371cd5bb5199564c4e89465eb", "title": "Date: 2022-08-04T19:24:09+00:00\n Amount: 798.2364685059122 tokens", "to": "\\x2ce1a66f22a2dc6e410d9021d57aeb8d13d6bfef"}, {"arrows": "to", "from": "\\x9a834b70c07c81a9fcd6f22e842bf002fbffbe4d", "title": "Date: 2022-08-04T19:14:58+00:00\n Amount: 100003.84914941707 tokens", "to": "\\xc4f3a14f53669d732cf7249385163fb41e6176a1"}, {"arrows": "to", "from": "\\x9a834b70c07c81a9fcd6f22e842bf002fbffbe4d", "title": "Date: 2022-08-04T19:30:40+00:00\n Amount: 32000.97909758708 tokens", "to": "\\x1c073d5045b1abb6924d5f0f8b2f667b1653a4c3"}, {"arrows": "to", "from": "\\xd632f22692fac7611d2aa1c0d552930d43caed3b", "title": "Date: 2022-08-04T19:24:09+00:00\n Amount: 2474.6381397351606 tokens", "to": "\\x5423a31ecdc46ac59a863c920446e410449e39e4"}]);

    data = {nodes: nodes, edges: edges};

    var options = {
        "configure": {
            "enabled": false
        },
        "edges": {
            "color": {
                "inherit": true
            },
            "smooth": {
                "enabled": true,
                "type": "dynamic"
            }
        },
        "interaction": {
            "dragNodes": true,
            "hideEdgesOnDrag": false,
            "hideNodesOnDrag": false
        },
        "physics": {
            "enabled": true,
            "stabilization": {
                "enabled": true,
                "fit": true,
                "iterations": 1000,
                "onlyDynamicEdges": false,
                "updateInterval": 50
            }
        }
    };

    network = new vis.Network(container, data, options);

    return network;

}

drawGraph();
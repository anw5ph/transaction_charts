setData();
function setData() {
    fetch('../../chz.json')
    .then(function(response) {
        if (response.status !== 200) {
            console.log(`Looks like there was a problem. Status code: ${response.status}`);
            return;
        }
        response.json().then(function(data) {

            console.log(data);
            data = JSON.parse(data);

            const node_num = document.getElementById("chz_node_num");
            node_num.innerText = data.num_node;

            const edge_num = document.getElementById("chz_edge_num");
            edge_num.innerText = data.num_edge;

            const self_loops_num = document.getElementById("chz_loop_num");
            self_loops_num.innerText = data.num_self_loops;

            const scc_num = document.getElementById("chz_scc_num");
            scc_num.innerText = data.num_conn_comp;

            const density = document.getElementById("chz_density_num");
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
    var container = document.getElementById('chz_network');

     // parsing and collecting nodes and edges from the python
     nodes = new vis.DataSet([{"group": 12, "id": "\\xdfd5293d8e347dfe59e90efd55b2956a1343963d", "label": "\\xdfd5293d8e347dfe59e90efd55b2956a1343963d", "shape": "dot", "title": "Binance 16", "value": 2}, {"group": 0, "id": "\\xd546a644a8b5387d2b970bc5c5a945bface5dc58", "label": "\\xd546a644a8b5387d2b970bc5c5a945bface5dc58", "shape": "dot", "title": "\\xd546a644a8b5387d2b970bc5c5a945bface5dc58", "value": 1}, {"group": 0, "id": "\\xf6c15b384b640e5ac718c2da1fc6d4cc6be063a0", "label": "\\xf6c15b384b640e5ac718c2da1fc6d4cc6be063a0", "shape": "dot", "title": "\\xf6c15b384b640e5ac718c2da1fc6d4cc6be063a0", "value": 1}, {"group": 0, "id": "\\x74de5d4fcbf63e00296fd95d33236b9794016631", "label": "\\x74de5d4fcbf63e00296fd95d33236b9794016631", "shape": "dot", "title": "\\x74de5d4fcbf63e00296fd95d33236b9794016631", "value": 1}, {"group": 5, "id": "\\x325365ed8275f6a74cac98917b7f6face8da533b", "label": "\\x325365ed8275f6a74cac98917b7f6face8da533b", "shape": "dot", "title": "Uniswap V3: CHZ", "value": 0}, {"group": 1, "id": "\\x6cc5f688a315f3dc28a7781717a9a798a59fda7b", "label": "\\x6cc5f688a315f3dc28a7781717a9a798a59fda7b", "shape": "dot", "title": "OKEx", "value": 1}, {"group": 0, "id": "\\x6643887784cb89cc9537dbb7ea20b00c45abeefb", "label": "\\x6643887784cb89cc9537dbb7ea20b00c45abeefb", "shape": "dot", "title": "\\x6643887784cb89cc9537dbb7ea20b00c45abeefb", "value": 1}, {"group": 2, "id": "\\x28c6c06298d514db089934071355e5743bf21d60", "label": "\\x28c6c06298d514db089934071355e5743bf21d60", "shape": "dot", "title": "Binance 14", "value": 2}, {"group": 0, "id": "\\xaeee0f86a109adea9b632e41d903e9edcab4f8e6", "label": "\\xaeee0f86a109adea9b632e41d903e9edcab4f8e6", "shape": "dot", "title": "\\xaeee0f86a109adea9b632e41d903e9edcab4f8e6", "value": 0}, {"group": 0, "id": "\\xcdc8488e63a403bfd580222ea0f3719477bfea9c", "label": "\\xcdc8488e63a403bfd580222ea0f3719477bfea9c", "shape": "dot", "title": "\\xcdc8488e63a403bfd580222ea0f3719477bfea9c", "value": 1}, {"group": 0, "id": "\\x93cc03a658cd104195e5a7ffc49e6f03bcdc1554", "label": "\\x93cc03a658cd104195e5a7ffc49e6f03bcdc1554", "shape": "dot", "title": "\\x93cc03a658cd104195e5a7ffc49e6f03bcdc1554", "value": 0}, {"group": 0, "id": "\\xb8001c3ec9aa1985f6c747e25c28324e4a361ec1", "label": "\\xb8001c3ec9aa1985f6c747e25c28324e4a361ec1", "shape": "dot", "title": "\\xb8001c3ec9aa1985f6c747e25c28324e4a361ec1", "value": 0}, {"group": 3, "id": "\\x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88", "label": "\\x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88", "shape": "dot", "title": "MEXC: Mexc.com", "value": 2}, {"group": 0, "id": "\\x1c39007238cacff7eb728f3b389e7061e4a3a9d8", "label": "\\x1c39007238cacff7eb728f3b389e7061e4a3a9d8", "shape": "dot", "title": "\\x1c39007238cacff7eb728f3b389e7061e4a3a9d8", "value": 1}, {"group": 0, "id": "\\xa9d1e08c7793af67e9d92fe308d5697fb81d3e43", "label": "\\xa9d1e08c7793af67e9d92fe308d5697fb81d3e43", "shape": "dot", "title": "\\xa9d1e08c7793af67e9d92fe308d5697fb81d3e43", "value": 3}, {"group": 0, "id": "\\xc8ab0209700e6c06d2b48b3de09fb1b468723355", "label": "\\xc8ab0209700e6c06d2b48b3de09fb1b468723355", "shape": "dot", "title": "\\xc8ab0209700e6c06d2b48b3de09fb1b468723355", "value": 0}, {"group": 0, "id": "\\x27239549dd40e1d60f5b80b0c4196923745b1fd2", "label": "\\x27239549dd40e1d60f5b80b0c4196923745b1fd2", "shape": "dot", "title": "\\x27239549dd40e1d60f5b80b0c4196923745b1fd2", "value": 2}, {"group": 6, "id": "\\xff58711683be66dad6e0e20e0043af46fc7f5f49", "label": "\\xff58711683be66dad6e0e20e0043af46fc7f5f49", "shape": "dot", "title": "Uniswap V2: CHZ 3", "value": 0}, {"group": 0, "id": "\\xa25c082701050e4f980e00b5c06affa74f1db3c8", "label": "\\xa25c082701050e4f980e00b5c06affa74f1db3c8", "shape": "dot", "title": "\\xa25c082701050e4f980e00b5c06affa74f1db3c8", "value": 1}, {"group": 0, "id": "\\x558247e365be655f9144e1a0140d793984372ef3", "label": "\\x558247e365be655f9144e1a0140d793984372ef3", "shape": "dot", "title": "\\x558247e365be655f9144e1a0140d793984372ef3", "value": 0}, {"group": 0, "id": "\\xf89d7b9c864f589bbf53a82105107622b35eaa40", "label": "\\xf89d7b9c864f589bbf53a82105107622b35eaa40", "shape": "dot", "title": "\\xf89d7b9c864f589bbf53a82105107622b35eaa40", "value": 0}, {"group": 0, "id": "\\x4235b215e764590339c6db542e7c8ca91dcf1795", "label": "\\x4235b215e764590339c6db542e7c8ca91dcf1795", "shape": "dot", "title": "\\x4235b215e764590339c6db542e7c8ca91dcf1795", "value": 0}, {"group": 7, "id": "\\x0d0707963952f2fba59dd06f2b425ace40b492fe", "label": "\\x0d0707963952f2fba59dd06f2b425ace40b492fe", "shape": "dot", "title": "Gate.io", "value": 1}, {"group": 0, "id": "\\x9e99c7debcde21e5ca9d04322b3be130c662e5a0", "label": "\\x9e99c7debcde21e5ca9d04322b3be130c662e5a0", "shape": "dot", "title": "\\x9e99c7debcde21e5ca9d04322b3be130c662e5a0", "value": 0}, {"group": 0, "id": "\\x1c17622cfa9b6fd2043a76dfc39a5b5a109aa708", "label": "\\x1c17622cfa9b6fd2043a76dfc39a5b5a109aa708", "shape": "dot", "title": "\\x1c17622cfa9b6fd2043a76dfc39a5b5a109aa708", "value": 1}, {"group": 0, "id": "\\x3b59a023d74aceca4b10b134fd218f887fa0ec1b", "label": "\\x3b59a023d74aceca4b10b134fd218f887fa0ec1b", "shape": "dot", "title": "\\x3b59a023d74aceca4b10b134fd218f887fa0ec1b", "value": 1}, {"group": 13, "id": "\\x21a31ee1afc51d94c2efccaa2092ad1028285549", "label": "\\x21a31ee1afc51d94c2efccaa2092ad1028285549", "shape": "dot", "title": "Binance 15", "value": 1}, {"group": 0, "id": "\\x3803d1d9217d056c80afb32e7896923424c35f2a", "label": "\\x3803d1d9217d056c80afb32e7896923424c35f2a", "shape": "dot", "title": "\\x3803d1d9217d056c80afb32e7896923424c35f2a", "value": 0}, {"group": 0, "id": "\\x7bd8efab672250de65ba4ba3bc6c3aa08120a1c3", "label": "\\x7bd8efab672250de65ba4ba3bc6c3aa08120a1c3", "shape": "dot", "title": "\\x7bd8efab672250de65ba4ba3bc6c3aa08120a1c3", "value": 2}, {"group": 0, "id": "\\x6e55809645fb876566d22156612b137b93f06c9b", "label": "\\x6e55809645fb876566d22156612b137b93f06c9b", "shape": "dot", "title": "\\x6e55809645fb876566d22156612b137b93f06c9b", "value": 0}, {"group": 0, "id": "\\xf80dc2bb5d2c2b96c06606765cc5b5f9d561b292", "label": "\\xf80dc2bb5d2c2b96c06606765cc5b5f9d561b292", "shape": "dot", "title": "\\xf80dc2bb5d2c2b96c06606765cc5b5f9d561b292", "value": 1}, {"group": 8, "id": "\\x5f65f7b609678448494de4c87521cdf6cef1e932", "label": "\\x5f65f7b609678448494de4c87521cdf6cef1e932", "shape": "dot", "title": "Gemini 4", "value": 0}, {"group": 0, "id": "\\x69ed546ae6aabb0dda338ae3aba05a215c63639d", "label": "\\x69ed546ae6aabb0dda338ae3aba05a215c63639d", "shape": "dot", "title": "\\x69ed546ae6aabb0dda338ae3aba05a215c63639d", "value": 0}, {"group": 0, "id": "\\x8ada91f2a59fdd51a17c31da13b608a1b2e93529", "label": "\\x8ada91f2a59fdd51a17c31da13b608a1b2e93529", "shape": "dot", "title": "\\x8ada91f2a59fdd51a17c31da13b608a1b2e93529", "value": 0}, {"group": 0, "id": "\\x022b1ef743d3172d24342ba9e2b909f68e559654", "label": "\\x022b1ef743d3172d24342ba9e2b909f68e559654", "shape": "dot", "title": "\\x022b1ef743d3172d24342ba9e2b909f68e559654", "value": 1}, {"group": 0, "id": "\\x01e0d769d32bbd11adc8168fc25ce911dc798905", "label": "\\x01e0d769d32bbd11adc8168fc25ce911dc798905", "shape": "dot", "title": "\\x01e0d769d32bbd11adc8168fc25ce911dc798905", "value": 0}, {"group": 0, "id": "\\xe0094048519936ca6f3711b70b64711fbbbfa41b", "label": "\\xe0094048519936ca6f3711b70b64711fbbbfa41b", "shape": "dot", "title": "\\xe0094048519936ca6f3711b70b64711fbbbfa41b", "value": 1}, {"group": 0, "id": "\\x4c270de592db7a3b01fda2ad7d485ce278d5b24c", "label": "\\x4c270de592db7a3b01fda2ad7d485ce278d5b24c", "shape": "dot", "title": "\\x4c270de592db7a3b01fda2ad7d485ce278d5b24c", "value": 0}, {"group": 0, "id": "\\x98009ccf0212a75aaaba7f27a8bef19e307c0abf", "label": "\\x98009ccf0212a75aaaba7f27a8bef19e307c0abf", "shape": "dot", "title": "\\x98009ccf0212a75aaaba7f27a8bef19e307c0abf", "value": 0}, {"group": 4, "id": "\\xb0f4a77bde7fee134265307c5cc19abff0ba409b", "label": "\\xb0f4a77bde7fee134265307c5cc19abff0ba409b", "shape": "dot", "title": "Uniswap V3: CHZ-USDT", "value": 1}, {"group": 0, "id": "\\x8d31056fd9fbf5f70096a5d712d9325e20c276af", "label": "\\x8d31056fd9fbf5f70096a5d712d9325e20c276af", "shape": "dot", "title": "\\x8d31056fd9fbf5f70096a5d712d9325e20c276af", "value": 0}, {"group": 0, "id": "\\xcd8a20209437261abf7c357a186c1f50b0944f06", "label": "\\xcd8a20209437261abf7c357a186c1f50b0944f06", "shape": "dot", "title": "\\xcd8a20209437261abf7c357a186c1f50b0944f06", "value": 0}, {"group": 0, "id": "\\x1333926e97af494450a590eb9b21e8fdefc45bc3", "label": "\\x1333926e97af494450a590eb9b21e8fdefc45bc3", "shape": "dot", "title": "\\x1333926e97af494450a590eb9b21e8fdefc45bc3", "value": 1}, {"group": 0, "id": "\\x75acb627b985ce7f1fcd492737c54e687e9a6043", "label": "\\x75acb627b985ce7f1fcd492737c54e687e9a6043", "shape": "dot", "title": "\\x75acb627b985ce7f1fcd492737c54e687e9a6043", "value": 0}, {"group": 9, "id": "\\x98c3d3183c4b8a650614ad179a1a98be0a8d6b8e", "label": "\\x98c3d3183c4b8a650614ad179a1a98be0a8d6b8e", "shape": "dot", "title": "MEV Bot", "value": 1}]);
     edges = new vis.DataSet([{"arrows": "to", "from": "\\xdfd5293d8e347dfe59e90efd55b2956a1343963d", "title": "Date: 2022-08-08T14:06:37+00:00\n Amount: 180240.535 tokens", "to": "\\xd546a644a8b5387d2b970bc5c5a945bface5dc58"}, {"arrows": "to", "from": "\\xf6c15b384b640e5ac718c2da1fc6d4cc6be063a0", "title": "Date: 2022-08-08T14:06:30+00:00\n Amount: 896.1381136148034 tokens", "to": "\\x74de5d4fcbf63e00296fd95d33236b9794016631"}, {"arrows": "to", "from": "\\x74de5d4fcbf63e00296fd95d33236b9794016631", "title": "Date: 2022-08-08T14:06:30+00:00\n Amount: 896.1381136148034 tokens", "to": "\\x325365ed8275f6a74cac98917b7f6face8da533b"}, {"arrows": "to", "from": "\\x6cc5f688a315f3dc28a7781717a9a798a59fda7b", "title": "Date: 2022-08-08T14:15:23+00:00\n Amount: 13545.0 tokens", "to": "\\x6643887784cb89cc9537dbb7ea20b00c45abeefb"}, {"arrows": "to", "from": "\\x28c6c06298d514db089934071355e5743bf21d60", "title": "Date: 2022-08-08T14:16:19+00:00\n Amount: 69956.0 tokens", "to": "\\xaeee0f86a109adea9b632e41d903e9edcab4f8e6"}, {"arrows": "to", "from": "\\xcdc8488e63a403bfd580222ea0f3719477bfea9c", "title": "Date: 2022-08-08T14:14:04+00:00\n Amount: 397.33608 tokens", "to": "\\x93cc03a658cd104195e5a7ffc49e6f03bcdc1554"}, {"arrows": "to", "from": "\\xd546a644a8b5387d2b970bc5c5a945bface5dc58", "title": "Date: 2022-08-08T14:18:39+00:00\n Amount: 180240.535 tokens", "to": "\\xb8001c3ec9aa1985f6c747e25c28324e4a361ec1"}, {"arrows": "to", "from": "\\x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88", "title": "Date: 2022-08-08T14:20:52+00:00\n Amount: 2416.0 tokens", "to": "\\x1c39007238cacff7eb728f3b389e7061e4a3a9d8"}, {"arrows": "to", "from": "\\xa9d1e08c7793af67e9d92fe308d5697fb81d3e43", "title": "Date: 2022-08-08T14:21:43+00:00\n Amount: 1198.97325831 tokens", "to": "\\xc8ab0209700e6c06d2b48b3de09fb1b468723355"}, {"arrows": "to", "from": "\\x27239549dd40e1d60f5b80b0c4196923745b1fd2", "title": "Date: 2022-08-08T14:21:24+00:00\n Amount: 555.045484595 tokens", "to": "\\xff58711683be66dad6e0e20e0043af46fc7f5f49"}, {"arrows": "to", "from": "\\xa25c082701050e4f980e00b5c06affa74f1db3c8", "title": "Date: 2022-08-08T14:21:24+00:00\n Amount: 560.36899 tokens", "to": "\\x27239549dd40e1d60f5b80b0c4196923745b1fd2"}, {"arrows": "to", "from": "\\x27239549dd40e1d60f5b80b0c4196923745b1fd2", "title": "Date: 2022-08-08T14:21:24+00:00\n Amount: 5.323505405 tokens", "to": "\\x558247e365be655f9144e1a0140d793984372ef3"}, {"arrows": "to", "from": "\\x6643887784cb89cc9537dbb7ea20b00c45abeefb", "title": "Date: 2022-08-08T14:23:48+00:00\n Amount: 13545.0 tokens", "to": "\\xf89d7b9c864f589bbf53a82105107622b35eaa40"}, {"arrows": "to", "from": "\\xa9d1e08c7793af67e9d92fe308d5697fb81d3e43", "title": "Date: 2022-08-08T14:24:30+00:00\n Amount: 389.5 tokens", "to": "\\x4235b215e764590339c6db542e7c8ca91dcf1795"}, {"arrows": "to", "from": "\\x0d0707963952f2fba59dd06f2b425ace40b492fe", "title": "Date: 2022-08-08T14:30:18+00:00\n Amount: 11250.089587 tokens", "to": "\\x9e99c7debcde21e5ca9d04322b3be130c662e5a0"}, {"arrows": "to", "from": "\\x1c17622cfa9b6fd2043a76dfc39a5b5a109aa708", "title": "Date: 2022-08-08T14:31:17+00:00\n Amount: 471357.0 tokens", "to": "\\x3b59a023d74aceca4b10b134fd218f887fa0ec1b"}, {"arrows": "to", "from": "\\x21a31ee1afc51d94c2efccaa2092ad1028285549", "title": "Date: 2022-08-08T14:34:22+00:00\n Amount: 98.9118094 tokens", "to": "\\x3803d1d9217d056c80afb32e7896923424c35f2a"}, {"arrows": "to", "from": "\\x1c39007238cacff7eb728f3b389e7061e4a3a9d8", "title": "Date: 2022-08-08T14:37:15+00:00\n Amount: 2416.0 tokens", "to": "\\x6cc5f688a315f3dc28a7781717a9a798a59fda7b"}, {"arrows": "to", "from": "\\x7bd8efab672250de65ba4ba3bc6c3aa08120a1c3", "title": "Date: 2022-08-08T14:42:02+00:00\n Amount: 210.89108910891088 tokens", "to": "\\x6e55809645fb876566d22156612b137b93f06c9b"}, {"arrows": "to", "from": "\\xf80dc2bb5d2c2b96c06606765cc5b5f9d561b292", "title": "Date: 2022-08-08T14:46:03+00:00\n Amount: 818.0835308890493 tokens", "to": "\\x5f65f7b609678448494de4c87521cdf6cef1e932"}, {"arrows": "to", "from": "\\x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88", "title": "Date: 2022-08-08T14:42:57+00:00\n Amount: 31088.49 tokens", "to": "\\x69ed546ae6aabb0dda338ae3aba05a215c63639d"}, {"arrows": "to", "from": "\\xdfd5293d8e347dfe59e90efd55b2956a1343963d", "title": "Date: 2022-08-08T14:47:02+00:00\n Amount: 4569.432 tokens", "to": "\\x8ada91f2a59fdd51a17c31da13b608a1b2e93529"}, {"arrows": "to", "from": "\\x022b1ef743d3172d24342ba9e2b909f68e559654", "title": "Date: 2022-08-08T14:45:17+00:00\n Amount: 818.0835308890493 tokens", "to": "\\xf80dc2bb5d2c2b96c06606765cc5b5f9d561b292"}, {"arrows": "to", "from": "\\x6cc5f688a315f3dc28a7781717a9a798a59fda7b", "title": "Date: 2022-08-08T14:48:42+00:00\n Amount: 19299.0 tokens", "to": "\\x6643887784cb89cc9537dbb7ea20b00c45abeefb"}, {"arrows": "to", "from": "\\xa9d1e08c7793af67e9d92fe308d5697fb81d3e43", "title": "Date: 2022-08-08T14:52:53+00:00\n Amount: 9.12408928 tokens", "to": "\\x01e0d769d32bbd11adc8168fc25ce911dc798905"}, {"arrows": "to", "from": "\\xe0094048519936ca6f3711b70b64711fbbbfa41b", "title": "Date: 2022-08-08T14:50:47+00:00\n Amount: 705.6 tokens", "to": "\\x4c270de592db7a3b01fda2ad7d485ce278d5b24c"}, {"arrows": "to", "from": "\\x7bd8efab672250de65ba4ba3bc6c3aa08120a1c3", "title": "Date: 2022-08-08T14:53:17+00:00\n Amount: 19645.186795809448 tokens", "to": "\\x98009ccf0212a75aaaba7f27a8bef19e307c0abf"}, {"arrows": "to", "from": "\\xb0f4a77bde7fee134265307c5cc19abff0ba409b", "title": "Date: 2022-08-08T14:50:36+00:00\n Amount: 642.4036615764156 tokens", "to": "\\x8d31056fd9fbf5f70096a5d712d9325e20c276af"}, {"arrows": "to", "from": "\\x28c6c06298d514db089934071355e5743bf21d60", "title": "Date: 2022-08-08T14:58:00+00:00\n Amount: 4956.07386261 tokens", "to": "\\xcd8a20209437261abf7c357a186c1f50b0944f06"}, {"arrows": "to", "from": "\\x1333926e97af494450a590eb9b21e8fdefc45bc3", "title": "Date: 2022-08-08T14:59:53+00:00\n Amount: 685.02550542 tokens", "to": "\\x75acb627b985ce7f1fcd492737c54e687e9a6043"}, {"arrows": "to", "from": "\\x98c3d3183c4b8a650614ad179a1a98be0a8d6b8e", "title": "Date: 2022-08-08T14:57:12+00:00\n Amount: 24305.0 tokens", "to": "\\xb0f4a77bde7fee134265307c5cc19abff0ba409b"}, {"arrows": "to", "from": "\\x3b59a023d74aceca4b10b134fd218f887fa0ec1b", "title": "Date: 2022-08-08T15:00:19+00:00\n Amount: 471357.0 tokens", "to": "\\x28c6c06298d514db089934071355e5743bf21d60"}, {"arrows": "to", "from": "\\x6643887784cb89cc9537dbb7ea20b00c45abeefb", "title": "Date: 2022-08-08T14:58:42+00:00\n Amount: 19299.0 tokens", "to": "\\xf89d7b9c864f589bbf53a82105107622b35eaa40"}]);
     
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
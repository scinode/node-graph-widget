from node_graph_widget import NodeGraphWidget


def test_widget():
    nodegraph_data = {'name': 'example',
    'uuid': '17ae596a-b179-11ef-a97d-906584de3e5b',
    'state': 'CREATED',
    'nodes': {'test_float1': {'label': 'test_float1',
    'node_type': 'NORMAL',
    'inputs': [],
    'properties': {},
    'outputs': [{'name': 'float'}],
    'position': [30, 30],
    'children': []},
    'test_float2': {'label': 'test_float2',
    'node_type': 'NORMAL',
    'inputs': [],
    'properties': {},
    'outputs': [{'name': 'float'}],
    'position': [60, 60],
    'children': []},
    'test_add3': {'label': 'test_add3',
    'node_type': 'NORMAL',
    'inputs': [{'name': 'x'}, {'name': 'y'}],
    'properties': {},
    'outputs': [],
    'position': [90, 90],
    'children': []}},
    'links': [{'from_socket': 'float',
    'from_node': 'test_float1',
    'to_socket': 'x',
    'to_node': 'test_add3',
    'state': False},
    {'from_socket': 'float',
    'from_node': 'test_float2',
    'to_socket': 'y',
    'to_node': 'test_add3',
    'state': False}]}
    
    v = NodeGraphWidget()
    v.value = nodegraph_data
    v
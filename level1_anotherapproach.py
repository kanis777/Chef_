import json
import operator
import numpy as np

def tsp(current_vertex, distance_matrix, visited, res, cost):
    adj_vertex = 999
    min_val = float('inf')
    visited[current_vertex] = 1
    print((current_vertex + 1), end=" ")
    res.append(current_vertex - 1)
    print('the distance matrix contains')
    print(distance_matrix)
    for k in range(len(distance_matrix)):
        if distance_matrix[current_vertex][k] != 0 and visited[k] == 0:
            if distance_matrix[current_vertex][k] < min_val:
                min_val = distance_matrix[current_vertex][k]
                adj_vertex = k
    if min_val != float('inf'):
        cost += min_val
    if adj_vertex == 999:
        adj_vertex = 0
        print((adj_vertex + 1), end=" ")
        cost += distance_matrix[current_vertex][adj_vertex]
        return cost
    return tsp(adj_vertex, distance_matrix, visited, res, cost)

def find_dist(res, distance_matrix):
    print('Calculating distances for:', res)
    tsp(0, distance_matrix, visited, res, 0)

def find(source, sorted_dict, distance_matrix):
    capacity = 600
    for keys, values in sorted_dict.items():
        if values < capacity:
            capacity = capacity - values
            res.append(keys)
    find_dist(res, distance_matrix)
    path.append(res)
    if 0 in visited:
        find(0, sorted_dict, distance_matrix)

# Use raw string for file paths
f1 = open(r"C:\mock_hack\Student Handout\Input data\level1a.json")
d1 = json.load(f1)

cap = d1['vehicles']['v0']['capacity']
print('Capacity of vehicle:', cap)
print('Order quantity:', d1['neighbourhoods']['n0']['order_quantity'])

all_orders = []
key_orders = []
res = []
visited = [0] * len(d1['neighbourhoods'])
n = len(d1['neighbourhoods'])

for i in range(len(d1['neighbourhoods'])):
    all_orders.append(d1['neighbourhoods'][f'n{i}']['order_quantity'])
    key_orders.append(f'n{i}')

dict1 = dict(zip(key_orders, all_orders))
sorted_dict = dict(sorted(dict1.items(), key=operator.itemgetter(1), reverse=True))

print(sorted_dict)
path = []
distance_matrix = np.array(d1['neighbourhoods']['n0']['distances'])
find(0, sorted_dict, distance_matrix)
result = {'v0': {'path': path}}
print(result)

with open("level1a_output.json", "w") as outfile:
    json.dump(result, outfile)

import numpy as np
import json

output = []

def travellingsalesman(c):
    global cost
    adj_vertex = 9999999
    min_val = 9999999
    visited[c] = 1
    output.append(c+1)
    print((c + 1), end=" ")
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if min_val != 9999999:
        cost = cost + min_val
    if adj_vertex == 9999999:
        adj_vertex = 0
        output.append(adj_vertex + 1)
        print((adj_vertex + 1), end=" ")
        cost = cost + tsp_g[c][adj_vertex]
        return
    travellingsalesman(adj_vertex)
n = 21
cost = 0
visited = np.zeros(n, dtype=int)
tsp_g = []

json_file_path = 'C:\Student Handout\Input data\level0.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

name = ['n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n16', 'n17', 'n18', 'n19']

r = data['restaurants']['r0']['neighbourhood_distance']

for i in range(len(name)+1):
    tsp_g.append([0])

for i in range(len(r)):
    tsp_g[0].append(r[i])



for i in range(1, len(name)+1):
    d = data['neighbourhoods'][name[i-1]]['distances']
    for j in d:
        tsp_g[i].append(j)

for i in range(1, 21):
    tsp_g[i][0] = r[i-1]

tsp_g = np.array(tsp_g)

print("Shortest Path:", end=" ")
travellingsalesman(0)

print()
print("Minimum Cost:", end=" ")
print(cost)

d = {'v0': {'path': {}}}

m = {1: 'r0', 
     2: 'n0',
     3: 'n1',
     4: 'n2',
     5: 'n3',
     6: 'n4',
     7: 'n5',
     8: 'n6',
     9: 'n7',
     10: 'n8',
     11: 'n9',
     12: 'n10',
     13: 'n11',
     14: 'n12',
     15: 'n13',
     16: 'n14',
     17: 'n15',
     18: 'n16',
     19: 'n17',
     20: 'n18',
     21 : 'n19'}

lst = []

for i in range(len(output)):
    lst.append(m[output[i]])

d['v0']['path'] = lst

json_file_path = 'C:\Validators\level0\level0_output.json'

with open(json_file_path, 'w') as json_file:
    json.dump(d, json_file, indent=2)





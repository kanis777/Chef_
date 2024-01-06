import json
import operator

def generate_delivery_path(source, sorted_dict, visited, res, path):
    capacity = 600
    for key, value in sorted_dict.items():
        if value < capacity and not visited[d1['neighbourhoods'][key]]:
            capacity -= value
            res.append(key)
            visited[d1['neighbourhoods'][key]] = 1
    path.append(res)
    if 0 in visited:
        generate_delivery_path(0, sorted_dict, visited, res, path)

# Use raw string for file paths
f1 = open(r"C:\mock_hack\Student Handout\Input data\level1a.json")
d1 = json.load(f1)

rest = d1['restaurants']['r0']['neighbourhood_distance']
print('temp=', rest)

trips = 0
distances = []  # distance matrix
distances.append(rest)
distances[0].insert(0, 0)
val = 1

for i in d1['neighbourhoods']:
    t = d1['neighbourhoods'][i]['distances']
    t.insert(0, rest[val])
    val += 1
    print(t)
    distances.append(t)

for i in distances:
    print(i)

cap = d1['vehicles']['v0']['capacity']
print('capacity of vehicle=', cap)
print('order quantity=', d1['neighbourhoods']['n0']['order_quantity'])

all_orders = []
key_orders = []
res = []
index = []
n = 21
visited = [0] * n
neighborhoods_list = ['n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n16', 'n17', 'n18', 'n19']

for i in range(len(d1['neighbourhoods'])):
    all_orders.append(d1['neighbourhoods'][neighborhoods_list[i]]['order_quantity'])
    key_orders.append(neighborhoods_list[i])
    index.append(i)

dict1 = dict(zip(key_orders, all_orders))
sorted_dict = dict(sorted(dict1.items(), key=operator.itemgetter(1), reverse=True))

print(sorted_dict)
path = []
for key, value in sorted_dict.items():
    print(key, end=' ')

generate_delivery_path(0, sorted_dict, visited, res, path)
result = {'v0': {'path': path}}
print(result)

with open("level1a_output.json", "w") as outfile:
    json.dump(result, outfile)

import json
import operator
import numpy as np 

def find_dist(res):
    rest=d1['restaurants']['r0']['neighbourhood_distance']
    print('temp=',rest)
    distances=[]#distance matrix
    distances.append(rest)
    distances[0].insert(0,0)
    val=1
    for i in range(len(res)):  
        t=d1['neighbourhoods'][res[i]]['distances']#for n0,n1,n2 distances
        t.insert(0,rest[i])
        val=val+1
        print(t)
        distances.append(t)
    for i in distances:
        print(i)
    tsp_g = np.array(distances)
    tsp(0,tsp_g)

def tsp(c,tsp_g):
    global cost
    adj_vertex = 999
    min_val = 10000
    visited[c] = 1
    print((c + 1), end=" ")
    res.append(c-1)
    print('the tsp graph contains')
    print(tsp_g)
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if min_val != 10000:
        cost = cost + min_val
    if adj_vertex == 999:
        adj_vertex = 0
        print((adj_vertex+1), end=" ")  
        cost = cost + tsp_g[c][adj_vertex]
        return
    tsp(adj_vertex,tsp_g)

def find(source,sorted_dict):
    capacity=600
    for keys,values in sorted_dict.items():
        if values<capacity:
            capacity=capacity-values
            res.append(keys)
            #index=list(sorted_dict).index(keys)
            #visited[index]=1
        #now that we found the capacities which can be included now find the minimum path for these n0,n1
    find_dist(res)
    path.append(res)
    if 0 in visited:
        find(0,sorted_dict)
        #if sorted_dict[i][1]
f1 = open("C:\mock_hack\Student Handout\Input data\level1a.json")
d1 = json.load(f1)
cost=0
cap=d1['vehicles']['v0']['capacity']
print('capacity of vehicle=',cap)
print('order quantity=',d1['neighbourhoods']['n0']['order_quantity'])
all_orders=[]
key_orders=[]
res=[]
index=[]
n=21
visited=[0]*n
l=['n0','n1','n2','n3','n4','n5','n6','n7','n8','n9','n10','n11','n12','n13','n14','n15','n16','n17','n18','n19']
for i in range(len(d1['neighbourhoods'])):
    all_orders.append(d1['neighbourhoods'][l[i]]['order_quantity'])
    key_orders.append(l[i])
    index.append(i)
dict1=dict(zip(key_orders,all_orders))
sorted_dict = dict(sorted(dict1.items(), key=operator.itemgetter(1),reverse=True))

print(sorted_dict)
path=[]
for keys,value in sorted_dict.items():
    print(keys,end=' ')
find(0,sorted_dict)
result={'v0': {'path':path}}
print(result)
with open("level1a_output.json", "w") as outfile:
    json.dump(result, outfile)
#my approach-find highest capacities in that range after that find the distance for those capacities res and after that for those find tsp and append each of those paths 
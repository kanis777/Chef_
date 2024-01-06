import json
import numpy as np
def tsp(c,cap,l):
    global cost
    adj_vertex = 999
    min_val = 10000
    visited[c] = 1
    print((c + 1), end=" ")
    res.append(c-1)
    for k in range(n):
        if (visited[k] == 0) and (tsp_g[c][k] != 0):
            if tsp_g[c][k] < min_val and (cap-d1['neighbourhoods'][l[k-1]]['order_quantity'])>0:
                cap=cap-d1['neighbourhoods'][l[k-1]]['order_quantity']
                min_val = tsp_g[c][k]
                adj_vertex = k
    if min_val != 10000:
        cost = cost + min_val
    if adj_vertex == 999:
        adj_vertex = 0
        print((adj_vertex+1), end=" ")  
        cost = cost + tsp_g[c][adj_vertex]
        return
    tsp(adj_vertex,cap,l)


f1 = open("C:\mock_hack\Student Handout\Input data\level1a.json")
d1 = json.load(f1)
rest=d1['restaurants']['r0']['neighbourhood_distance']
print('temp=',rest)
trips=0
distances=[]#distance matrix
distances.append(rest)
distances[0].insert(0,0)
val=1
for i in d1['neighbourhoods']:
    t=d1['neighbourhoods'][i]['distances']#for n0,n1,n2 distances
    t.insert(0,rest[val])
    val=val+1
    print(t)
    distances.append(t)
for i in distances:
    print(i)

cap=d1['vehicles']['v0']['capacity']
print('capacity of vehicle=',cap)
print('order quantity=',d1['neighbourhoods']['n0']['order_quantity'])
num_neighborhoods = d1.get('n_neighbourhoods', 0)
num_restaurants=d1.get('n_restaurants', 0)
n=num_neighborhoods+num_restaurants
print("n=",n)
cost=0
visited=[0]*(n)
res=[]
l=['n0','n1','n2','n3','n4','n5','n6','n7','n8','n9','n10','n11','n12','n13','n14','n15','n16','n17','n18','n19']
trip=0
tsp_g = np.array(distances)
print("Shortest Path:", end=" ")
path=[]
while 0 in visited:
    res1=[]
    res1.append('r0')
    trip+=1
    tsp(0,cap,l) 
    for i in range (1,len(res)):
        s='n'+str(res[i])
        res1.append(s)
    path.append(res1)
result={'v0': {'path':path}}
print(result)
with open("level1a_output.json", "w") as outfile:
    json.dump(result, outfile)
import json
import  numpy as np

def tsp(c):
    global cost
    adj_vertex = 999
    min_val = 10000
    visited[c] = 1
    print((c + 1), end=" ")
    res.append(c-1)
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
    tsp(adj_vertex)

f1 = open("C:\mock_hack\Student Handout\Input data\level0.json")
d1 = json.load(f1)
#print(d1['restaurants'])
#dealing with r0
rest=d1['restaurants']['r0']['neighbourhood_distance']
print('temp=',rest)
distances=[]#distance matrix
distances.append(rest)
distances[0].insert(0,0)#to initialize r0 with r0 as 0 
print('distance now=',distances)
val=1
for i in d1['neighbourhoods']:
    t=d1['neighbourhoods'][i]['distances']#for n0,n1,n2 distances
    t.insert(0,rest[val])
    val=val+1
    print(t)
    distances.append(t)
for i in distances:
    print(i)

res=[]
num_neighborhoods = d1.get('n_neighbourhoods', 0)
num_restaurants=d1.get('n_restaurants', 0)
n = num_neighborhoods + num_restaurants
cost = 0
visited = np.zeros(n, dtype=int)
tsp_g = np.array(distances)
print("Shortest Path:", end=" ")
tsp(0)
print('res=',res)
res1=[]
res1.append('r0')
for i in range (1,len(res)):
    s='n'+str(res[i])
    res1.append(s)
res1.append('r0')
print(res1)
result={'v0': {'path':res1}}
with open("level0_output.json", "w") as outfile:
    json.dump(result, outfile)

	

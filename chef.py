import json
import numpy as np
class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \t Distance from Source")
		for node in range(self.V):
			print(node, "\t\t", dist[node])
			
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = 1e7

		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	def dijkstra(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):
			u = self.minDistance(dist, sptSet)
			sptSet[u] = True
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)
if __name__ == "__main__": 	
    json_file_path = r"C:\mock_hack\Student Handout\Input data\level0.json"
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    g=[]
    name = ['n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n16', 'n17', 'n18', 'n19']
    print("hello")
    r = data['restaurants']['r0']['neighbourhood_distance']
    print("r=",r)
    for i in range(len(name)+1):
        g.append([0])

    for i in range(len(r)):
        g[0].append(r[i])

    for i in range(1, len(name)+1):
        d = data['neighbourhoods'][name[i-1]]['distances']
        for j in d:
            g[i].append(j)

    for i in range(1, 21):
        g[i][0] = r[i-1]

    tsp_g = np.array(g)
    # Extract distances from the neighborhoods section
    neighborhoods_data = data.get('neighbourhoods', {})
    restaurants_data = data.get('restaurants', {})
    num_neighborhoods = data.get('n_neighbourhoods', 0)
    print("Number of Neighborhoods:", num_neighborhoods)

    # Initialize distances matrix with zeros
    distances = [[0] * num_neighborhoods for _ in range(num_neighborhoods+1)]
    i=0
    distances[0]=restaurants_data
    # Fill distances matrix with data from the neighborhoods
    for i in range(1,num_neighborhoods+1):
        for j in range(num_neighborhoods):
            distances[i][j] = neighborhoods_data[f'n{i-1}']['distances'][j-1]
        print(distances[i])
# Driver program
    gr = Graph(num_neighborhoods+1)
    gr.graph = g

    gr.dijkstra(0)



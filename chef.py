import json
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
		
json_file_path = r"C:\mock_hack\Student Handout\Input data\level0.json"
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

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

# Driver program
g = Graph(num_neighborhoods)
g.graph = distances

g.dijkstra(0)

# This code is contributed by Divyanshu Mehta



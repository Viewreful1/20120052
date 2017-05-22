def main():
	global graph, dfsStack, bfsQueue
	dfsStack = []
	bfsQueue = []
	getGraph()
	dfs(v)
	print ""
	bfs(v)

def getGraph():
	global n, m, v, matrix, visited
	n, m, v = map(int, raw_input().split())
	visited = [0 for number in range(n+1)]
	matrix = [[0 for col in range(n+1)] for row in range(n+1)]

	for i in range(m):
		a, b = map(int, raw_input().split())
		matrix[a][b] = matrix[b][a] = 1

def dfs(v):
	visited[v] = 1
	dfsStack.append(v)
	print v,

	for i in range(1, n+1):
		if matrix[v][i] and (not visited[i]):
			dfs(i)

def bfs(v):
	visited = [False for number in range(n+1)]
	visited[v] = 1
	bfsQueue.append(v)
	while bfsQueue != []:
		current = bfsQueue[0]
		bfsQueue.pop(0)
		print current,
		for i in range(1, n+1):
			if (matrix[current][i] == 1) and visited[i] == False:
				visited[i] = True
				bfsQueue.append(i)

main()
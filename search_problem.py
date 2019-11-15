# import sys

"""
P1) Perform DFS and BFS on unweighted graphs G1 and G2.

Given the undirected graph G1 represented as vertex-list:
Perform DFS using recursion. (1pt)
"""


graph = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd', 'f'],
    'd': ['b', 'c', 'e', 's'],
    'e': ['d', 'h', 'r', 's'],
    'f': ['c', 'g', 'r'],
    'h': ['e', 'p', 'q'],
    's': ['d', 'e', 'p'],
    'r': ['e', 'f'],
    'p': ['h', 'q', 's'],
    'q': ['h', 'p'],
    'g': ['f']
}

# graph = {
# 	'a': ['c', 's'],
# 	'b': ['d', 's'],
# 	'c': ['a', 'd', 'g'],
# 	'd': ['b', 'c', 'g', 's'],
# 	'g': ['c', 'd'],
# 	's': ['a', 'b', 'd']
# }

start = 's'
goal = 'g'
expanded_states = [start]

def dfs_recursion(graph, start, path):
	if start == goal:
		print('Perform DFS using recursion\npath returned {}\nexpanded_states {}\n________________'.
			format(path, expanded_states))
	else:
		for ajacent in graph[start]:
			if ajacent not in path and ajacent not in expanded_states:
				expanded_states.append(ajacent)
				dfs_recursion(graph, ajacent, path+[ajacent])

"""
P1) Perform DFS and BFS on unweighted graphs G1 and G2.

Given the undirected graph G1 represented as vertex-list:
Perform DFS using stack. (1pt)
"""

def dfs_stack(graph, start, goal, expanded_states):

	def IsBackTracingPoint(node, path, visited):
		"""
		"""
		allready_visited = 0
		connect_node = graph[node]
		for cnode in connect_node:
			if cnode in visited:
				allready_visited += 1
		return True if allready_visited == len(graph[node]) else False

	visited = {}
	stack = [start]

	path = []

	while stack:
		vertex = stack.pop()
		if vertex not in expanded_states:
			expanded_states.append(vertex)
		if vertex not in visited.keys():
			visited[vertex] = []
		
		if vertex == goal:
			print('Perform DFS using stack\npath returned {}\nexpanded_states {}\n________________'.
				format(path+[goal], expanded_states))
			break
		
		path.append(vertex)


		if IsBackTracingPoint(vertex, path[:-1], visited[vertex]):
			# print('{} 是回溯点'.format(vertex))
			path.remove(vertex)
		# 判断vertex是不是回溯点，依据 其邻接点是否都被访问
			for node in path[::-1]:
				if IsBackTracingPoint(node, path[:-1], visited[node]):
					path.remove(node)
				else:
					for ajacent in graph[node][::-1]:
						if ajacent not in path and ajacent not in visited[node]:
							stack.append(ajacent)
					visited[node].append(stack[-1])
					break
		else:
			# print('{} 不是回溯点'.format(vertex))
			for ajacent in graph[vertex][::-1]:
				if ajacent not in path:
					stack.append(ajacent)
			visited[vertex].append(stack[-1])
			if stack[-1] not in visited.keys():
				visited[stack[-1]] = []
			if stack[-1] not in visited[vertex]:
				visited[stack[-1]].append(vertex)




def bfs_queue(graph, start, goal, expanded_states):
	queue = [(start, [start])]
	expanded_states.append(start)
	while queue:
		(vertex, path) = queue.pop(0)
		for next in sorted(list(set(graph[vertex]) - set(path))):
			if next not in expanded_states:
				expanded_states.append(next)
			if next == goal:
				print('Perform BFS using queue\npath returned {}\nexpanded_states {}\n________________'.
					format(path + [next], expanded_states))
				return
			else:
				queue.append((next, path + [next]))


dfs_recursion(graph, start, [start])
dfs_stack(graph, start, goal, [])
bfs_queue(graph, start, goal, [])

"""
Given the undirected graph G1 represented as adjacency matrix:
Perform DFS using recursion. (1pt)
"""
all_node = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'p', 'q', 'r', 's']
graph_by_ajacent_matrix = [[0]*len(all_node) for _ in range(len(all_node))]

def genAjacentMatrix(all_node, graph_by_ajacent_matrix, graph):
	print('\npresent graph by Adjacent Matrix')
	for i in range(len(all_node)):
		connect_node = graph[all_node[i]]
		for node in connect_node:
			idx = all_node.index(node)
			graph_by_ajacent_matrix[i][idx] = 1
	print(' ', end=' ')
	for i in range(len(all_node)):
		print(all_node[i], end=' ')
	print()
	for i in range(len(all_node)):
		print(all_node[i], end=' ')
		for j in range(len(all_node)):
			print(graph_by_ajacent_matrix[i][j], end=' ')
		print()
	print('##############################################################\n')
	return graph_by_ajacent_matrix

"""
  a b c d e f g h p q r s 
a 0 1 1 0 0 0 0 0 0 0 0 0 
b 1 0 0 1 0 0 0 0 0 0 0 0 
c 1 0 0 1 0 1 0 0 0 0 0 0 
d 0 1 1 0 1 0 0 0 0 0 0 1 
e 0 0 0 1 0 0 0 1 0 0 1 1 
f 0 0 1 0 0 0 1 0 0 0 1 0 
g 0 0 0 0 0 1 0 0 0 0 0 0 
h 0 0 0 0 1 0 0 0 1 1 0 0 
p 0 0 0 0 0 0 0 1 0 1 0 1 
q 0 0 0 0 0 0 0 1 1 0 0 0 
r 0 0 0 0 1 1 0 0 0 0 0 0 
s 0 0 0 1 1 0 0 0 1 0 0 0
"""	



# Perform DFS using recursion
exit_flag = False
expanded_states = [start]

def dfs_recursion_ajacent_matrix(graph, start, goal, path):
	if all_node.index(start) == all_node.index(goal):
		print('Adjacent Matrix Perform DFS using recursion\npath returned {}\nexpanded_states {}\n**************'.
			format(path, expanded_states))

	else:
		for i, connect in enumerate(graph[all_node.index(start)]):
			if connect and all_node[i] not in path and all_node[i] not in expanded_states:
				expanded_states.append(all_node[i])
				dfs_recursion_ajacent_matrix(graph, all_node[i], goal, path+[all_node[i]])


def dfs_stack_ajacent_matrix(graph, start, goal, expanded_states):
	def IsBackTracingPoint(node, path, visited):
		"""
		如果没有可访问的邻接点就是回溯点
		"""
		allready_visited = 0
		connect_node = graph[all_node.index(node)]
		for i, cnode in enumerate(connect_node):
			if cnode and (all_node[i] in path or all_node[i] in visited):
				allready_visited += 1
		return True if allready_visited == sum(graph[all_node.index(node)]) else False

	visited = {}
	stack = [start]

	path = []

	while stack:
		vertex = stack.pop()
		# print(vertex)
		if vertex not in expanded_states:
			expanded_states.append(vertex)
		if vertex not in visited.keys():
			visited[vertex] = []
		
		if vertex == goal:
			print('Adjacent Matrix Perform DFS using stack\npath returned {}\nexpanded_states {}\n**************'.
				format(path+[goal], expanded_states))
			break
		
		path.append(vertex)


		if IsBackTracingPoint(vertex, path[:-1], visited[vertex]):
			# print('{} 是回溯点'.format(vertex))
			path.remove(vertex)
		# 判断vertex是不是回溯点，依据 其邻接点是否都被访问
			for node in path[::-1]:
				if IsBackTracingPoint(node, path[:-1], visited[node]):
					path.remove(node)
				else:

					for i, ajacent in enumerate(graph[all_node.index(node)][::-1]):
						if ajacent and all_node[len(all_node)-1-i] not in path and all_node[len(all_node)-1-i] not in visited[node]:
							stack.append(all_node[len(all_node)-1-i])
					visited[node].append(stack[-1])

					break
		else:
			# print('{} 不是回溯点'.format(vertex))
			for i, ajacent in enumerate(graph[all_node.index(vertex)][::-1]):
				if ajacent and all_node[len(all_node)-1-i] not in path:
					stack.append(all_node[len(all_node)-1-i])
			visited[vertex].append(stack[-1])
			if stack[-1] not in visited.keys():
				visited[stack[-1]] = []
			visited[stack[-1]].append(vertex)



def bfs_queue_ajacent_matrix(graph, start, goal, expanded_states):
	queue = [(start, [start])]
	expanded_states.append(start)
	while queue:
		(vertex, path) = queue.pop(0)
		for node in [i for i, connect in enumerate(graph[all_node.index(vertex)]) if connect and all_node[i] not in path]:
		# for next in sorted(list(set(graph[vertex]) - set(path))):
			next = all_node[node]
			if next not in expanded_states:
				expanded_states.append(next)
			if next == goal:
				print('Adjacent Matrix Perform BFS using queue\npath returned {}\nexpanded_states {}\n**************'.
					format(path + [next], expanded_states))
				return
			else:
				queue.append((next, path + [next]))

	
graph_by_ajacent_matrix = genAjacentMatrix(all_node, graph_by_ajacent_matrix, graph)

dfs_recursion_ajacent_matrix(graph_by_ajacent_matrix, start, goal, ['s'])
dfs_stack_ajacent_matrix(graph_by_ajacent_matrix, start, goal, [])
bfs_queue_ajacent_matrix(graph_by_ajacent_matrix, start, goal, [])


print('\n##############################################################################\n')
"""
Given the directed graph G2 represented as vertex-list:
"""
directed_graph = {
    'a': [],
    'b': ['a'],
    'c': ['a'],
    'd': ['b', 'c', 'e'],
    'e': ['h', 'r'],
    'f': ['c', 'g'],
    'h': ['p', 'q'],
    's': ['d', 'e', 'p'],
    'r': ['f'],
    'p': ['q'],
    'q': [],
    'g': [],
    'v': []
}
expanded_states = [start]

def directed_graph_dfs_recursion(graph, start, path):
	if start == goal:
		print('directed_graph Perform DFS using recursion\npath returned {}\nexpanded_states {}\n________________'.
			format(path, expanded_states))
	else:
		for ajacent in graph[start]:
			if ajacent not in path and ajacent not in expanded_states:
				expanded_states.append(ajacent)
				directed_graph_dfs_recursion(graph, ajacent, path+[ajacent])


def directed_graph_dfs_stack(graph, start, goal, expanded_states):

	def IsBackTracingPoint(node, path, visited):
		"""
		如果没有可访问的邻接点就是回溯点
		"""
		allready_visited = 0
		connect_node = graph[node]
		for cnode in connect_node:
			if cnode in path or cnode in visited:
				allready_visited += 1
		return True if allready_visited == len(graph[node]) else False

	visited = {}
	stack = [start]

	path = []

	while stack:
		vertex = stack.pop()
		# print(vertex)
		if vertex not in expanded_states:
			expanded_states.append(vertex)
		if vertex not in visited.keys():
			visited[vertex] = []
		
		if vertex == goal:
			print('directed_graph Perform DFS using stack\npath returned {}\nexpanded_states {}\n________________'.
				format(path+[goal], expanded_states))
			break
		
		path.append(vertex)


		if IsBackTracingPoint(vertex, path[:-1], visited[vertex]):
			# print('{} 是回溯点 '.format(vertex), end= ' ')
			path.remove(vertex)

		# 判断vertex是不是回溯点，依据 其邻接点是否都被访问
			for node in path[::-1]:
				if IsBackTracingPoint(node, path[:-1], visited[node]):
					# print('--> {} 回溯点'.format(node))
					path.remove(node)
				else:
					for ajacent in graph[node][::-1]:
						if ajacent not in path and ajacent not in visited[node]:
							stack.append(ajacent)
					visited[node].append(stack[-1])
					break
		else:
			for ajacent in graph[vertex][::-1]:
				if ajacent not in path:
					stack.append(ajacent)
			visited[vertex].append(stack[-1])


def directed_graph_bfs_queue(graph, start, goal, expanded_states):
	queue = [(start, [start])]
	expanded_states.append(start)
	while queue:
		(vertex, path) = queue.pop(0)
		for next in sorted(list(set(graph[vertex]) - set(path))):
			if next not in expanded_states:
				expanded_states.append(next)
			if next == goal:
				print('Perform BFS using queue\npath returned {}\nexpanded_states {}\n________________'.
					format(path + [next], expanded_states))
				return
			else:
				queue.append((next, path + [next]))


directed_graph_dfs_recursion(directed_graph, start, [start])
directed_graph_dfs_stack(directed_graph, start, goal, [])
directed_graph_bfs_queue(directed_graph, start, goal, [])

print('\n##############################################################################\n')

"""
Given the directed graph G2 represented as adjacency matrix:
  a b c d e f g h p q r s 
a 0 0 0 0 0 0 0 0 0 0 0 0 
b 1 0 0 0 0 0 0 0 0 0 0 0 
c 1 0 0 0 0 0 0 0 0 0 0 0 
d 0 1 1 0 1 0 0 0 0 0 0 0 
e 0 0 0 0 0 0 0 1 0 0 1 0 
f 0 0 1 0 0 0 1 0 0 0 0 0 
g 0 0 0 0 0 0 0 0 0 0 0 0 
h 0 0 0 0 0 0 0 0 1 1 0 0 
p 0 0 0 0 0 0 0 0 0 1 0 0 
q 0 0 0 0 0 0 0 0 0 0 0 0 
r 0 0 0 0 0 1 0 0 0 0 0 0 
s 0 0 0 1 1 0 0 0 1 0 0 0 
Perform DFS using recursion. (1pt)
"""
directed_graph_adjacenct_matrix = [[0]*len(all_node) for _ in range(len(all_node))]
directed_graph_adjacenct_matrix = genAjacentMatrix(all_node, directed_graph_adjacenct_matrix, directed_graph)

exit_flag = False
expanded_states = [start]

def dfs_recursion_ajacent_matrix(graph, start, goal, path):
	if all_node.index(start) == all_node.index(goal):
		print('Adjacent Matrix Perform DFS using recursion\npath returned {}\nexpanded_states {}\n**************'.
			format(path, expanded_states))
	else:
		for i, connect in enumerate(graph[all_node.index(start)]):
			if connect and all_node[i] not in path and all_node[i] not in expanded_states:
 				expanded_states.append(all_node[i])
 				dfs_recursion_ajacent_matrix(graph, all_node[i], goal, path+[all_node[i]])

def directed_dfs_stack_ajacent_matrix(graph, start, goal, expanded_states):
	def IsBackTracingPoint(node, path, visited):
		"""
		如果没有可访问的邻接点就是回溯点
		"""
		allready_visited = 0
		connect_node = graph[all_node.index(node)]
		for i, cnode in enumerate(connect_node):
			if cnode and (all_node[i] in path or all_node[i] in visited):
				allready_visited += 1
		return True if allready_visited == sum(graph[all_node.index(node)]) else False

	visited = {}
	stack = [start]

	path = []

	while stack:
		vertex = stack.pop()
		# print(vertex)
		if vertex not in expanded_states:
			expanded_states.append(vertex)
		if vertex not in visited.keys():
			visited[vertex] = []
		
		if vertex == goal:
			print('Adjacent Matrix Perform DFS using stack\npath returned {}\nexpanded_states {}\n**************'.
				format(path+[goal], expanded_states))
			break
		
		path.append(vertex)


		if IsBackTracingPoint(vertex, path[:-1], visited[vertex]):
			path.remove(vertex)
			for node in path[::-1]:
				if IsBackTracingPoint(node, path[:-1], visited[node]):
					path.remove(node)
				else:
					for i, ajacent in enumerate(graph[all_node.index(node)][::-1]):
						if ajacent and (all_node[len(all_node)-1-i] not in path and all_node[len(all_node)-1-i] not in visited[node]):
							stack.append(all_node[len(all_node)-1-i])
					if stack[-1] not in visited[node]:
						visited[node].append(stack[-1])
					break
		else:
			for i, ajacent in enumerate(graph[all_node.index(vertex)][::-1]):
				if ajacent and (all_node[len(all_node)-1-i] not in path and all_node[len(all_node)-1-i] not in visited[vertex]):
					stack.append(all_node[len(all_node)-1-i])
			if stack[-1] not in visited[vertex]:
				visited[vertex].append(stack[-1])
			

dfs_recursion_ajacent_matrix(directed_graph_adjacenct_matrix, start, goal, [start])
directed_dfs_stack_ajacent_matrix(directed_graph_adjacenct_matrix, start, goal, [])
bfs_queue_ajacent_matrix(directed_graph_adjacenct_matrix, start, goal, [])



"""
=======================================================================================
P2) Perform UCS on weighted graph G3 and G4.
=======================================================================================
"""
import heapq

graph3_vertex_list = {
	'a': [(2, 'b'), (2, 'c')],
	'b': [(2, 'a'), (1, 'd')],
	'c': [(2, 'a'), (8, 'd'), (3, 'f')],
	'd': [(1, 'b'), (8, 'c'), (2, 'e'), (3, 's')],
	'e': [(2, 'd'), (8, 'h'), (2, 'r'), (9, 's')],
    'f': [(3, 'c'), (2, 'g'), (2, 'r')],
    'h': [(8, 'e'), (4, 'p'), (4, 'q')],
    's': [(3, 'd'), (9, 'e'), (1, 'p')],
    'r': [(2, 'e'), (2, 'f')],
    'p': [(4, 'h'), (15, 'q'), (1, 's')],
    'q': [(4, 'h'), (15, 'p')],
    'g': [(2, 'f')]
}

all_node = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'p', 'q', 'r', 's']
weighted_graph_by_ajacent_matrix = [[0]*len(all_node) for _ in range(len(all_node))]

def genWeightedAjacentMatrix(all_node, ajacent_matrix, graph):
	print('################### == Adjacent Matrix == #########################')
	print('\npresent Weighted graph by Adjacent Matrix')
	for i in range(len(all_node)):
		connect_node = graph[all_node[i]]
		for node in connect_node:
			idx = all_node.index(node[1])
			ajacent_matrix[i][idx] = node[0]
	print(' ', end=' ')
	for i in range(len(all_node)):
		print(all_node[i], end=' ')
	print()
	for i in range(len(all_node)):
		print(all_node[i], end=' ')
		for j in range(len(all_node)):
			print(ajacent_matrix[i][j], end=' ')
		print()
	print('###################################################################\n')
	return ajacent_matrix

weighted_graph_by_ajacent_matrix = genWeightedAjacentMatrix(all_node, weighted_graph_by_ajacent_matrix, graph3_vertex_list)

# graph3_vertex_list = {
# 	'a': [(4, 'c'), (2, 's')],
# 	'b': [(4, 'd'), (3, 's')],
# 	'c': [(4, 'a'), (1, 'd'), (2, 'g')],
# 	'd': [(4, 'b'), (1, 'c'), (5, 'g'), (5, 's')],
# 	'g': [(2, 'c'), (5, 'd')],
# 	's': [(2, 'a'), (3, 'b'), (5, 'd')]
# }

def weighted_graph_ucs(graph, start, goal, expanded_states):
	queue = [(0, (start, [start]))]
	expanded_states.append(start)

	while queue:
		# print('ennter queue {}'.format(queue))

		(priority, expanded_pair) = heapq.heappop(queue)
		vertex, path = expanded_pair[0], expanded_pair[1]
		if vertex not in expanded_states:
			expanded_states.append(vertex)
		if vertex == goal:
			print('vertex-list Perform UCS using PQ\npath returned {}\nexpanded_states {}\n________________'.
					format(path, expanded_states))
			return

		connect_pair = graph[vertex]

		for next in connect_pair:
			if next[1] not in path:
				heapq.heappush(queue, (priority+next[0], (next[1], path+[next[1]])))


def weighted_graph_ajacent_matrix_ucs(matrix, start, goal, expanded_states):
	queue = [(0, (start, [start]))]
	expanded_states.append(start)

	while queue:
		# print('ennter queue {}'.format(queue))

		(priority, expanded_pair) = heapq.heappop(queue)
		vertex, path = expanded_pair[0], expanded_pair[1]
		if vertex not in expanded_states:
			expanded_states.append(vertex)
		if vertex == goal:
			print('adjacency matrix Perform UCS using PQ\npath returned {}\nexpanded_states {}\n________________'.
					format(path, expanded_states))
			return

		connect_pair = matrix[all_node.index(vertex)]

		for i, weight in enumerate(connect_pair):
			if weight and all_node[i] not in path:
				heapq.heappush(queue, (priority+weight, (all_node[i], path+[all_node[i]])))



weighted_graph_ucs(graph3_vertex_list, start, goal, [])	
weighted_graph_ajacent_matrix_ucs(weighted_graph_by_ajacent_matrix, start, goal, [])			



"""
#############################################################################
Given the directed weighted graph G4 represented as vertex-list:
#############################################################################
"""
graph4_directed_vertex_list = {
	'a': [],
	'b': [(2, 'a')],
	'c': [(2, 'a')],
	'd': [(1, 'b'), (8, 'c'), (2, 'e')],
	'e': [(8, 'h'), (2, 'r')],
    'f': [(3, 'c'), (2, 'g')],
    'h': [(4, 'p'), (4, 'q')],
    's': [(3, 'd'), (9, 'e'), (1, 'p')],
    'r': [(2, 'f')],
    'p': [(15, 'q')],
    'q': [],
    'g': []
}


directed_weighted_graph_by_ajacent_matrix = [[0]*len(all_node) for _ in range(len(all_node))]
directed_weighted_graph_by_ajacent_matrix = genWeightedAjacentMatrix(all_node, directed_weighted_graph_by_ajacent_matrix, graph4_directed_vertex_list)


weighted_graph_ucs(graph4_directed_vertex_list, start, goal, [])
weighted_graph_ajacent_matrix_ucs(directed_weighted_graph_by_ajacent_matrix, start, goal, [])

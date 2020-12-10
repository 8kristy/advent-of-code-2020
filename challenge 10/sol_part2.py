with open("input", "r") as f:
    adapters =  [int(x) for x in f.readlines()]
    adapters.sort()

graph = dict()

# Converting the input into a graph such that difference between two nodes is at most 3

# Getting the starting points
graph[0] = list()
graph[0].append(adapters[0])

if adapters[1] < 4:
    graph[0].append(adapters[1])

if adapters[2] < 4:
    graph[0].append(adapters[2])    

# Everything in between
for i in range(len(adapters) - 3):
    graph[adapters[i]] = list()
    if adapters[i + 1] - adapters[i] < 4:
        graph[adapters[i]].append(adapters[i + 1])

    if adapters[i + 2] - adapters[i] < 4:
        graph[adapters[i]].append(adapters[i + 2]) 

    if adapters[i + 3] - adapters[i] < 4:
        graph[adapters[i]].append(adapters[i + 3])  

# Last 3 bits we didn't count in the loop

graph[adapters[-3]] = list()
graph[adapters[-2]] = list()
graph[adapters[-1]] = list()        

if adapters[-2] - adapters[-3] < 4:
    graph[adapters[-3]].append(adapters[-2])

if adapters[-1] - adapters[-3] < 4:
    graph[adapters[-3]].append(adapters[-1])
    
if adapters[-1] - adapters[-2] < 4:
    graph[adapters[-2]].append(adapters[-1])

graph[adapters[-1]] = [adapters[-1] + 3]  

# Going backwards on our graph, calculating the paths possible from 
# each node and adding them to the previous
totals = dict()
totals[adapters[-1]] = 1

for node in reversed(graph):
    if node != adapters[-1]:
        totals[node] = 0
        for dest in graph[node]:
            totals[node] += totals[dest]

print(totals[0])            
            
    
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # Перебрать все узлы
        cost = costs[node]
        # Если этот узел с наименьшей стоимостью из уже виденных и он еще не был обработан
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost  # Он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # Найти узел с наименьшей стоимостью среди необработанных
while node is not None:  # Если обработаны все узлы,цикл while завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # Перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # Если к соседу можно быстрее добраться через текущий узел
            costs[n] = new_cost  # Обновить стоимость для этого узла
            parents[n] = node  # Этот узел становится новым родителем для соседа
    processed.append(node)  # Узел помечается как обработанный
    node = find_lowest_cost_node(costs)  # Найти следующий узел для обработки и повторить цикл

print("Cost from the start to each node:")
print(costs)

from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()  # Создаем новую очередь
    search_queue += graph[name]  # Все соседи добавляются в очередь поиска
    searched = set()  # Этот массив используется для отслеживания уже проверенных людей
    while search_queue:  # Пока очередь не пуста
        person = search_queue.popleft()  # Из очереди извлекается первый человек
        if not person in searched:  # Человек проверяется только в том случае, если он не проверялся ранее
            if person_is_seller(person):  # Проверяем, является ли этот человек продавцом манго
                print(person, "is a mango seller!")  # Да, этот человек продавец манго
                return True
            else:
                search_queue += graph[person]  # Нет,не является.Все друзья этого человека добавляются в очередь поиска
                searched.add(person)  # Человек помечается как уже проверенный
    return False  # Если выполнение дошло до этой строки, значит, в очереди нет продавца манго


search("you")

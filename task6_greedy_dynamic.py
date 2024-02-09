class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def greedy_algorithm(items_dict, budget):
    # Включення назви страви у конструктор Item
    items = [Item(name, info['cost'], info['calories']) for name, info in items_dict.items()]
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_calories = 0
    chosen_items = []

    for item in items:
        if budget >= item.weight:
            budget -= item.weight
            total_calories += item.value
            chosen_items.append(item)  
    
    return total_calories, chosen_items

def dynamic_programming(items_data, budget):
    # Створення списку об'єктів Item    
    items = [Item(name, info['cost'], info['calories']) for name, info in items_data.items()]
    n = len(items)

    # Ініціалізація таблиці
    dp = [[0 for _ in range(budget + 1)] for _ in range(n+1)]

    # будуємо таблицю
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items[i-1].weight <= w:
                dp[i][w] = max(items[i-1].value + dp[i-1][w-items[i-1].weight], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    chosen_items_dp = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items_dp.append(items[i-1].name)
            w -= items[i-1].weight
    
    total_calories_dp = dp[n][budget]

    return total_calories_dp, chosen_items_dp[::-1]


items_data = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100 

# Виклик функції greedy_algorithm і збереження результатів
total_calories, chosen_items = greedy_algorithm(items_data, budget)
chosen_item_names = [item.name for item in chosen_items]  # Беремо назви з об'єктів Item

# Виведення результатів
print("Результат жадібного алгоритму")
print("-----------------------------")
print(f"Загальна кількість калорій: {total_calories}")
print(f"Обрані страви: {chosen_item_names}")
print('\n')

# Виклик функції dynamic_programming
total_calories_dp, chosen_items_dp = dynamic_programming(items_data, budget)

# Виведення результатів
print("Результат динамічного програмування")
print("-----------------------------------")
print(f"Загальна кількість калорій: {total_calories_dp}")
print(f"Обрані страви: {chosen_items_dp}")
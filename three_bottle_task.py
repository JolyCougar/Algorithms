import random

# Определяем банки с орехами
jars = {
    "Кешью": "фисташки",  # Перепутанные названия
    "Фисташки": "арахис",
    "Арахис": "кешью"
}

# Перемешиваем банки
jars_list = list(jars.items())
random.shuffle(jars_list)

# Выводим перепутанные банки
print("Перепутанные банки:")
for name, _ in jars_list:
    print(name)

# Выбираем банку с названием "Кешью"
chosen_jar_name = "Кешью"
chosen_jar = next((jar for jar in jars_list if jar[0] == chosen_jar_name), None)

if chosen_jar:
    # Достаем один орех из выбранной банки
    actual_nuts = jars[chosen_jar[0]]
    print(f"\nВы достали орех из банки '{chosen_jar[0]}': это {actual_nuts}.")

    # Определяем, что находится в остальных банках
    if actual_nuts == "фисташки":
        print("Следовательно, банка 'Фисташки' содержит кешью, а банка 'Арахис' содержит арахис.")
    elif actual_nuts == "арахис":
        print("Следовательно, банка 'Арахис' содержит фисташки, а банка 'Фисташки' содержит кешью.")
    else:
        print("Ошибка: не удалось определить орехи.")
else:
    print("Банка с названием 'Кешью' не найдена.")

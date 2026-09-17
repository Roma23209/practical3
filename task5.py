shopping_list = ["яблоки", "молоко", "хлеб", "яблоки"]
shopping_list.append("сыр")
print("Список покупок:", shopping_list)

unique_items = set(shopping_list) # это множество автоматически удалил повторяющийся элемент и сохраняет порядок
print("Множество уникальных товаров:", unique_items)

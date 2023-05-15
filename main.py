class FoodItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __call__(self, *args, **kwargs):
        lst_1 = [0]
        lst_2 = [1]
        lst_3 = [2]

        return lst_1, lst_2, lst_3


class Menu(FoodItem):
    def __init__(self, g, v, n):
        super().__init__(g, v, n)

        self.list_dishes = []
        self.dict_dishes = {}

    def add_dish(self, name, description, price):
        self.dict_dishes[name] = price
        self.list_dishes.append(description)

    def remove_dish(self, name_dish):
        if name_dish in self.dict_dishes:
            del self.dict_dishes[name_dish]
            self.list_dishes.remove(name_dish)
        else:
            print("Немає такої страви у меню ресторану")

    def __str__(self):
        result = "Ось усі наші страви з нашого ресторану:\n"
        for dish, price, description in zip(self.dict_dishes.keys(), self.dict_dishes.values(), self.list_dishes):
            result += f"Страва: {dish} | Цiна: {price} | Опис страв: {description}\n"
        return result

    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class Order(Menu):
    def __init__(self, g, v, n):
        super().__init__(g, v, n)

        self.items = {}

    def add_item(self, item_key, item_value):
        self.items[item_key] = item_value
        # else:
        #     raise TypeError("Нема такої страви в нашому меню")

    def total(self):
        total = 0
        for i in self.items.values():
            total += i
        return total

    def __call__(self, *args, **kwargs):
        lst_1 = [0]
        lst_2 = [1]
        lst_3 = [2]

        return lst_1, lst_2, lst_3


class Restaurant:
    # def __init__(self, g, v, n):
    #     super().__init__(g, v, n)
    #
    #     self.order = Order(g, v, n)

    def order_item(self, item_name):

        item = next((x for x in order.items if x[0] == item_name), None)
        if item:
            order.add_item(item[0], item[1])

    def remove_order(self, item_name):
        item = next((x for x in order.items.keys() if x == item_name), None)
        if item:
            del order.items[item]

    def get_bill(self):
        total = 0
        for i in order.items.values():
            total += i
        return total

    def save_order(self):
        with open('order.txt', 'w') as file:
            for item_name, item_price in order.items.items():
                file.write(f"Name: {item_name} - {item_price}\n")
                file.write('\n')
            file.write(f"Total: {self.get_bill()}")


item = FoodItem('Pizza', 'Peperoni pizza', 250)

a, b, c = item()

menu = Menu(a, b, c)

menu.add_dish('Pizza', 'Peperoni pizza', 250)

order = Order(a, b, c)

order.add_item('Pizza', 250)

print(menu)

restaurant = Restaurant()
restaurant.order_item('Pizza')
print(restaurant.get_bill())
restaurant.save_order()

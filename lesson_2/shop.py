class Shop:

    total_amount = 0

    def __init__(self, name, amount_goods_sold):
        self.name = name
        self.amount_goods_sold = amount_goods_sold
        Shop.total_amount += self.amount_goods_sold

    def increase_sold(self, other): 
        self.amount_goods_sold += other
        Shop.total_amount += other

    def __str__(self):
        return f'The shop "{self.name}" sold {self.amount_goods_sold} goods.\nTotal = {self.total_amount}'


fish_shop = Shop("Fish", 100)
meal_shop = Shop("Meal", 200)
print("-" * 45)
print(fish_shop)
print(meal_shop)
print("-" * 45)
fish_shop.increase_sold(100)
meal_shop.increase_sold(300)
print(fish_shop)
print(meal_shop)
print("-" * 45)


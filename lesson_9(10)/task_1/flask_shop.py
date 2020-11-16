#1) Создать базу данных товаров, у товара есть: Категория (связанная
#таблица), название, есть ли товар в продаже или на складе, цена, кол-во
#единиц.Создать html страницу. На первой странице выводить ссылки на все
#категории, при переходе на категорию получать список всех товаров в
#наличии ссылками, при клике на товар выводить его цену, полное описание и
#кол-во единиц в наличии.



from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def show_categories():
    categories = list()
    connection = sqlite3.connect('catalogue.db')
    cursor = connection.cursor()
    cursor.execute("SELECT categ_name FROM category")
    for category in cursor:
        categories.append(*category)
    connection.close()
    return render_template('index.html', categories=categories)


@app.route('/<category>')
def show_available_products(category):
    products = list()
    connection = sqlite3.connect('catalogue.db')
    cursor = connection.cursor()
    cursor.execute("SELECT category.categ_name, products.prod_name FROM products "
                   "INNER JOIN category ON products.categ_id=category.categ_id "
                   "WHERE products.is_available = 1 AND category.categ_name = ?", [category])
    for product in cursor:
        products.append(product[1])
    connection.close()
    return render_template('products.html', products=products, category=category)


@app.route('/<category>/<product>')
def show_product_details(category, product):
    products_description = list()
    connection = sqlite3.connect('catalogue.db')
    cursor = connection.cursor()
    cursor.execute("SELECT products.prod_name, products.price, products.quantity "
                   "FROM products INNER JOIN category on products.categ_id=category.categ_id "
                   "WHERE category.categ_name= ? AND products.prod_name = ?",  [category, product])
    for product in cursor:
        products_description.append(product)
    connection.close()
    return render_template('products_details.html',
                           prod_name=product[0],
                           prod_price=product[1],
                           prod_qty=product[2])


if __name__ == '__main__':
    app.run(host='127.0.0.2', port=4444, debug=True)

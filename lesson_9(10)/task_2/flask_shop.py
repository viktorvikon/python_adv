#1) Создать базу данных товаров, у товара есть: Категория (связанная
#таблица), название, есть ли товар в продаже или на складе, цена, кол-во
#единиц.Создать html страницу. На первой странице выводить ссылки на все
#категории, при переходе на категорию получать список всех товаров в
#наличии ссылками, при клике на товар выводить его цену, полное описание и
#кол-во единиц в наличии.
#2) Создать страницу для администратора, через которую он может добавлять
#новые товары и категории.



from flask import Flask, render_template, request
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


# ADMIN
@app.route('/admin')
def admin_main():
    categories = list()
    connection = sqlite3.connect('catalogue.db')
    cursor = connection.cursor()
    cursor.execute("SELECT categ_name FROM category")
    for category in cursor:
        categories.append(*category)
    connection.close()
    return render_template('admin_main.html', categories=categories)


@app.route('/admin/category', methods=["GET", "POST"])
def admin_add_category():
    if request.method == "GET":
        return render_template('admin_add_category.html')
    else:
        new_category = request.form["new_category"]
        connection = sqlite3.connect('catalogue.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO category ('categ_name') VALUES (?)", [new_category])
        connection.commit()
        connection.close()
        return render_template('admin_add_category.html', new_category=new_category)


@app.route('/admin/product', methods=["GET", "POST"])
def admin_add_product():
    if request.method == "GET":
        categories = list()
        connection = sqlite3.connect('catalogue.db')
        cursor = connection.cursor()
        cursor.execute("SELECT categ_name FROM category")
        for category in cursor:
            categories.append(*category)
        connection.close()
        return render_template('admin_add_product.html', categories=categories)
    else:
        pr_name = request.form["pr_name"]
        categ_name = request.form["categ_name"]
        pr_price = float(request.form["pr_price"])
        pr_qty = int(request.form["pr_qty"])
        is_avail = 1
        connection = sqlite3.connect('catalogue.db')
        cursor = connection.cursor()
        cursor.execute("SELECT categ_id from category where categ_name=?", [categ_name])
        categ_id = list(cursor.fetchall())[0][0]
        connection.close()
        connection = sqlite3.connect('catalogue.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products ('prod_name', 'categ_id', 'is_available', 'quantity', 'price')"
                       "VALUES (?,?,?,?,?)", [pr_name, categ_id, is_avail, pr_qty, pr_price])
        connection.commit()
        connection.close()
        return render_template('admin_add_product.html', new_product=pr_name)


if __name__ == '__main__':
    app.run(host='127.0.0.2', port=4444, debug=True)

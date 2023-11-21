from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/employee')
def employee():
    return render_template('Employee.html')


@app.route('/employeeedit')
def employeeedit():
    return render_template('EmployeeEdit.html')


@app.route('/employeenew')
def employeenew():
    return render_template('EmployeeNew.html')


@app.route('/inventory')
def inventory():
    return render_template('Inventory.html')


@app.route('/inventoryedit')
def inventoryedit():
    return render_template('InventoryEdit.html')


@app.route('/inventorynew')
def inventorynew():
    return render_template('InventoryNew.html')


@app.route('/product')
def product():
    return render_template('Product.html')


@app.route('/productedit')
def productedit():
    return render_template('ProductEdit.html')


@app.route('/productnew')
def productnew():
    return render_template('ProductNew.html')


@app.route('/revenue')
def revenue():
    return render_template('Revenue.html')


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # 处理添加产品的逻辑
        return redirect(url_for('product_management'))
    return render_template('add_product.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, jsonify
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


next_employee_id = 1
employee_info = {}  # 字典来存储员工信息
current_employee = None  # 用于存储当前编辑的员工名字


@app.route('/set_current_employee', methods=['POST'])
def set_current_employee():
    global current_employee
    data = request.json
    current_employee = data['id']
    print(current_employee)
    return jsonify({"message": "Current employee set"}), 200


@app.route('/get_current_employee', methods=['GET'])
def get_current_employee():
    global current_employee
    if current_employee in employee_info:
        return jsonify(current_employee, employee_info[current_employee])
    else:
        return jsonify({"error": "Employee not found"}), 404


@app.route('/add_employee', methods=['POST'])
def add_employee():
    global next_employee_id
    data = request.json
    employee_info[next_employee_id] = {
        'name': data['name'],
        'position': data['position'],
        'AcworkHours': 0,
        'workHours': data['workHours'],
        'salary': data['salary']
    }
    next_employee_id += 1
    return jsonify({"message": "Employee added"}), 200


@app.route('/update_employee', methods=['POST'])
def update_employee():
    data = request.json
    print(data)
    print(employee_info)
    print(next_employee_id)
    employee_id = int(data['id'])
    if employee_id in employee_info:
        employee_info[employee_id] = {
            'name': data['name'],
            'position': data['position'],
            'AcworkHours': data['AcworkHours'],
            'workHours': data['workHours'],
            'salary': data['salary']
        }
        return jsonify({"message": "Employee updated"}), 200
    else:
        return jsonify({"error": "Employee not found"}), 404


@app.route('/delete_employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    if employee_id in employee_info:
        del employee_info[employee_id]
        return jsonify({"message": "Employee deleted"}), 200
    else:
        return jsonify({"error": "Employee not found"}), 404


@app.route('/get_employees', methods=['GET'])
def get_employees():
    return jsonify(employee_info)


# -----------------------------------------------------------------------------------------------------
# Product

next_product_id = 1
product_info = {}  # 字典来存储产品信息
current_product = None  # 用于存储当前编辑的产品名字


@app.route('/set_current_product', methods=['POST'])
def set_current_product():
    global current_product
    data = request.json
    current_product = data['id']
    print(current_product)
    return jsonify({"message": "Current product set"}), 200


@app.route('/get_current_product', methods=['GET'])
def get_current_product():
    global current_product
    if current_product in product_info:
        return jsonify(current_product, product_info[current_product])
    else:
        return jsonify({"error": "product not found"}), 404


@app.route('/add_product', methods=['POST'])
def addproduct():
    global next_product_id
    data = request.json
    product_info[next_product_id] = {
        'name': data['name'],
        'sold_quantity': data['sold_quantity'],
        'remaining_quantity': data['remaining_quantity'],
        'selling_price': data['selling_price']
    }
    next_product_id += 1
    return jsonify({"message": "product added"}), 200


@app.route('/update_product', methods=['POST'])
def update_product():
    data = request.json
    print(data)
    print(product_info)
    print(next_product_id)
    product_id = int(data['id'])
    if product_id in product_info:
        product_info[product_id] = {
            'name': data['name'],
            'sold_quantity': data['sold_quantity'],
            'remaining_quantity': data['remaining_quantity'],
            'selling_price': data['selling_price']
        }
        return jsonify({"message": "product updated"}), 200
    else:
        return jsonify({"error": "product not found"}), 404


@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in product_info:
        del product_info[product_id]
        return jsonify({"message": "product deleted"}), 200
    else:
        return jsonify({"error": "product not found"}), 404


@app.route('/get_product', methods=['GET'])
def get_product():
    return jsonify(product_info)


# -----------------------------------------------------------------------------------------------------
# Inventory

next_inventory_id = 1
inventory_info = {}  # 字典来存储产品信息
current_inventory = None  # 用于存储当前编辑的产品名字


@app.route('/set_current_inventory', methods=['POST'])
def set_current_inventory():
    global current_inventory
    data = request.json
    current_inventory = data['id']
    print(current_inventory)
    return jsonify({"message": "Current inventory set"}), 200


@app.route('/get_current_inventory', methods=['GET'])
def get_current_inventory():
    global current_inventory
    if current_inventory in inventory_info:
        return jsonify(current_inventory, inventory_info[current_inventory])
    else:
        return jsonify({"error": "inventory not found"}), 404


@app.route('/add_inventory', methods=['POST'])
def addinventory():
    global next_inventory_id
    data = request.json
    inventory_info[next_inventory_id] = {
        'name': data['name'],
        'remaining_quantity': data['remaining_quantity'],
        'purchase_price': data['purchase_price'],
        'selling_price': data['selling_price'],
        'next_restock_date': data['next_restock_date'],
    }
    next_inventory_id += 1
    return jsonify({"message": "inventory added"}), 200


@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    data = request.json
    print(data)
    print(inventory_info)
    print(next_inventory_id)
    inventory_id = int(data['id'])
    if inventory_id in inventory_info:
        inventory_info[inventory_id] = {
            'name': data['name'],
            'remaining_quantity': data['remaining_quantity'],
            'purchase_price': data['purchase_price'],
            'selling_price': data['selling_price'],
            'next_restock_date': data['next_restock_date'],
        }
        return jsonify({"message": "inventory updated"}), 200
    else:
        return jsonify({"error": "inventory not found"}), 404


@app.route('/delete_inventory/<int:inventory_id>', methods=['DELETE'])
def delete_inventory(inventory_id):
    if inventory_id in inventory_info:
        del inventory_info[inventory_id]
        return jsonify({"message": "inventory deleted"}), 200
    else:
        return jsonify({"error": "inventory not found"}), 404


@app.route('/get_inventory', methods=['GET'])
def get_inventory():
    print(inventory_info)
    return jsonify(inventory_info)


if __name__ == '__main__':
    app.run(debug=True)

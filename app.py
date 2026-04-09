from flask import Flask, request, jsonify

app = Flask(__name__)

# fake database
products = []

@app.route('/')
def home():
    return "ERP Server Running"

# @app.route('/add-product', methods=['POST'])
# def add_product():
#     data = request.get_json()

#     name = data.get('name')
#     quantity = data.get('quantity')

#     product = {
#         "name": name,
#         "quantity": quantity
#     }

#     products.append(product)

#     return jsonify({"message": "Product added", "product": product})
@app.route('/add-product', methods=['POST'])
def add_product():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get('name')
    quantity = data.get('quantity')

    if not name:
        return jsonify({"error": "Product name required"}), 400

    if not quantity:
        return jsonify({"error": "Quantity required"}), 400

    if not isinstance(quantity, int):
        return jsonify({"error": "Quantity must be integer"}), 400

    product = {
        "name": name,
        "quantity": quantity
    }

    products.append(product)

    return jsonify({"message": "Product added", "product": product})

@app.route('/products')
def get_products():
    return jsonify(products)

@app.route('/search')
def search_product():
    name = request.args.get('name')

    result = [p for p in products if p['name'] == name]

    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)
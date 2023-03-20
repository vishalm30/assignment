from flask import request, jsonify

@app.route('/orders', methods = ['POST'])

def add_order():
    data = request.json
    order = Order(id=data['id'], status=data['status'],items=data['items'],total=data['total'],currency_unit=data['currencyUnit'])
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order added successfully'})

@app.route('/orders/<id>', methods=['PUT'])
def update_order_status(id):
    order = Order.query.get_or_404(id)
    order.status = request.json['status']
    db.session.commit()
    return jsonify({'message': 'Order status updated successfully'})

# Retrieve orders
@app.route('/orders', methods=['GET'])
def get_orders():
    query_params = request.args.to_dict()
    orders = Order.query.filter_by(**query_params).all()
    sorted_orders = sorted(orders, key=lambda o: o.id)
    return jsonify([order.__dict__ for order in sorted_orders])
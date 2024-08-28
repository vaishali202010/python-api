from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
items = []

# Helper function to find item by id
def find_item(item_id):
    return next((item for item in items if item['id'] == item_id), None)

# GET /items - List all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# POST /items - Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# PUT /items/<int:item_id> - Update an item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = find_item(item_id)
    if item:
        item.update(request.json)
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

# DELETE /items/<int:item_id> - Delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return '', 204

# Start the server
if __name__ == '__main__':
    app.run(debug=True)

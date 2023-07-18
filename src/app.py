from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def get_data():
    json_data = jsonify(todos)
    return json_data

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)

    todo_list = jsonify(todos)
    return todo_list

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]

    todo_list = jsonify(todos)
    return todo_list 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
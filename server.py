from flask import Flask, request, jsonify
import json

app = Flask(__name__)
employee_data_file = 'employees.json'

# Load existing employee data from the JSON file
def load_employee_data():
    try:
        with open(employee_data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save employee data to the JSON file
def save_employee_data(data):
    with open(employee_data_file, 'w') as file:
        json.dump(data, file, indent=4)

@app.route("/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route('/employee', methods=['POST'])
def create_employee():
    data = request.get_json()

    employee_data = load_employee_data()

    # Generate a unique employee ID based on the number of existing employees
    employee_id = str(len(employee_data) + 1)

    employee = {
        "employeeId": employee_id,
        "name": data['name'],
        "city": data['city']
    }

    employee_data.append(employee)

    # Save the updated employee data to the JSON file
    save_employee_data(employee_data)

    return jsonify({"employeeId": employee_id}), 201

@app.route('/employees/all', methods=['GET'])
def get_all_employees():
    employee_data = load_employee_data()
    return jsonify(employee_data)

@app.route('/employee/<id>', methods=['GET'])
def get_employee(id):
    employee_data = load_employee_data()
    employee = next((e for e in employee_data if e['employeeId'] == id), None)
    if employee is None:
        return jsonify({"message": f"Employee with ID {id} was not found"}), 404
    return jsonify(employee)

# Rest of your code for searching and filtering employees...

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

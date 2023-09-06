from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Specify the JSON filename
json_filename = "data.json"

# Load existing data from the JSON file
try:
    with open(json_filename, "r") as json_file:
        employee_database = json.load(json_file)
except FileNotFoundError:
    employee_database = []

def save_employee_data():
    # Save the employee data to the JSON file
    with open(json_filename, "w") as json_file:
        json.dump(employee_database, json_file, indent=4)

def generate_employee_id():
    return str(len(employee_database) + 1)

# Greeting
@app.route("/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

# Create Employee
@app.route('/employee', methods=['POST'])
def create_employee():
    data = request.get_json()

    # Generate a unique employee ID (You can implement this as needed)
    employee_id = generate_employee_id()

    employee = {
        "employeeId": employee_id,
        "name": data['name'],
        "city": data['city']
    }

    employee_database.append(employee)
    
    # Save the updated data to the JSON file
    save_employee_data()

    return jsonify({"employeeId": employee_id}), 201

# Get all Employee details
@app.route('/employees/all', methods=['GET'])
def get_all_employees():
    return jsonify(employee_database)

# Get Employee details by ID
@app.route('/employee/<id>', methods=['GET'])
def get_employee(id):
    for employee in employee_database:
        if employee['employeeId'] == id:
            return jsonify(employee)
    return jsonify({"message": f"Employee with ID {id} was not found"}), 404

# Update and Delete routes can be added similarly

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

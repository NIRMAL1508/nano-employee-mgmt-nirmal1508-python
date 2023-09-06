from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
employee_database = []
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

    return jsonify({"employeeId": employee_id}), 201


# Get all Employee details
@app.route('/employees/all', methods=['GET'])
def get_all_employees():
    return jsonify(employee_database)

# Get all Employee details
def find_employee_by_id(employee_id):
    for employee in employee_database:
        if employee['employeeId'] == employee_id:
            return employee
    return None

# Get Employee details
@app.route('/employee/<id>', methods=['GET'])
def get_employee(id):
    employee = find_employee_by_id(id)
    if employee is None:
        return jsonify({"message": f"Employee with {id} was not found"}), 404
    return jsonify(employee)

# Search employees
def search_employees(search_request):

    if "fields" not in search_request:
        return jsonify({"error": "The 'fields' field is required"}), 400

    fields = search_request["fields"]

    if not fields:
        return jsonify({"error": "At least one filter criterion is required"}), 400

    condition = search_request.get("condition", "AND")

    # Initialize a list to store matching employees
    matching_employees = []

    for employee in employee_database:
        if evaluate_filters(employee, fields, condition):
            matching_employees.append(employee)

    return jsonify(matching_employees), 200

# Evaluate filter criteria
def evaluate_filters(employee, fields, condition):
    for criterion in fields:
        fieldName = criterion.get("fieldName")
        eq = criterion.get("eq")
        neq = criterion.get("neq")

        if not fieldName or (eq is None and neq is None):
            continue

        if eq is not None and employee.get(fieldName) == eq:
            if condition == "OR":
                return True
        elif neq is not None and employee.get(fieldName) != neq:
            if condition == "OR":
                return True
        elif condition == "AND":
            return False

    return condition == "OR"


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
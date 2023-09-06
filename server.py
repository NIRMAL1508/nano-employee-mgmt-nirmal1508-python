from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'  # SQLite database
db = SQLAlchemy(app)

# Define a database model
class Employee(db.Model):
    employeeId = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))

db.create_all()

def generate_employee_id():
    return str(Employee.query.count() + 1)

# Greeting
@app.route("/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

# Create Employee
@app.route('/employee', methods=['POST'])
def create_employee():
    data = request.get_json()

    # Generate a unique employee ID
    employee_id = generate_employee_id()

    employee = Employee(
        employeeId=employee_id,
        name=data['name'],
        city=data['city']
    )

    db.session.add(employee)
    db.session.commit()

    return jsonify({"employeeId": employee_id}), 201

# Get all Employee details
@app.route('/employees/all', methods=['GET'])
def get_all_employees():
    employees = Employee.query.all()
    employee_list = [{"employeeId": employee.employeeId, "name": employee.name, "city": employee.city} for employee in employees]
    return jsonify(employee_list)

# Get Employee details
@app.route('/employee/<id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"message": f"Employee with {id} was not found"}), 404
    return jsonify({"employeeId": employee.employeeId, "name": employee.name, "city": employee.city})

def evaluate_filters(employee, filters, condition="AND"):
    if not filters:
        return True  # No filters, so consider it a match

    if condition == "AND":
        return all(apply_filter(employee, filter_data) for filter_data in filters)
    elif condition == "OR":
        return any(apply_filter(employee, filter_data) for filter_data in filters)
    else:
        return False

def apply_filter(employee, filter_data):
    field_name = filter_data.get("fieldName")
    eq_value = filter_data.get("eq")
    neq_value = filter_data.get("neq")

    if field_name == "name":
        return (eq_value and employee.name == eq_value) or (neq_value and employee.name != neq_value)
    elif field_name == "city":
        return (eq_value and employee.city == eq_value) or (neq_value and employee.city != neq_value)
    else:
        return False  # Unknown field name

@app.route('/employees/search', methods=['POST'])
def search_employees():
    search_request = request.get_json()

    if "fields" not in search_request:
        return jsonify({"error": "The 'fields' field is required"}), 400

    fields = search_request["fields"]

    if not fields:
        return jsonify({"error": "At least one filter criterion is required"}), 400

    condition = search_request.get("condition", "AND")

    employees = Employee.query.all()
    matching_employees = [employee for employee in employees if evaluate_filters(employee, fields, condition)]

    return jsonify(matching_employees), 200

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

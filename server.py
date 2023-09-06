from flask import Flask

app = Flask(__name__)

# Greeting 
@app.route("/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

# Create Employee
@app.route('/employee', methods=['POST'])
def create_employee():
    return {}

# Get all Employee details
@app.route('/employees/all', methods=['GET'])
def get_all_employees():
    return []

# Get Employee details
@app.route('/employee/<id>', methods=['GET'])
def get_employee(id):
    return {}

# Search employees
def search_employees(search_request):
    return {}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')